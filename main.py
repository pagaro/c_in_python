import os
from ctypes import CDLL, Structure, c_int, POINTER, byref
import matplotlib.pyplot as plt
from ipywidgets import interact, IntSlider

k = 50  # Taille du tableau


class Array(Structure):
    _fields_ = [("array", POINTER(c_int)),
                ("som_min_max", c_int),
                ("som_min_i", c_int),
                ("som_max_i", c_int),
                ("index_min", c_int),
                ("index_max", c_int),
                ("size", c_int),
                ("step", c_int)]
    _pack_ = 1


# Chargez la bibliothèque partagée
print(os.name)

# Recherche du chemin complet de la bibliothèque
if os.name == 'nt':  # Windows
    lib_path = './cmake-build-debug/libCalculSomMinMaxLib.dll'
else:
    lib_path = './cmake-build-debug/libCalculSomMinMaxLib.so'  # Unix-like

print('koko')
lib = CDLL(lib_path)

# Créer une instance de la structure Array
arr = Array((c_int * k)(), 0, 0, 0, 0, 0, k, 0)


lib.insertion_aleatoire(arr)

print('titi')

def plot_step(step):
    frame = frames[step]
    arr, current_idx, highlighted_min_max, som_min_max, somme_min_i, somme_max_i = frame

    plt.figure(figsize=(10, 6))
    bars = plt.bar(range(len(arr)), arr, color='lightblue')
    for i, bar in enumerate(bars):
        if i == current_idx:
            bar.set_color('yellow')
        elif i in highlighted_min_max:
            bar.set_color('red')
        elif highlighted_min_max[0] < i < highlighted_min_max[1] or highlighted_min_max[0] > i > highlighted_min_max[1]:
            bar.set_color('green')
        else:
            bar.set_color('lightblue')

    plt.title(f"Étape {current_idx + 1}")
    plt.xlabel("Index")
    plt.ylabel("Valeur")
    plt.text(0.01, 0.95, f"Somme min-max: {som_min_max}", transform=plt.gca().transAxes)
    plt.text(0.01, 0.90,
             f"Index min {highlighted_min_max[0]}, Min: {arr[highlighted_min_max[0]]}, Somme min i: {somme_min_i}",
             transform=plt.gca().transAxes)
    plt.text(0.01, 0.85,
             f"Index max {highlighted_min_max[1]}, Max: {arr[highlighted_min_max[1]]}, Somme max i: {somme_max_i}",
             transform=plt.gca().transAxes)
    plt.show()


frames = []
array_size = arr.size

for step in range(k):
    lib.calcul_som_min_max(byref(arr))

    array = []
    for index in range(array_size):
        array.append(arr.array[index])
    frames.append((array, arr.step - 1, [arr.index_min, arr.index_max], arr.som_min_max, arr.som_min_i, arr.som_max_i))

# # Utiliser interact pour visualiser chaque étape
interact(plot_step, step=IntSlider(min=0, max=arr.size - 1, step=0, value=0))
print("toto", os.path.exists(lib_path))

