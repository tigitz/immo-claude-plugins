---
name: qualification-acquereur
description: >-
  Traite une demande d'acquisition : challenge l'agent pour capter toutes les informations
  nécessaires (budget, secteur, typologie, financement, délai, motivation), crée la fiche
  acquéreur dans le CRM, puis lance la recherche de biens correspondants (base interne + veille
  des sources / portails). Objectif : une réactivité maximale sur chaque lead entrant.
  Déclenche ce skill dès que l'agent dit « une demande acquéreur », « un client cherche »,
  « qualifie cette demande », « nouveau lead », « il cherche un bien », « prends ce contact ».
---

# Qualification acquéreur — capter le besoin, répondre vite

Un lead acquéreur mal qualifié, c'est du temps perdu et une réactivité en berne. Ton job :
**challenger l'agent pour tout capter, ranger dans le CRM, et lancer la recherche.**

## Déroulé

### 1. Challenger la demande
Passe en revue les **critères indispensables** et **pose ce qui manque, en un lot** :
budget (et financement : prêt / apport / fonds), **secteur**, typologie (surface, pièces,
extérieur, vue), **délai**, motivation (résidence / investissement), non-négociables.
Ne laisse pas de trou : sans budget ni financement, pas de matching sérieux.

### 2. Fiche acquéreur (CRM)
Produis le **draft de fiche acquéreur** à créer dans le CRM (source de vérité) avec les
critères pondérés. L'agent valide.

### 3. Rechercher
Croise d'abord la **base interne** (biens de l'agence / du réseau). Puis élargis à la
**veille** des sources externes. *(Skill `se-loger` en construction pour les portails —
à brancher ici quand prêt.)*

## Format de sortie
1. **Questions de qualification** — le lot à combler.
2. **Fiche acquéreur** — draft CRM, critères pondérés.
3. **Premiers biens** — correspondances internes + pistes de veille.

## Ligne rouge
La recherche sur des sources externes respecte les CGU des portails (pas de scraping
sauvage). L'agent valide la fiche et les premières mises en relation.
