#!/usr/bin/env python3
"""Token-efficient CLI over the public seloger.com search endpoints.

Three public JSON endpoints power the whole flow. None require an auth cookie:
the only gate is DataDome, which curl_cffi clears by impersonating a real
Chrome TLS/JA3 fingerprint.

  POST /search-mfe-bff/autocomplete   name        -> placeId(s)   (`places` cmd)
  POST /serp-bff/search               criteria    -> classified IDs + totalCount
  GET  /classifiedList/{id,id,...}    IDs         -> full listing detail

`search` chains all three and prints a compact digest (one listing per line),
because the raw detail payload is ~9 KB per listing — far too heavy to hand back
to a model verbatim.

Requires: pip install curl_cffi
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from typing import Any, Literal, TypedDict

try:
    from curl_cffi import requests as cffi
except ImportError:  # pragma: no cover - dependency guard
    sys.exit("Missing dependency: pip install curl_cffi")

BASE = "https://www.seloger.com"
IMPERSONATE = "chrome"
HEADERS = {
    "origin": BASE,
    "referer": f"{BASE}/classified-search",
    "accept": "application/json",
    "content-type": "application/json",
    "x-language": "fr",
}
# placeIds look like AD08FR2038 / POCOFR249 / NBH2FR9829 (type prefix + FR + int).
PLACE_ID_RE = re.compile(r"^[A-Z0-9]{4}FR\d+$")
# Place taxonomy returned by the autocomplete `type_key`.
PLACE_TYPES = ["HONU", "NBH1", "NBH3", "AD09", "NBH2", "AD08", "AD06", "AD04", "POCO", "AD02"]
TYPE_LABELS = {"AD08": "ville", "POCO": "code postal", "NBH1": "quartier",
               "NBH2": "quartier", "NBH3": "quartier", "AD04": "département",
               "AD02": "pays", "AD06": "commune", "AD09": "secteur"}

Distribution = Literal["Buy", "Rent"]
Order = Literal["Default", "PriceAsc", "PriceDesc", "DateDesc"]


class Place(TypedDict):
    id: str
    type: str
    label: str
    zips: list[str]


class Listing(TypedDict):
    id: str
    price: str
    price_sqm: str | None
    rooms: int | None
    bedrooms: int | None
    surface: int | None
    floor: str | None
    title: str
    city: str | None
    zip: str | None
    district: str | None
    dpe: str | None
    agency: str | None
    flags: list[str]
    url: str


def _post(path: str, body: dict[str, Any]) -> Any:
    r = cffi.post(f"{BASE}{path}", json=body, impersonate=IMPERSONATE, headers=HEADERS, timeout=25)
    if r.status_code != 200:
        sys.exit(f"POST {path} -> HTTP {r.status_code}: {r.text[:200]}")
    return r.json()


def _get(path: str) -> Any:
    r = cffi.get(f"{BASE}{path}", impersonate=IMPERSONATE, headers=HEADERS, timeout=25)
    if r.status_code != 200:
        sys.exit(f"GET {path} -> HTTP {r.status_code}: {r.text[:200]}")
    return r.json()


def autocomplete(text: str, limit: int = 10) -> list[Place]:
    """Resolve a free-text location to candidate placeIds (best match first)."""
    raw = _post("/search-mfe-bff/autocomplete", {
        "text": text, "limit": limit,
        "placeTypes": PLACE_TYPES, "parentTypes": PLACE_TYPES, "locale": "fr",
    })
    out: list[Place] = []
    for it in raw:
        out.append(Place(
            id=it["id"],
            type=it.get("type_key", ""),
            label=(it.get("labels") or [""])[0],
            zips=it.get("postal_codes") or [],
        ))
    return out


def resolve(where: str) -> str:
    """A placeId is used as-is; anything else is resolved to the top autocomplete hit."""
    if PLACE_ID_RE.match(where):
        return where
    hits = autocomplete(where, limit=1)
    if not hits:
        sys.exit(f"No place found for {where!r}")
    h = hits[0]
    print(f"# {where!r} -> {h['label']} [{TYPE_LABELS.get(h['type'], h['type'])}] {h['id']}",
          file=sys.stderr)
    return h["id"]


def search_ids(criteria: dict[str, Any], limit: int, order: Order) -> tuple[int, list[str]]:
    """Page through /serp-bff/search accumulating classified IDs up to `limit`."""
    ids: list[str] = []
    total = 0
    page = 1
    while len(ids) < limit:
        want = min(limit - len(ids), 100)
        res = _post("/serp-bff/search", {
            "criteria": criteria,
            "paging": {"page": page, "size": want, "order": order},
        })
        total = res.get("totalCount", 0)
        batch = [c["id"] for c in res.get("classifieds", [])]
        if not batch:
            break
        ids.extend(batch)
        if len(ids) >= total:
            break
        page += 1
    return total, ids[:limit]


def _facts(hard: dict[str, Any]) -> dict[str, Any]:
    by_type = {f["type"]: f for f in hard.get("facts", [])}

    def num(key: str) -> int | None:
        v = by_type.get(key, {}).get("splitValue")
        try:
            return int(v)
        except (TypeError, ValueError):
            return None

    floor = by_type.get("numberOfFloors", {})
    return {
        "rooms": num("numberOfRooms"),
        "bedrooms": num("numberOfBedrooms"),
        "surface": num("livingSpace"),
        "floor": floor.get("value"),
    }


def _compact(it: dict[str, Any]) -> Listing:
    hard = it.get("hardFacts", {})
    price = hard.get("price", {})
    addr = it.get("location", {}).get("address", {})
    tags = it.get("tags", {})
    flags = [name for name, on in (
        ("neuf", tags.get("isNew")),
        ("exclu", tags.get("isExclusive")),
        ("3D", tags.get("has3DVisit")),
        ("sans-honos", tags.get("hasBrokerageFee") is False),
    ) if on]
    return Listing(
        id=it.get("id", ""),
        price=price.get("value", "?"),
        price_sqm=(price.get("addition") or {}).get("value") or price.get("additionalInformation"),
        title=(it.get("mainDescription", {}) or {}).get("headline") or hard.get("title", ""),
        agency=(it.get("provider", {}) or {}).get("intermediaryCard", {}).get("title"),
        city=addr.get("city"), zip=addr.get("zipCode"), district=addr.get("district"),
        dpe=it.get("energyClass"),
        flags=flags,
        url=it.get("url", ""),
        **_facts(hard),
    )


def details(ids: list[str]) -> list[Listing]:
    """Fetch full detail for IDs (chunked) and reduce to compact records."""
    out: list[Listing] = []
    for i in range(0, len(ids), 30):
        chunk = ids[i:i + 30]
        for it in _get("/classifiedList/" + ",".join(chunk)):
            out.append(_compact(it))
    return out


def _fmt(lst: Listing) -> str:
    bits: list[str] = [lst["price"]]
    if lst["price_sqm"]:
        bits.append(f"({lst['price_sqm']})")
    rb = "/".join(str(x) for x in (lst["rooms"], lst["bedrooms"]) if x is not None)
    if rb:
        bits.append(f"{rb}P" if lst["bedrooms"] is None else f"{lst['rooms']}P·{lst['bedrooms']}ch")
    if lst["surface"]:
        bits.append(f"{lst['surface']}m²")
    if lst["floor"]:
        bits.append(lst["floor"])
    loc = " ".join(x for x in (lst["city"], lst["zip"], lst["district"]) if x)
    if loc:
        bits.append(loc)
    if lst["dpe"]:
        bits.append(f"DPE {lst['dpe']}")
    if lst["agency"]:
        bits.append(lst["agency"])
    if lst["flags"]:
        bits.append("[" + ",".join(lst["flags"]) + "]")
    return " · ".join(bits) + "\n  " + lst["url"]


def cmd_places(args: argparse.Namespace) -> None:
    hits = autocomplete(args.query, args.limit)
    if args.json:
        print(json.dumps(hits, ensure_ascii=False))
        return
    for h in hits:
        zips = f" zips={','.join(h['zips'])}" if h["zips"] else ""
        print(f"{h['id']:14} {TYPE_LABELS.get(h['type'], h['type']):10} {h['label']}{zips}")


def cmd_search(args: argparse.Namespace) -> None:
    criteria: dict[str, Any] = {
        "distributionTypes": ["Rent" if args.rent else "Buy"],
        "estateTypes": args.type,
        "projectTypes": args.projects,
        "location": {"placeIds": [resolve(w) for w in args.where]},
    }
    opt = {
        "numberOfRoomsMin": args.rooms_min, "numberOfRoomsMax": args.rooms_max,
        "numberOfBedroomsMin": args.bedrooms_min,
        "priceMin": args.price_min, "priceMax": args.price_max,
        "spaceMin": args.surface_min, "plotSpaceMin": args.land_min,
    }
    criteria.update({k: v for k, v in opt.items() if v is not None})

    total, ids = search_ids(criteria, args.limit, args.sort)
    listings = details(ids)
    if args.json:
        print(json.dumps({"total": total, "count": len(listings), "listings": listings},
                         ensure_ascii=False))
        return
    print(f"# {len(listings)}/{total} annonces")
    for i, lst in enumerate(listings, 1):
        print(f"[{i}] {_fmt(lst)}")


def main() -> None:
    p = argparse.ArgumentParser(description="Public SeLoger search (token-efficient).")
    sub = p.add_subparsers(dest="cmd", required=True)

    pl = sub.add_parser("places", help="Resolve a location name to placeId(s).")
    pl.add_argument("query")
    pl.add_argument("--limit", type=int, default=10)
    pl.add_argument("--json", action="store_true")
    pl.set_defaults(func=cmd_places)

    se = sub.add_parser("search", help="Search listings by location + criteria.")
    se.add_argument("--where", nargs="+", required=True,
                    help="One or more place names or placeIds (names auto-resolved).")
    se.add_argument("--rent", action="store_true", help="Rentals instead of sales.")
    se.add_argument("--type", nargs="+", default=["House", "Apartment"],
                    help="Estate types (House Apartment Parking Land Building Office Shop Loft).")
    se.add_argument("--projects", nargs="+",
                    default=["Life_Annuity", "New_Build", "Projected", "Resale"],
                    help="Project types; drop Life_Annuity to exclude viager.")
    se.add_argument("--price-min", type=int)
    se.add_argument("--price-max", type=int)
    se.add_argument("--rooms-min", type=int)
    se.add_argument("--rooms-max", type=int)
    se.add_argument("--bedrooms-min", type=int)
    se.add_argument("--surface-min", type=int, help="Min living space m².")
    se.add_argument("--land-min", type=int, help="Min plot/land m².")
    se.add_argument("--limit", type=int, default=30)
    se.add_argument("--sort", choices=["Default", "PriceAsc", "PriceDesc", "DateDesc"],
                    default="Default")
    se.add_argument("--json", action="store_true")
    se.set_defaults(func=cmd_search)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
