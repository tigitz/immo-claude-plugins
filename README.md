# immo-claude-plugins

Marketplace de plugins [Claude Code](https://code.claude.com/docs/en/plugins) pour les
professionnels de l'immobilier français.

Le plugin **`immo`** embarque des *skills* (savoir-faire) que Claude déclenche
automatiquement quand le contexte s'y prête. Les skills sont enrichis dans le temps :
une fois le plugin installé, un simple `/plugin update` récupère les dernières versions.

## Skills inclus

| Skill | À quoi il sert |
|-------|----------------|
| **vigilance-immo** | Constitue le dossier de vigilance **LCB-FT / TRACFIN** d'une transaction : collecte KYC, screening gratuit (sanctions, PPE, SCI, sources ouvertes) et production de la **Fiche d'évaluation des risques** officielle TRACFIN-DGCCRF (notation 1→4). Se déclenche sur « fais-moi le Tracfin du dossier », « vérifie cet acheteur », « fiche de vigilance »… |

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
      vigilance-immo/
        SKILL.md            ← le skill (instructions pour Claude)
        references/         ← docs de référence (obligations CMF, sources, fiche)
        assets/             ← gabarits (template de fiche d'évaluation)
```

Pour ajouter un skill : créer `plugins/immo/skills/<nom>/SKILL.md`, commit, push.
Les personnes qui ont installé le plugin le reçoivent au prochain `/plugin update`.
