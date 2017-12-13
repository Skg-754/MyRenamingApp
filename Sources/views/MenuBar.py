# -*- coding: utf-8 -*-
from tkinter import *

class MenuBar(Menu):
    '''
        Menu : Création du menu de la fenêtre principale
    '''

    def __init__(self, menus) :

        Menu.__init__(self)

        self.menus = menus

        self.build()

    def build(self) :

        self.buildMenu(self.menus, self)
 
    def buildMenu(self, menus,root) :
        '''
            Permet de créer automatiquement l'arborescence de la barre de menu en fonction d'un dictionnaire
        '''
        for menu,value in menus.items() :
            if isinstance(value,dict) :
                subMenu = Menu(root,tearoff=0)
                self.buildMenu(value,subMenu)
                root.add_cascade(label=menu, menu=subMenu)
            else : 
                root.add_command(label=menu, command=value)