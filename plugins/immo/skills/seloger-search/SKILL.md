---
name: seloger-search
description: >-
  Interroge la recherche publique de biens SeLoger (seloger.com) en ligne de
  commande, sans compte ni clé API : résout un nom de lieu en placeId, lance une
  recherche par critères (achat/location, type de bien, prix, pièces, surface,
  secteur) et renvoie un digest compact des annonces (prix, €/m², pièces,
  surface, ville, DPE, agence, lien). Déclenche ce skill dès qu'on veut chercher,
  sonder ou comparer des biens sur SeLoger, estimer un marché local, sortir une
  liste d'annonces pour un secteur, ou dit « cherche des appart sur SeLoger »,
  « qu'est-ce qui se vend à Nice », « les biens à moins de X€ à Cannes »,
  « combien d'annonces sur ce quartier », « trouve-moi des maisons à vendre »,
  même sans nommer SeLoger explicitement dès qu'il s'agit d'annonces immobilières
  françaises en ligne. Couvre achat et location.
---

# seloger-search — recherche publique SeLoger en CLI

Expose les trois endpoints publics de `seloger.com` via un seul script Python.
Aucun d'eux n'exige de cookie d'authentification ; le seul verrou est **DataDome**
(anti-bot), franchi par `curl_cffi` qui imite l'empreinte TLS d'un vrai Chrome.

Le flux réel du site se fait en trois temps — le script les enchaîne :

1. `POST /search-mfe-bff/autocomplete` — nom de lieu → `placeId`
2. `POST /serp-bff/search` — critères + placeId → **liste d'IDs** + `totalCount`
3. `GET /classifiedList/{id,id,…}` — IDs → détail complet (~9 KB/annonce)

L'étape 3 est volumineuse : le script en extrait **uniquement les champs utiles**
et rend une ligne par annonce. C'est le cœur du « token efficient » — ne jamais
renvoyer le JSON brut du détail dans le contexte.

## Prérequis

`curl_cffi` doit être installé. Si le script s'arrête sur `Missing dependency` :

```bash
pip install curl_cffi
```

## Utilisation

Le script est dans `scripts/seloger.py`. Deux sous-commandes.

### 1. Résoudre un lieu (`places`)

Les `placeId` sont opaques (`AD08FR2038` = Nice). Cette commande les retrouve à
partir d'un nom. Utile quand un nom est ambigu (plusieurs « Cannes ») ou pour
cibler un quartier / code postal précis.

```bash
python3 scripts/seloger.py places "cannes"
```

Sortie : `placeId  type  libellé  zips`. Taxonomie des types :

| type   | signification |
|--------|---------------|
| `AD08` | ville         |
| `POCO` | code postal   |
| `NBH1/2/3` | quartier  |
| `AD04` | département    |
| `AD06` | commune / arrondissement |
| `AD02` | pays          |

### 2. Chercher des annonces (`search`)

`--where` accepte des **noms** (résolus automatiquement au meilleur match, la
correspondance choisie est affichée sur stderr) **ou des `placeId`** directement.
Plusieurs lieux possibles.

```bash
# Appartements à vendre à Nice, ≤ 250 000 €, ≥ 2 pièces, du moins cher au plus cher
python3 scripts/seloger.py search --where nice --type Apartment \
  --price-max 250000 --rooms-min 2 --sort PriceAsc --limit 10

# Deux quartiers précis, par placeId
python3 scripts/seloger.py search --where NBH2FR9829 POCOFR249 --limit 20

# Locations de maisons à Cannes
python3 scripts/seloger.py search --where cannes --rent --type House
```

Options clés :

- `--rent` : locations au lieu de ventes (défaut : achat).
- `--type` : `House Apartment Parking Land Building Office Shop Loft` (défaut : House Apartment).
- `--price-min/--price-max`, `--rooms-min/--rooms-max`, `--bedrooms-min`,
  `--surface-min` (habitable m²), `--land-min` (terrain m²).
- `--sort` : `Default` | `PriceAsc` | `PriceDesc` | `DateDesc`.
- `--limit` : nombre d'annonces (défaut 30 ; pagine automatiquement).
- `--projects` : par défaut inclut le **viager** (`Life_Annuity`). En tri
  `PriceAsc` les viagers (« Bouquet 30 000 € + 3 000 €/mois ») remontent en tête.
  Pour de la vente classique uniquement : `--projects Resale New_Build Projected`.
- `--json` : sortie structurée compacte (`{total, count, listings[]}`) pour
  chaîner ou filtrer. Sans ce flag, sortie texte (plus légère en tokens).

## Lecture de la sortie texte

```
# 4/1030 annonces
[1] 95 000 € · (2 714 €/m²) · 2P·1ch · 35m² · RDC · Nice 06000 Roquebillière · DPE C · Le coin du LMNP · [exclu,sans-honos]
  https://www.seloger.com/228591943/detail.htm
```

`totalCount` (ici 1030) est le total réel côté SeLoger ; le premier chiffre est
le nombre rapatrié (`--limit`). Flags : `neuf`, `exclu`, `3D`, `sans-honos`.

## Notes

- Le script échoue vite (message + code HTTP) si un endpoint renvoie autre chose
  que 200 — typiquement un durcissement DataDome. Réessayer suffit le plus souvent.
- Pour du volume (comparaison de marché sur plusieurs secteurs), préférer
  plusieurs `--where` dans un seul appel plutôt que d'itérer.
