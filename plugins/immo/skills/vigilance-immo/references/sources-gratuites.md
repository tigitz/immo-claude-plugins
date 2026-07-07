# Sources gratuites de vérification (auto-collecte)

Toutes gratuites, sans abonnement. Utilise-les au **Temps 1** pour pré-remplir la
fiche avant d'interroger l'agent. Dans Claude Desktop, tu y accèdes par récupération
web (fetch) ou recherche web. **Documente toujours ce que tu as consulté et trouvé** :
c'est la preuve que les « sources ouvertes » ont été vérifiées (champ de la fiche).

## 1. Sociétés & SCI — `recherche-entreprises.api.gouv.fr` (sans clé)

Pour tout acheteur/vendeur **personne morale** (société, SCI). Renvoie identité légale
+ **dirigeants**.

```
GET https://recherche-entreprises.api.gouv.fr/search?q=<nom ou SIREN>&per_page=1
```

Champs utiles dans `results[0]` : `nom_complet`, `siren`, `nature_juridique`,
`date_creation`, `etat_administratif`, `siege.adresse`, `dirigeants[]`
(`nom`, `prenoms`, `qualite`, `annee_de_naissance`), `finances`.

→ Sert à : vérifier l'existence réelle de la structure, lister les dirigeants, et
**identifier qui interroger comme bénéficiaire effectif** (> 25 %).

## 2. Bénéficiaire effectif — registre INPI / RBE

Le registre des bénéficiaires effectifs (RBE) est accessible **aux assujettis LCB-FT**
(dont l'agent immobilier) via l'INPI, sur justification. `recherche-entreprises` donne
les **dirigeants** mais pas toujours la détention capitalistique : demande à l'agent
de récupérer/confirmer le **bénéficiaire effectif réel** (> 25 % du capital ou des
droits de vote), et applique-lui les critères « Clients » + le screening.

## 3. Adresse — Base Adresse Nationale (sans clé)

```
GET https://api-adresse.data.gouv.fr/search/?q=<adresse>&limit=1
```

→ Normalise l'adresse et signale une **adresse incohérente / introuvable** (critère
« éléments défavorables »).

## 4. Screening sanctions & PPE

Objectif : vérifier que le client (et chaque dirigeant / bénéficiaire effectif) n'est
**ni sous sanctions, ni PPE, ni cité défavorablement** en sources ouvertes.

**Approche pour Claude Desktop (gratuite, best-effort) :**
- **Recherche web ciblée** du nom + termes : `sanctions OFAC`, `sanctions UE`,
  `gel des avoirs`, `PPE / politically exposed`, + une recherche presse (adverse media).
- **Consultation des listes officielles** si besoin de confirmer :
  - **OpenSanctions** (agrège sanctions + PPE, 400+ sources) — `opensanctions.org` (recherche par nom).
  - **UE — liste consolidée** (inclut les gels français).
  - **OFAC / ONU** (sanctions US / internationales).

Note ce qui a été vérifié et le résultat, même négatif : *« Vérifié OFAC/UE/PPE/presse
le [date] : aucune correspondance »* — c'est une preuve de diligence, pas une formalité.

**Résultat → feu :** 🟢 rien / 🟠 correspondance à lever / 🔴 match avéré.

> ⚠️ **Homonymie — ne conclus pas 🟢 trop vite.** Sur un nom courant (ex. « Ivan Petrov »,
> équivalent d'un « Jean Dupont »), l'absence de match direct **ne vaut pas absence de
> risque** : des homonymes peuvent être sanctionnés. Sans **date de naissance + pièce
> d'identité (passeport)**, une correspondance reste **🟠 indéterminée** — tu ne peux
> pas la lever. Réclame la pièce d'identité **avant** de conclure le screening.

## 4bis. Gel des avoirs — obligation DISTINCTE et prioritaire

Ne confonds pas deux choses :
- Le **screening sanctions** ci-dessus nourrit l'évaluation du risque.
- Le **gel des avoirs** est une **obligation autonome** : tu dois vérifier le client
  (et le bénéficiaire effectif) contre le **registre national des gels (Direction
  générale du Trésor)** et la **liste consolidée UE**.

**Un match sur une liste de gel n'est PAS un simple 🔴 de risque** : la transaction est
**interdite**, doit être **bloquée immédiatement**, et **signalée sans délai à la DG
Trésor** — c'est une voie **différente** de la déclaration de soupçon TRACFIN (les deux
peuvent se cumuler). Vérification : `gels-avoirs.dgtresor.gouv.fr` + liste UE.

## 5. Pays à risque — listes GAFI / UE

Pour les critères « géographiques » : vérifie si le pays de résidence du client, la
nationalité, ou la **provenance des fonds** relève d'une liste **GAFI** (grise/noire)
ou UE à haut risque. Recherche web : `pays liste GAFI` / `liste UE pays tiers à haut risque`.

> ⚠️ **Ces listes bougent souvent — vérifie la date.** Un pays peut sortir (ex. les
> Émirats, retirés en 2024-2025) ou entrer. Fie-toi à la **liste à jour**, pas à une
> réputation. Et distingue deux choses : **« hors liste »** (plus d'obligation
> automatique de vigilance renforcée pays) **≠ « risque réel faible »** — un pays hors
> liste peut rester un facteur d'attention selon le dossier (à noter en commentaire).

---

## Évolution possible (hors runtime Claude Desktop)

Pour un screening industriel et confidentiel (données clients qui ne sortent pas),
**auto-héberger OpenSanctions** (moteur `yente`, Docker) expose une API `/match`
gratuite qui agrège PEP + toutes les sanctions. Non requis ici, mais c'est la brique
à brancher si l'outil passe en version dédiée.
