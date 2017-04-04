
#Ca c'est la première partie de notre projet. En principe, nous avons écrit une partie qui concerne le modèle du labyrinthe et une partie de code,
#parce que on l'a pas fini. Il y a quelques choses qui manquent et à qui nous devons penser.

empty=" "
wall="0"
start="A"
end="B"
visited="-"
good="x"

LABYRINTH = """
0000000000000000000000000000000000000000000000000000000000000
A        0              0        0        0     0           0
0  0000  0000  0000000  0  0000  0  0000  0  0  0  0000000  0
0  0  0     0  0     0  0     0     0  0  0  0  0  0        0
0  0  0000  0  0000  0  0  0  0000000  0  0000  0000  0000000
0  0     0     0     0  0  0  0        0     0  0     0     0
0  0000  0  0000  0000  0000  0  0000000000  0  0  0000  0000
0  0     0     0     0  0     0  0     0  0     0  0        0
0  0  0000000000000  0  0  0000  0  0  0  0000000  0000  0  0
0        0        0              0  0     0        0     0  0
0000  0000  0  0000000  0  0000000  0000  0  0000000  0000  0
0     0     0  0        0  0        0     0  0        0     0
0  0000  0000000  0000000  0  0000000  0000  0  0000000  0000
0  0              0           0     0     0     0           0
0000  0000000000000  0000000000  0  0000  0000  0  0000000000
0     0           0     0     0  0     0        0  0        0
0  0000  0000000  0  0  0  0  0000000  0000000000  0  0000  0
0     0  0        0  0     0  0        0        0  0  0     0
0000  0000  0000000000000000  0  0000000  0000  0  0  0  0000
0  0  0     0                 0  0     0  0     0     0     0
0  0  0  0000  0000000000000000  0  0  0  0000000000000  0  0
0  0  0     0  0     0        0  0  0     0           0  0  0
0  0  0  0  0  0  0  0  0000  0  0  0000000  0000000  0  0  0
0  0  0  0  0     0  0  0     0  0     0     0     0     0  0
0  0  0000  0000000  0  0000000  0000  0000  0  0  0000000  0

"""

#Puis on va vérifier si les éléments de la matrice sont visités ou pas.
#La vérification se fait par la restauration de la route et où se trouve une route fermé il retourne.


def solve(labyrinth, x, y, m, n):
    path = False
    if 0 <= x < m and 0 <= y < n:
        if labyrinth[y][x] in (empty, start):
            if labyrinth[y][x] == empty:
                labyrinth[y][x] = visited
