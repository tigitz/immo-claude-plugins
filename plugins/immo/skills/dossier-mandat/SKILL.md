---
name: dossier-mandat
description: >-
  Prend en charge la phase administrative une fois le vendeur d'accord : rédige le projet
  de mandat, sort la checklist de validation (siège), produit les jeux de champs prêts à
  saisir dans le CRM de l'agence ET dans Modelo (fini la triple-saisie), et enchaîne sur la
  fiche de vigilance TRACFIN. Déclenche ce skill dès que l'agent dit « rentrer le mandat »,
  « faire le mandat », « la partie administrative », « prépare le mandat », « saisir le
  bien », « le dossier est validé, on avance ».
---

# Dossier mandat — la paperasse, une seule fois

Une fois les infos consolidées (via `estimation-vendeur` / le CRM), l'agent doit produire
le mandat et le saisir partout. Ton job : **rédiger, préparer la validation, et générer une
seule saisie réutilisée dans tous les outils** — puis déclencher le Tracfin.

## Déroulé

### 1. Assembler
Reprends les infos du **CRM** (fiche vendeur + bien) et de l'estimation. Repère les champs
manquants pour un mandat complet et réclame-les **en un seul lot**.

### 2. Rédiger le projet de mandat
Produis le **projet de mandat** (type, durée, prix, honoraires, clauses) au format de
l'agence + une **checklist de validation siège** (ce qui doit être relu / signé avant).

### 3. Une saisie, tous les outils
Génère les **jeux de champs structurés** à coller sans ressaisie dans :
- le **CRM de l'agence** (fiche bien / mandat),
- **Modelo** (acte / mandat).
Même source, formats adaptés à chaque outil.

### 4. Enchaîner sur la vigilance
Déclenche / rappelle le skill **`vigilance-immo`** pour produire la **fiche de vigilance
LCB-FT (Tracfin)** du client — obligatoire, à chaque transaction.

## Format de sortie
1. **Projet de mandat** + checklist de validation.
2. **Champs CRM** et **champs Modelo** — prêts à coller.
3. **Renvoi vigilance** — lancement de `vigilance-immo`.

## Ligne rouge
Le mandat engage l'agence : **relecture et validation humaines** obligatoires. La fiche de
vigilance est un **acte légal** — l'agent décide, Claude prépare.
