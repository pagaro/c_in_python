import os
from ctypes import CDLL, Structure, c_int, POINTER, byref

k = 5  # Taille du tableau

class Array(Structure):
    _fields_ = [("array", POINTER(c_int)),
                ("som_min_max", c_int),
                ("min", c_int),
                ("max", c_int),
                ("size", c_int)]

# Chargez la bibliothèque partagée
if os.name == 'nt':  # Windows
    lib_path = './cmake-build-debug/libCalculSomMinMaxLib.dll'
else:
    lib_path = './cmake-build-debug/libCalculSomMinMaxLib.so'  # Unix-like

lib = CDLL(lib_path)

# Créer une instance de la structure Array
arr = Array((c_int * k)(), 0, -1, -1,k)


# Utiliser les fonctions
lib.insertion_aleatoire(byref(arr))
lib.display_t(arr)
lib.calcul_som_min_max(byref(arr))
lib.display_t(arr)
