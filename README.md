# Projet Array Operations

Ce projet implémente des opérations sur des tableaux en C, avec une interface Python pour visualiser les opérations étape par étape.

## Compilation des librairies

Pour compiler le projet, utilisez les commandes suivantes :

1. Créer un répertoire de build : `mkdir cmake-build-debug && cd cmake-build-debug`
2. Générer les fichiers de build avec CMake : `cmake ..`
3. Compiler le projet : `cmake --build .`

Cela générera une bibliothèque partagée (`libarray_ops.so` ou `libarray_ops.dll`) et un exécutable (`ArrayOperationsApp`).

## Lancement jupyter notebook et instalation des dépendances

Pour lancer le notebook, utilisez les commandes suivantes :

1. Creer un environnement virtuel : `python3 -m venv venv`
2. Activer l'environnement virtuel : `source venv/bin/activate`
3. Installer les dépendances : `pip install -r requirements.txt`
4. Lancer le notebook : `jupyter notebook`
5. Ouvrir ce fichier : `c_and_python.ipynb`
