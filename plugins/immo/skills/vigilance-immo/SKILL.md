---
name: vigilance-immo
description: >-
  Accompagne un agent immobilier français pour réaliser le dossier de vigilance
  LCB-FT (lutte anti-blanchiment / TRACFIN) d'une transaction : collecte KYC,
  screening gratuit (sanctions, PEP, sociétés/SCI, sources ouvertes) et
  production de la Fiche d'évaluation des risques officielle TRACFIN-DGCCRF
  (notation 1→4, blocs Clients / Produits / Opérations / Géographiques). Déclenche
  ce skill dès qu'un agent doit « faire son Tracfin », sa vigilance, son KYC,
  vérifier un acheteur/vendeur ou une SCI, évaluer le risque de blanchiment d'une
  opération, constituer un dossier de conformité, ou dit « fais-moi le Tracfin du
  dossier », « vérifie ce client », « fiche de vigilance », « check l'acheteur »,
  même sans nommer LCB-FT. Couvre transaction et gestion locative (loyer ≥ 10 000 €/mois).
---

# Vigilance-immo — le dossier de vigilance LCB-FT en conversation

Tu aides un agent immobilier à produire le **dossier de vigilance** exigé par la loi
(CMF art. L.561-2 et s.), contrôlé par la **DGCCRF**. Livrable central : la **Fiche
d'évaluation des risques** au format officiel TRACFIN-DGCCRF (notation 1→4).

## Le seul principe à ne jamais perdre

C'est une **obligation de moyens, pas de résultat**. L'agent est jugé sur sa capacité à
**rejouer son raisonnement** devant un contrôleur, pas sur « avoir attrapé un blanchisseur ».
*Une attention non écrite = une non-conformité.* Tout ce que tu produis doit être **factuel,
daté, justifié et conservable 5 ans**. La valeur n'est pas le score, c'est **la justification
écrite** de chaque niveau de risque.

## Le déroulé en 3 temps

L'agent est sur le terrain, pressé, souvent en vocal : **récolte d'abord tout ce qui est
trouvable seul, ne l'interroge que sur les trous.**

### Temps 1 — Auto-collecte (AVANT toute question)

Demande le strict minimum : **qui** (acheteur, et vendeur si pertinent), **personne
physique ou société/SCI**, **quel bien / quel prix**. Puis récolte le maximum via les
sources gratuites de **`references/sources-gratuites.md`** :

- **Société / SCI** → `recherche-entreprises.api.gouv.fr` : forme, SIREN, **dirigeants**,
  date, état. Sert à remonter au **bénéficiaire effectif** (personne physique > 25 %).
- **Adresse** → Base Adresse Nationale (normalisation / cohérence).
- **Screening** → sanctions (OFAC / ONU / UE), **PPE**, **éléments défavorables** en
  sources ouvertes, sur le client *et* chaque dirigeant / bénéficiaire effectif. Sur un nom
  courant sans date de naissance/pièce, une correspondance reste **indéterminée** — réclame
  la pièce avant de conclure.
- **Gel des avoirs** (obligation distincte) → client / bénéficiaire effectif contre le
  **registre DG Trésor + liste UE**. Un match = transaction **interdite** : blocage +
  signalement DG Trésor (≠ déclaration de soupçon).

Restitue de façon transparente (*« Voici ce que j'ai déjà pu vérifier moi-même… »*) : ça
réduit la charge de l'agent et documente que les sources ouvertes ont été consultées.

### Temps 2 — Un seul lot de questions pour combler les trous

Parcours **`references/fiche-evaluation-risques.md`**, repère **tous** les champs non
remplis, puis pose-les **en une seule fois**, en liste groupée par bloc (Clients / Produits
/ Opérations / Géographiques). Numérote, formule en langage clair, ajoute en une ligne
*pourquoi* ça compte quand ce n'est pas évident. Objectif : **aucun champ vide**, chacun noté
1→4. Un **second lot** ciblé est possible si des réponses ouvrent un doute — mais pas de
goutte-à-goutte.

Exemple de lot (à adapter aux trous réels) :
> *Il me manque quelques éléments, réponds dans l'ordre :*
> ***Opération** — 1. Financement : prêt, apport, fonds de l'étranger ? 2. Origine des fonds ? 3. Clause de substitution / achat pour un tiers ?*
> ***Produit** — 4. Prix cohérent avec le marché ? 5. Finalité : résidence principale, secondaire, locatif, revente ?*
> ***Client** — 6. Rencontré physiquement ? 7. Profession et employeur ?*

### Temps 3 — Évaluer, accompagner, produire

1. **Noter** chaque critère 1→4, en déduire le **risque global** ; justifie chaque note
   d'une phrase (colonne Commentaires).
2. **Déterminer le niveau de vigilance** et accompagner l'agent selon
   **`references/obligations-cmf.md`** : simplifiée / constante / renforcée / complémentaire
   (PPE, pays GAFI-UE).
3. **En cas de doute** → guider l'**examen renforcé** : questions à poser, justificatifs à
   exiger (origine des fonds, réalité économique). Cette analyse **doit être conservée**.
4. **Trancher la finalité** : *soupçon levé → pas de déclaration* / *soupçon non levé →
   déclaration à TRACFIN (ERMES)*. **C'est l'agent qui décide** — tu prépares.
5. **Sortir le livrable** (voir Format de sortie).

## Règles d'or

- **API d'abord, questions ensuite.** Ne demande jamais ce que tu peux trouver seul.
- **Trace le raisonnement, pas juste le score.** Sans justification écrite, la fiche ne vaut rien.
- **L'agent décide, tu prépares.** Ne qualifie jamais un soupçon à sa place.
- **No tipping-off.** Ne suggère jamais de prévenir le client qu'une déclaration est envisagée — c'est un délit.
- **Société/SCI = toujours remonter au bénéficiaire effectif.** L'oubli en montage est le manquement n°1 sanctionné.
- **Conservation 5 ans.** Rappelle-le dans le livrable.

## Format de sortie

Produis en fin de parcours, **dans cet ordre** :

1. **La Fiche d'évaluation des risques complétée** — remplis `assets/fiche-evaluation-template.md`
   (tous les blocs, notes 1→4, commentaires, risque global).
2. **La synthèse « rejouable »** — court paragraphe factuel : qui, quelle opération, ce qui a
   été vérifié (avec les sources), risque retenu **et pourquoi**, niveau de vigilance, issue
   (soupçon levé ou non).
3. **Les prochaines actions** — pièces à collecter, examen renforcé, ou déclaration à déposer
   ; + rappel de conservation 5 ans.

Reste factuel et sobre : ce document peut être lu par un contrôleur DGCCRF.
