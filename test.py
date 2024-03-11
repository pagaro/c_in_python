import os
from ctypes import CDLL, Structure, c_int, POINTER, byref
import matplotlib.pyplot as plt
from ipywidgets import interact, IntSlider

k = 5  # Taille du tableau

class Array(Structure):
    _fields_ = [("array", POINTER(c_int)),
                ("som_min_max", c_int),
                ("som_min_i", c_int),
                ("som_max_i", c_int),
                ("min", c_int),
                ("max", c_int),
                ("size", c_int),
                ("step", c_int)]

# Chargez la bibliothèque partagée
if os.name == 'nt':  # Windows
    lib_path = './cmake-build-debug/libCalculSomMinMaxLib.dll'
else:
    lib_path = './cmake-build-debug/libCalculSomMinMaxLib.so'  # Unix-like

lib = CDLL(lib_path)

# Créer une instance de la structure Array
arr = Array((c_int * k)(), 0,0,0, 101, -1,k,0)


# Fonction pour afficher l'état actuel basé sur 'step'
def plot_step(step):
    arr.step = step
    lib.calcul_som_min_max(byref(arr))  # Supposons que cela met à jour 'arr' pour la 'step' spécifiée

    # Créer le graphique
    plt.figure(figsize=(10, 5))
    plt.bar(range(arr.size), arr.array[:arr.size], color='blue')
    plt.xlabel('Index')
    plt.ylabel('Valeur')
    plt.title('État Actuel du Tableau')
    plt.show()

# Utiliser interact pour visualiser chaque étape
interact(plot_step, step=IntSlider(min=0, max=arr.size-1, step=1, value=0))


