# immo-claude-plugins

Marketplace de plugins [Claude Code](https://code.claude.com/docs/en/plugins) pour les
professionnels de l'immobilier français.

Le plugin **`immo`** embarque des *skills* (savoir-faire) que Claude déclenche
automatiquement quand le contexte s'y prête. Les skills sont enrichis dans le temps :
une fois le plugin installé, un simple `/plugin update` récupère les dernières versions.

## Skills inclus

Les skills suivent le **cycle d'activité** de l'agent immobilier, une compétence par étape.
Fil rouge : le **CRM est la source de vérité**, et l'agent valide toujours avant écriture / envoi.

| Skill | Étape | À quoi il sert |
|-------|-------|----------------|
| **revue-du-matin** | 1 · Capter & trier | Consolide les nouveautés de la veille (mails, WhatsApp, Slack, CRM), propose les saisies CRM et une **to-do priorisée orientée signature** + les actions clés en main. |
| **estimation-vendeur** | 2 · Estimer | Vocal + documents → estimation argumentée par comparables, synchro fiche vendeur/bien dans le CRM, et **pitch ADN Kretz** pour décrocher le mandat. |
| **dossier-mandat** | 3 · Rentrer le mandat | Rédige le mandat, checklist de validation, jeux de champs **CRM + Modelo** (fini la triple-saisie), et enchaîne sur `vigilance-immo`. |
| **annonce-diffusion** | 4 · Mettre en marché | Annonce à la marque Kretz (≈2000 car SEO, FR/EN, avec/sans logo), traitement des photos, affiche via le CRM, paquets de diffusion par plateforme. |
| **qualification-acquereur** | 5 · Qualifier | Challenge l'agent pour capter tous les critères, crée la fiche acquéreur, lance la recherche (base interne + veille). |
| **rapprochement** | 6 · Rapprocher & visiter | Le **cerveau matching** : croise une recherche avec la base, classe le Top N, prépare mises en relation + créneaux de visite. |
| **vigilance-immo** | 7 · Vigilance | Dossier **LCB-FT / TRACFIN** : KYC, screening gratuit (sanctions, PPE, SCI), **Fiche d'évaluation des risques** officielle TRACFIN-DGCCRF (1→4). |
| **negociation-closing** | 8 · Négocier & closer | Coache la négociation, pré-remplit le **compromis Modelo**, fait l'entremetteur (messages + créneaux), suit les conditions suspensives. |
| **crm-sync** | 9 · Entretenir & réactiver | Capitalise le flux entrant dans le **CRM (source de vérité)** avec les bons statuts, repère les dossiers dormants et propose les relances. |
| **seloger-search** | veille *(en construction)* | Recherche publique de biens SeLoger en CLI (sans compte) : critères → digest d'annonces (prix, €/m², DPE, agence, lien). |

## Installation (à faire une fois)

Dans Claude Code, tape ces deux commandes :

```
/plugin marketplace add tigitz/immo-claude-plugins
/plugin install immo@immo-plugins
```

Le repo est public : aucun token ni authentification n'est nécessaire pour l'ajouter.

C'est tout. Les skills se déclenchent ensuite tout seuls selon ce que tu demandes à Claude.

## Recevoir les mises à jour

Les skills évoluent. Pour récupérer les dernières versions :

```
/plugin marketplace update
/plugin update immo@immo-plugins
```

> Le plugin n'a pas de numéro de version figé : chaque nouveau commit sur ce repo
> devient automatiquement la version courante. Un `/plugin update` suffit donc toujours
> à être à jour.

## Structure du repo

```
.claude-plugin/
  marketplace.json          ← catalogue de la marketplace
plugins/
  immo/
    .claude-plugin/
      plugin.json           ← manifeste du plugin
    skills/
      revue-du-matin/         SKILL.md
      estimation-vendeur/     SKILL.md
      dossier-mandat/         SKILL.md
      annonce-diffusion/      SKILL.md
      qualification-acquereur/ SKILL.md
      rapprochement/          SKILL.md
      vigilance-immo/         SKILL.md + references/ + assets/
      negociation-closing/    SKILL.md
      crm-sync/               SKILL.md
      seloger-search/         SKILL.md + scripts/   (en construction)
```

Pour ajouter un skill : créer `plugins/immo/skills/<nom>/SKILL.md`, commit, push.
Les personnes qui ont installé le plugin le reçoivent au prochain `/plugin update`.
