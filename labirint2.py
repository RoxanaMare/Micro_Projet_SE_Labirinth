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
0     0           0  0     0  0     0           0  0     0  0
0  0000  0000000000  0000  0  0  0  0000000  0000  0  0  0  0
0                 0  0     0     0  0        0     0  0  0  0
0000000000000000  0  0  0000000000  0  0000000  0000000  0  0
0     0           0     0        0  0  0     0           0  0
0  0000  0000000000  0000  0  0000  0  0  0000000000000000  0
0        0        0  0     0        0  0                 0  0
0000000000  0  0  0  0  0  0000000000  0000000000000000  0  0
0           0  0  0  0  0                 0                 0
0  0000000000  0000  0000000000000000000000  0000000000000  0
0           0        0              0        0     0        0
0000000000  0000000000  0000000000  0  0000  0  0000  0000000
0           0           0        0     0     0        0     0
0  0000000000  0000000000  0000000000000  0000000000000  0  0
0           0  0           0           0     0           0  0
0000000000  0  0  0000000000  0000  0000000  0  0000000000  0
0     0     0     0        0     0  0     0  0  0     0     0
0  0  0  0000000000  0000  0000  0  0  0  0000  0  0000  0000
0  0  0              0  0  0     0     0     0        0     0
0  0  0000000000000000  0  0  0  0000000000  0000  0  0000  0
0  0     0              0     0  0        0     0  0     0  0
0  0000  0  0000000  0000000000000  0000000000  0  0000000  0
0  0              0  0     0     0                 0        0
0  0000000  0  0000  0  0000  0  0000  0000  0  0000  0000000
0        0  0     0  0        0  0        0  0     0  0     0
0  0000  0  0000  0  0  0000000  0000000000  0000000  0000  0
0  0  0  0  0     0  0     0     0           0     0        0
0  0  0  0000  0000  0000  0  0000  0000000000  0  0000000000
0     0  0     0     0  0  0     0              0     0     0
0000000  0  0000000  0  0  0000  0  0000000000000000  0000  0
0        0     0     0  0  0  0     0                 0     0
0  0000000000  0  0000  0  0  0000  0  0000000000000000  0000
0  0     0     0        0  0        0  0     0        0  0  0
0  0  0  0  0000000000000  0000000  0  0  0  0000000  0  0  0
0     0  0                 0        0     0                 B
0000000000000000000000000000000000000000000000000000000000000

"""


""" on  verifie si les elements de la matrice sont deja visite ou pas. La verification se realise en refaisant le chemin, et en retournant si elle trouve une voie bloquee. """

from threading import Thread, Lock
_db_locks = Lock()
locks = threading.Lock()

def get_lock(posx, posy):
    if not posx in locks:
        locks[posx] = dict()
    if not posy in locks[posx]:
        locks[posx][posy] = threading.Lock()
    return locks[posx][posy]


class Solver(Thread):
    def __init__(self, maze, posx, posy, sizex, sizey):
        Thread.__init__(self)
        self.maze = maze
        self.posx = posx
        self.posy = posy
        self.sizex = sizex
        self.sizey = sizey
        self.found = 0
        
        """ On a la classe Solver qui contienne un constructeur avec les parametres:
            maze,
            posx et posy - les positions de x et de y
            sizex et size y - leurs tailles
            On a initialisee la valeur found avec 0 c.a.d que nous sommens au debut. """

    def run(self):
        lock = get_lock(self.posx, self.posy)
        if not lock.acquire(False): return    #on assure que seulement 1 thread marchera sur ce domaine
        
        if 0 <= self.posx < self.sizex and 0 <= self.posy < self.sizey:     #on verifie seulement pour les valeurs positives
            if self.maze[self.posy][self.posx] in (NONE, START):
                if self.maze[self.posy][self.posx] == NONE:
                    self.maze[self.posy][self.posx] = SEEN

                sub_solver1 = Solver(self.maze, self.posx, self.posy+1, self.sizex, self.sizey)
                sub_solver1.start()
                sub_solver2 = Solver(self.maze, self.posx, self.posy-1, self.sizex, self.sizey)
                sub_solver2.start()
                sub_solver3 = Solver(self.maze, self.posx-1, self.posy, self.sizex, self.sizey)
                sub_solver3.start()
                sub_solver4 = Solver(self.maze, self.posx+1, self.posy, self.sizex, self.sizey)
                sub_solver4.start()

        """On verifie en envoyant des threads si l'element de la matrice est un espace vide pres du point de debut.
            Puis on verifie si chaque position UP/DOWN/Right/LEFT, en comparant le point de reference qui peut etre localise dans l'intersection.s
