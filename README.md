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

1. Installer jupyter : `sudo apt install jupyter`
1. Lancer le notebook : `jupyter notebook`
2. Installer les dépendances : `!pip install numpy matplotlib`
3. Exécuter les cellules 
