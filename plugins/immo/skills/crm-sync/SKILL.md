---
name: crm-sync
description: >-
  Tient le CRM comme source de vérité de toute l'activité : transforme le flux entrant de la
  journée (mails, messages, notes, appels) en mises à jour de statut propres et actualisées
  par dossier, puis repère les dossiers dormants et propose les relances. C'est la base sur
  laquelle tous les autres skills s'appuient. Déclenche ce skill dès que l'agent dit « mets à
  jour le CRM », « actualise mes dossiers », « où j'en suis », « fais le ménage dans mes
  contacts », « qui je dois relancer », « entretiens ma base », « statut de mes affaires ».
---

# CRM sync — la source de vérité, tenue à jour

Sans CRM propre, l'IA travaille dans le vide. Ton job : **capitaliser tout le flux entrant
dans le CRM avec le bon statut**, pour qu'il reflète en permanence la réalité — et animer la
relance à partir de là.

## Le principe
Le **CRM est la source de vérité** de toute l'activité de l'agent : chaque contact, chaque
bien, chaque dossier, avec **son statut** (prospect / actif / offre / compromis / signé /
perdu / à relancer). C'est la base sur laquelle s'appuient `revue-du-matin`, `rapprochement`,
`negociation-closing`… Sa tenue conditionne tout le reste.

## Déroulé

### 1. Capter le flux entrant
Rassemble ce qui est arrivé (mails, WhatsApp, Slack, notes d'appel, comptes rendus de visite)
et **rattache chaque élément à son dossier**.

### 2. Actualiser les statuts
Propose, par dossier, la **mise à jour de statut et la note d'activité** correspondantes —
en draft. Objectif : plus aucun dossier « figé » qui ne reflète pas la dernière interaction.

### 3. Animer la relance
Repère les dossiers **dormants** (pas de contact depuis X, statut « à relancer », conditions
qui approchent) et propose des **relances prêtes** — l'agent garde la personnalisation et
l'envoi.

## Format de sortie
1. **Mises à jour CRM** — par dossier : nouveau statut + note (draft).
2. **Dossiers dormants** — à relancer, triés par urgence / proximité de signature.
3. **Relances proposées** — messages prêts à personnaliser et envoyer.

## Ligne rouge
Toute mise à jour et tout envoi **attendent la validation de l'agent**. La relance reste
**personnelle** : Claude rappelle et prépare, l'agent garde le lien.
