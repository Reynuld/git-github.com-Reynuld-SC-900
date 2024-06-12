# Simulation d'examen SC-900

Cette application en PyQt6 permet de simuler un examen pour le SC-900 avec des questions à choix multiple et vrai/faux. Elle inclut deux modes : la simulation d'examen standard et un mode hardcore.

## Fonctionnalités

- **Simulation d'examen** : Sélectionne aléatoirement 40 questions pour simuler un examen.
- **Mode hardcore** : Permet de parcourir toutes les questions pour un entraînement intensif.
- **Gestion des réponses** : Permet de répondre à des questions à choix multiple et vrai/faux.
- **Affichage des résultats** : Affiche le score à la fin de l'examen.

## Prérequis

- Python 3.6 ou plus récent
- PyQt6

## Installation

1. **Clonez ce dépôt :**
   ```sh
   git clone https://github.com/Reynuld/simulation-sc900.git
   ```
2. **Accédez au répertoire :**
   ```sh
   cd SC-900
   ```
3. **Installez les dépendances :**
   ```sh
   pip install -r requirements.txt
   ```

## Fichier de questions

Les questions doivent être définies dans un fichier JSON. Voici un exemple de structure de fichier JSON pour les questions (`SC-900-Questions.txt`):

```json
[
    {
        "texte": "Quelle est la couleur du ciel ?",
        "type": "choix_multiple",
        "options": ["Bleu", "Vert", "Rouge"],
        "reponse_correcte": ["Bleu"]
    },
    {
        "texte": "La terre est-elle ronde ?",
        "type": "vrai_faux",
        "reponse_correcte": 1
    }
]
```

- **texte** : Le texte de la question.
- **type** : Le type de question, soit `choix_multiple` pour les questions à choix multiples, soit `vrai_faux` pour les questions vrai/faux.
- **options** : Une liste des options pour les questions à choix multiples.
- **reponse_correcte** : La réponse correcte. Pour les questions à choix multiples, c'est une liste d'options correctes. Pour les questions vrai/faux, c'est `1` pour "Oui" et `2` pour "Non".

## Utilisation

1. **Lancez l'application :**
   ```sh
   python app.py
   ```
2. **Cliquez sur le bouton "Simulation d'examen"** pour commencer une simulation aléatoire de 40 questions.
3. **Cliquez sur le bouton "Hardcore mode"** pour parcourir toutes les questions.
4. **Répondez aux questions** affichées.
5. **Cliquez sur "Suivant"** pour passer à la question suivante.
6. **À la fin**, un message s'affichera avec votre score.

## Architecture du code

- **`SC-900.py`** : Le fichier principal qui contient la logique de l'application.
- **`SC-900-Questions.txt`** : Le fichier JSON contenant les questions.
- **`README.md`** : Ce fichier de documentation.

## Contribution

Les contributions sont les bienvenues ! Pour apporter une contribution :

1. **Forkez ce dépôt.**
2. **Créez une branche** pour votre fonctionnalité (`git checkout -b feature-nomDeLaFonctionnalité`).
3. **Apportez vos modifications** et **committez** (`git commit -am 'Ajouter une fonctionnalité'`).
4. **Poussez vers la branche** (`git push origin feature-nomDeLaFonctionnalité`).
5. **Créez une Pull Request**.


