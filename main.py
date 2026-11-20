import random
import sys


def lire_grille_stdin():
    lignes = [l.split() for l in sys.stdin.read().splitlines() if l.strip()]
    if not lignes:
        raise ValueError("grille vide")
    if len(lignes[0]) != 1 or not lignes[0][0].isdigit():
        raise ValueError("la première ligne doit contenir la taille de la grille")
    taille = int(lignes[0][0])
    if taille <= 0:
        raise ValueError("la taille doit être strictement positive")

    rangees = lignes[1:]
    if len(rangees) != taille or any(len(r) != taille for r in rangees):
        raise ValueError("la grille doit être carrée et correspondre à la taille indiquée")
    if any(c not in ("0", "1") for r in rangees for c in r):
        raise ValueError("chaque cellule doit valoir 0 ou 1")

    return [[int(c) for c in r] for r in rangees]

from lib import write_grid

def compte_voisins(grille, x, y):
    voisins = 0
    lignes = len(grille)
    colonnes = len(grille[0])
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if (i, j) != (x, y) and 0 <= i < lignes and 0 <= j < colonnes:
                voisins += grille[i][j]
    return voisins

def nouvelle_valeur_cellule(etat_actuel, nb_voisins):
    if etat_actuel == 1:
        return 1 if nb_voisins in (2, 3) else 0
    else:
        return 1 if nb_voisins == 3 else 0

def calculer_generation_suivante(grille):
    lignes = len(grille)
    colonnes = len(grille[0])
    nouvelle_grille = [[0 for _ in range(colonnes)] for _ in range(lignes)]

def main():
    nb_cells = 50

    rng = random.Random(4200)

    matrix = [
        [rng.choice([0, 1]) for _ in range(nb_cells)]
        for _ in range(nb_cells)
    ]

    iter = 0
    filename = f"outputs/grid_{iter:04d}.png"
    write_grid(matrix=matrix, filename=filename)

if __name__ == "__main__":
    main()
