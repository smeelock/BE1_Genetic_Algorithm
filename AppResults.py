from Ant import *
from Civilization import *

from tkinter import *
from tkinter.messagebox import showinfo
import random

COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

# --------------------------------------------------------
class ResultsZone(Canvas):
    def __init__ (self, master, civ, lst_cities=[], lst_routes=[], w=500, h=400, _bg='white'):
        self.__w = w
        self.__h = h

        # Lst of nodes
        self.__nodes = []

        # Border around Canvas
        self.__master = master
        Canvas.__init__(self, master, width=w, height=h, bg=_bg, relief=RAISED, bd=5)

        # Civilization (ie environnment)
        self.__civ = civ

        # Cities and routes
        self.__cities = lst_cities
        self.__routes = lst_routes
        self.drawAllCities()
        self.drawAllRoutes()

        # Ants
        self.__ants = civ.getAnts()
        self.__antsRectID = [] # lst of id of shapes representing ants. Useful when erasing previous position of ants
        self.drawAllAnts()
        print("DEBUG ants ", self.__ants)

    def screenClickAction(self, event):
        print("Trace : (x,y) = ", event.x, event.y)
        
        # Place node where mouse clicked
        self.__master.drawNodeInCanva(event.x, event.y) 

    def getDims(self):
        return (self.__w, self.__h)
    
    def drawAllCities(self):
        for city in self.__cities:
            x, y = city.getX(), city.getY()
            self.drawNodeInCanva((x/200 + 1/2)*self.__w, (y/200 + 1/2)*self.__h) # (0 0) is center of window
                    # normalization because cities coordinates are in [-100 100]
            # self.__master.drawNode(x, y)

    def drawAllRoutes(self):
        for route in self.__routes:
            start_city, end_city = route.getStartCity(), route.getEndCity()
            x1, y1 = start_city.getX(), start_city.getY()
            x2, y2 = end_city.getX(), end_city.getY()
            self.drawRouteInCanva((x1/200 + 1/2)*self.__w, (y1/200 + 1/2)*self.__h, (x2/200 + 1/2)*self.__w, (y2/200 + 1/2)*self.__h) # (0 0) is center of window
                # normalization because cities coordinates are in [-100 100]
            # self.__master.drawRoute(x1, y1, x2, y2)

    def drawNodeInCanva(self, x, y):
        radius = 10
        outline_color = random.choice(COLORS)
        fill_color = outline_color
        self.create_oval(x - radius, y - radius, x + radius, y + radius, outline=outline_color, fill=fill_color)
        self.pack()

        # TODO : add id to each node and save it in list in order to be able to supresse it later.
        # TODO : BUT, this here is only for displaying the results, so technically, no need to be able to supress it...

        # self.__nodes.append(node)
        # self.set_coordonnes_du_last_node(x,y)
        # self.__liste_coordonnes_centre_des_nodes.append((x,y))
    
    def drawRouteInCanva(self, x1, y1, x2, y2, color='black'):
        fill_color = color
        self.create_line(x1, y1, x2, y2, fill=fill_color)
        self.pack()
    
    def drawAntInCanva(self, x, y, color):
        r = 5
        outline_color = color
        fill_color = outline_color
        antRectID = self.create_rectangle(x-r, y-r, x+r, y+r, outline=outline_color, fill=fill_color)
        self.pack()
        self.__antsRectID.append(antRectID)
    
    def drawAllAnts(self):
        # Erase previous position
        if len(self.__antsRectID) > 0 :
            for ID in self.__antsRectID: 
                self.delete(ID)
            self.__antsRectID = [] # resetting previous shapes ID, must be empty to enter following loop
            self.update()

        for ant in self.__ants:
            # Re-draw ants at new position
            x, y = ant.getX(), ant.getY()
            # color = COLORS[ant.getID()]
            color = 'red'
            self.drawAntInCanva((x/200+1/2)*self.__w, (y/200+1/2)*self.__h, color)
            
            # Draw each ants' followed path
            x_prev, y_prev = ant.getLastPosition()
            self.create_line((x_prev/200+1/2)*self.__w, (y_prev/200+1/2)*self.__h, (x/200+1/2)*self.__w, (y/200+1/2)*self.__h, fill=color)
            self.pack()


            # TODO: add shape property to ant and reset followed route when returning home...
        
        

class MainWindow(Tk):
    def __init__(self, civ, lst_cities=[], lst_routes=[]):
        Tk.__init__(self)
        self.title('ESSAI GRAPHE')

        # Civilization (ie environnment)
        self.__civ = civ

        self.__resultsZone = ResultsZone(self, civ, lst_cities, lst_routes)
        self.__resultsZone.pack()

        self.__nodes = []

        # Buttons
        self.__buttonStart = Button(self, text='Simulation Step', command=self.simulationStep).pack(side=LEFT, padx=5, pady=5)
        self.__boutonUndo = Button(self, text='Undo', command=self.undo).pack(side=LEFT, padx=5, pady=5)
        self.__boutonErase = Button(self, text='Erase', command=self.eraseScreen).pack(side=LEFT, padx=5, pady=5)
        self.__boutonQuit = Button(self, text='Quit', command=self.destroy).pack(side=LEFT, padx=5, pady=5)

        # Set action for mouse click 1 (defined in resultsZone screenClickAction)
        self.__resultsZone.bind('<Button-1>', self.__resultsZone.screenClickAction)
    
    def undo(self):
        pass

    def eraseScreen(self):
        pass

    def simulationStep(self):
        for i in range(10): # skip forward 10 steps
            self.__civ.stepForward()
            self.__resultsZone.drawAllAnts()














# ==================== code du prof===================
# ==================================================
# ===================================================

# class ZoneAffichage(Canvas):
#     def __init__(self, parent, w=500, h=400, _bg='white'):  # 500x400 : dessin final !
#         self.__w = w
#         self.__h = h
#         self.__liste_noeuds = []

#         # Pour avoir un contour pour le Canevas
#         self.__fen_parent=parent
#         Canvas.__init__(self, parent, width=w, height=h, bg=_bg, relief=RAISED, bd=5)


#     def get_dims(self):
#         return (self.__w, self.__h)

#     def not_used_keep_dessiner_graphe(self):
#         for b in self.__liste_noeuds:
#             b.deplacement()
#         self.after(50, self.dessiner_graphe)  # Important, sinon on fera une seul execution

#     def creer_noeud(self, x_centre, y_centre, rayon , col, fill_color="white"):
#         noeud=Balle(self, x_centre, y_centre, rayon , col)
#         self.pack()
#         return noeud

#     def action_pour_un_clique(self, event):
#         print("Trace : (x,y) = ", event.x, event.y)
#         #showinfo('Résultat ', "Arrrgh : vous avez dans la fenetre" + '\nThanks !')
        
#         # Placer un noeud à l'endroit cliqué
#         self.__fen_parent.placer_un_noeud(event.x, event.y)


#     def not_used_set_coordonnes_du_last_node(self, x_centre, y_centre):
#         self.__last_node=(x_centre, y_centre)

#     def placer_un_noeud_sur_canevas(self, x_centre, y_centre, col=None, fill_color="white"):
#         w,h = self.get_dims()
#         rayon=5
#         if col == None :
#             col= random.choice(['green', 'blue', 'red', 'magenta', 'black', 'maroon', 'purple', 'navy', 'dark cyan'])

#         node=self.creer_noeud(x_centre, y_centre, rayon , col, fill_color)
#         self.update()

#         self.__fen_parent.set_coordonnes_du_last_node(x_centre, y_centre)
#         return node.get_node_ident()


# class FenPrincipale(Tk):
#     def __init__(self):
#         Tk.__init__(self)
#         self.title('ESSAI GRAPHE')
#         self.__zoneAffichage = ZoneAffichage(self)

#         self.__zoneAffichage.pack()

#         # ----------------------------
#         # Création d'un widget Button (bouton Effacer)
#         self.__boutonEffacer = Button(self, text='undo last node', command=self.undo_last_noeud).pack(side=LEFT, padx=5, pady=5)

#         # Création d'un widget Button (bouton Effacer)
#         self.__boutonEffacer = Button(self, text='Effacer', command=self.effacer).pack(side=LEFT, padx=5, pady=5)
#         # Création d'un widget Button (bouton Quitter)
#         self.__boutonQuitter = Button(self, text='Quitter', command=self.destroy).pack(side=LEFT, padx=5, pady=5)

#         self.__zoneAffichage.bind('<Button-1>', self.__zoneAffichage.action_pour_un_clique)

#         self.__liste_d_ident_d_objets_crees=[]
#         self.__liste_coordonnes_centre_des_nodes=[]

#         self.placer_noeud_depart()

#     def add_a_node_to_your_list(self, noeud) :
#         self.__liste_d_ident_d_objets_crees.append(noeud)
        
#     def placer_un_noeud(self, x, y):
#         node=self.__zoneAffichage.placer_un_noeud_sur_canevas(x,y)
#         self.add_a_node_to_your_list(node)
#         self.set_coordonnes_du_last_node(x,y)
#         self.__liste_coordonnes_centre_des_nodes.append((x,y))


#     def set_coordonnes_du_last_node(self, x_centre, y_centre):
#         self.__last_node=(x_centre, y_centre)

#     def get_last_node(self):
#         return self.__last_node

#     def placer_noeud_depart(self):
#         w,h = self.__zoneAffichage.get_dims()
#         x_centre, y_centre=20, h//2
#         node= self.__zoneAffichage.placer_un_noeud_sur_canevas(x_centre, y_centre, col="red", fill_color="red")
#         self.add_a_node_to_your_list(node)
#         self.__liste_coordonnes_centre_des_nodes.append((x_centre, y_centre))

#     #--------------------------
#     #

#     def undo_last_noeud(self):
#         print("Avant undo, liste contient {} elements".format(len(self.__liste_d_ident_d_objets_crees)))
#         if len(self.__liste_d_ident_d_objets_crees)==1 :
#             print("Peut pas enlever noeud départ")
#             return

#         x_centre,  y_centre=self.get_last_node()

#         last_node=self.__liste_d_ident_d_objets_crees.pop()

#         # Pour supprimer, il faut can_id du noeud, pas le noeud lui mm !!
#         self.__zoneAffichage.delete(last_node)
#         self.__zoneAffichage.update()

#         x_last_node,y_last_node=self.__liste_coordonnes_centre_des_nodes.pop()
#         self.set_coordonnes_du_last_node(x_last_node,y_last_node)
#         print("Après undo, liste contient {} elements".format(len(self.__liste_d_ident_d_objets_crees)))

        

#     def ajout_noeud(self):
#         # Dessin d'un petit cercle
#         x_centre,  y_centre = self.not_used_generer_un_point_XY_dans_une_bande()
#         print("(x,y) =", x_centre, ' , ', y_centre)

#         rayon=5
#         col= random.choice(['green', 'blue', 'red', 'magenta', 'black', 'maroon', 'purple', 'navy', 'dark cyan'])
#         self.__zoneAffichage.creer_noeud(x_centre, y_centre, rayon , col)
#         self.__zoneAffichage.update()
#         self.__last_node=(x_centre, y_centre)


#     def effacer(self):
#         """ Efface la zone graphique """
#         self.__zoneAffichage.delete(ALL)
#         self.__liste_d_ident_d_objets_crees.clear()
#         self.__liste_coordonnes_centre_des_nodes.clear()
#         self.placer_noeud_depart()
# #--------------------------
# class Balle:
#     def __init__(self, canvas, cx, cy, rayon, couleur, fill_color="white"):
#         self.__cx, self.__cy = cx, cy
#         self.__rayon = rayon
#         self.__color = couleur
#         self.__can = canvas  # Il le faut pour les déplacements

#         self.__canid = self.__can.create_oval(cx - rayon, cy - rayon, cx + rayon, cy + rayon, outline=couleur, fill=fill_color)
#         # Pour 3.6 : col: object  # essaie typage !

#     def get_node_ident(self):
#         return self.__canid

#     def NoNeed_Here_not_used_generer_un_point_XY_dans_une_bande(self, last_x, last_y):
#         w,h = self.__can.get_dims()
#         #last_x, last_y=self.__last_node
#         delta_x_centre = random.randint(10, 50); delta_y_centre = random.randint(10, 50)
#         hasard_x=random.randint(0, 1); hasard_y=random.randint(0, 1)

#         x_centre = last_x+random.randint(10, 50)* 1 if hasard_x else -1
#         y_centre = last_y+random.randint(10, 50)* 1 if hasard_y else -1
#         if x_centre < 0 :  x_centre*=-1
#         if y_centre < 0 :  y_centre*=-1
#         return (x_centre, y_centre)

#     # Un seul déplacement
#     def not_used_keep_deplacement(self):
#         self.__can.move(self.__canid, 0, 0)
