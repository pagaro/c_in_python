/* En-tete de liste
   ----------------
   objectif : définir le TAA HashTable : gestion des collisions par hachage*/

#ifndef _int_t_h
#define _int_t_h

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

typedef struct {
    int *array;
    int som_min_max;
    int som_min_i;
    int som_max_i;
    int index_min;
    int index_max;
    int size;
    int step;
} Array;

void fill(Array * pt);

// affichage de la table
void display_t(Array t);


//insertion aléatoire de clefs
void insertion_aleatoire(Array t);

// recherche d'une clé dans la table
bool recherche(Array t, int val);

// recherche de la somme minimale et maximale
void calcul_som_min_max(Array *t);

void sort_paired_unpaired(Array *t);

// liberation de la mémoire
//void libérer_t(Int_Array *liste);
#endif
