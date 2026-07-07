---
name: revue-du-matin
description: >-
  Routine du matin d'un agent immobilier : consolide toutes les nouveautés de la
  veille (mails, WhatsApp, Slack, et le CRM), les relie aux dossiers existants, puis
  produit trois livrables — un brouillon des saisies à faire dans le CRM, une to-do
  priorisée orientée signature, et pour chaque tâche une action clé en main que Claude
  peut exécuter ou préparer. Déclenche ce skill dès que l'agent dit « ma revue du
  matin », « prépare ma journée », « quoi de neuf depuis hier », « qu'est-ce que j'ai
  raté », « mes to-dos du jour », « brief du matin », « fais le point sur mes dossiers ».
---

# Revue du matin — repartir avec une journée priorisée

L'agent arrive débordé, l'info est éparpillée (mail, WhatsApp, Slack, CRM). Ton job :
**tout consolider, tout rattacher au CRM (la source de vérité), et sortir une journée
priorisée avec des actions déjà préparées.** L'agent valide, tu exécutes.

## Déroulé

### 1. Collecter les nouveautés depuis hier
Balaie chaque canal disponible : **Gmail** (connecteur), **Slack**, **WhatsApp**
(screenshots collés, ou MCP si branché), et le **CRM** (nouvelles entrées, changements
de statut, messages entrants). Ne remonte que ce qui est **nouveau depuis la dernière revue**.

### 2. Consolider et rattacher
Dédoublonne, puis relie **chaque information à un contact / un bien / un dossier** du CRM.
Signale ce qui ne correspond à aucun dossier connu (= à créer).

### 3. Brouillon de saisie CRM
Pour chaque info, propose l'**entrée à créer ou à mettre à jour** (contact, bien, statut,
note d'activité) — en **draft**, jamais écrit sans validation. L'objectif : que le CRM
reflète fidèlement la réalité en fin de revue.

### 4. To-do priorisée
Construis / complète / actualise la liste de tâches. **Priorise par proximité d'une
signature** : offres en cours > compromis à suivre > visites à caler > relances chaudes >
prospection. **Ne lâche jamais** les urgences et les actions restées ouvertes de la veille —
remonte-les en tête.

### 5. Actions clés en main
Pour chaque tâche, propose ce que **Claude peut faire tout de suite** (rédiger le message,
préparer le mail, proposer un créneau, pré-remplir une fiche) ou comment il accompagne.

## Format de sortie
1. **Ce qui est arrivé** — consolidé par dossier, avec la source.
2. **Saisies CRM proposées** — liste de drafts create/update, prêts à valider.
3. **Votre journée** — to-do priorisée ; pour chaque ligne : l'action Claude proposée.

## Ligne rouge
Tout draft de saisie CRM et tout message **attend la validation de l'agent** avant écriture
ou envoi. Tu prépares et proposes — l'agent tranche.
