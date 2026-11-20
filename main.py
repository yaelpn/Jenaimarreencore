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
