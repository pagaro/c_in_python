#include "IntTable.h"

void insertion_aleatoire(Array t) {
// insertion aléatoire
    srand((unsigned int) time(NULL)); //initialise le générateur avec temps courant.
    for (unsigned int i = 0; i < t.size; i++) {
        t.array[i] = rand() % 101; // retourne un entier compris entre 0 et 100
        // La valeur retournée par rand() est comprise entre 0 et RAND_MAX;
        // le standard C ISO garantit que #define RAND_MAX sera au moins supérieure ou égale à 32767
    }
}

void display_t(Array t) {
    printf("Affichage de la table\n");
    printf("Taille de la table = %d\n", t.size);
    printf("Somme minimale et maximale = %d\n", t.som_min_max);
    printf("Minimum = %d\n", t.min);
    printf("Maximum = %d\n", t.max);
    for (int i = 0; i < t.size; i++) {
        printf("T[%d] = %d ", i, t.array[i]);
    }
}

bool recherche(Array t, int val) {
    int it = 0; //iterateur de parcours
    while (it < t.size && t.array[it] != val) {
        it++;
    }
    return it != t.size;
}

void calcul_som_min_max(Array *t) {
    int som_min_i = 0;
    int som_max_i = 0;
    for (int i = 0; i < t->size; i++) {
        int num = t->array[i];
        som_min_i += num;
        som_max_i += num;
        if (num < t->min) {
            t->min = num;
            t->som_min_max = som_max_i;
            som_min_i = num;
        }
        if (num > t->max) {
            t->max = num;
            t->som_min_max = som_min_i;
            som_max_i = num;
        }
    }
}

int main() {
    Array array;
    array.size = 10;
    array.som_min_max = 0;
    array.min = INT_MAX;
    array.max = INT_MIN;
    array.array = (int *) malloc(array.size * sizeof(int));

    insertion_aleatoire(array);
    display_t(array);

    calcul_som_min_max(&array);
    display_t(array);

    return 0;
}
