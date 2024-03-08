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
    printf("\nAffichage de la table\n");
    printf("Taille de la table = %d\n", t.size);
    printf("Somme minimale et maximale = %d\n", t.som_min_max);
    printf("Minimum = %d\n", t.array[t.index_min]);
    printf("Maximum = %d\n", t.array[t.index_max]);
    printf("Somme min i = %d\n", t.som_min_i);
    printf("Somme max i = %d\n", t.som_max_i);
    printf("Step = %d\n", t.step);
    for (int i = 0; i < t.size; i++) {
        printf("T[%d] = %d ", i, t.array[i]);
    }
    printf("\n");
}

bool recherche(Array t, int val) {
    int it = 0; //iterateur de parcours
    while (it < t.size && t.array[it] != val) {
        it++;
    }
    return it != t.size;
}

void calcul_som_min_max(Array *t) {
    if (t->step < t->size) {
        int num = t->array[t->step];
        t->som_min_i += num;
        t->som_max_i += num;

        if (num < t->array[t->index_min]) {
            t->index_min = t->step;
            t->som_min_max = t->som_max_i;
            t->som_min_i = num;
        }
        if (num > t->array[t->index_max]) {
            t->index_max = t->step;
            t->som_min_max = t->som_min_i;
            t->som_max_i = num;
        }
        t->step++;
    } else{
        printf("To many steps\n");
    }
}

int main() {
    Array array;
    array.size = 5;
    array.som_min_max = 0;
    array.som_min_i = 0;
    array.som_max_i = 0;
    array.step = 0;
    array.index_min = 0;
    array.index_max = 0;
    array.array = (int *) malloc(array.size * sizeof(int));

    insertion_aleatoire(array);
    display_t(array);
    for (int i = 0; i < array.size ; i++) {
        calcul_som_min_max(&array);
    }

    display_t(array);

    return 0;
}
