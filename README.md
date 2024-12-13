# Travaux pratiques sur le "scraping" et les expressions régulières: JudiLibre

Vous venez d'être recruté par la jeune startup [Docteur Justice](https://fr.wikipedia.org/wiki/Docteur_Justice) qui souhaite créer un LLM afin de réaliser des analyses juridiques.
Pour cela, cette startup a besoin d'un fond documentaire incluant les données de jurisprudence des cours de droit privé (tribunaux judiciaires, cours d'appel et cour de cassation).
Votre première mission est de créer un système permettant de récupérer toutes les décisions de la cour de cassation qui sont disponibles sur le site [judilibre](https://www.courdecassation.fr/acces-rapide-judilibre) de la cour de cassation.

### Exercice 1: vérification des CGU du site

Avant de vous lancer dans toute tâche de moissonnage ([_scraping_](https://fr.wikipedia.org/wiki/Web_scraping)), il faut vérifier les CGU du site ciblé afin de vérifier si: 1) vous avez le droit d'effectuer cette opération sur le site et 2) quelles limitations éventuelles s'appliquent à l'utilisation des données ainsi récupérées.

Vérifiez sur le site [judilibre](https://www.courdecassation.fr/acces-rapide-judilibre) si vous avez le droit de faire cette opération.
Justifiez votre réponse.

#### Réponse

TODO

### Exercice 2: proposition de stratégie de récupération du stock

Votre startup souhaite récupérer toutes les données (format HTML) de la cour de cassation du site JudiLibre (stock) et de manière quotidienne toutes les modifications (flux), contenant les nouveaux documents et les documents modifiés.

Proposez une stratégie pour implémenter un robot de récupération, et donnez une estimation du temps nécessaire pour récupérer tout le stock avec diverses stratégies.

#### Réponse

TODO

### Exercice 3: extraction de données structurées

Grâce à des expressions régulières, modifiez la méthode `from_html` pour ajouter l'extraction des différents éléments.

Utilisez `unittest` tel que ci-dessous pour mesurer l'avancée de votre travail:

```bash
python -m unittest tp_regexps.test_regexps
```

#### Réponse

TODO
