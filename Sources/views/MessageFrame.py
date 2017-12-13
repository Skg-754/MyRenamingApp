# -*- coding: utf-8 -*-
from tkinter import *

class MessageFrame(Frame):
    '''
        Frame : Contient les "messages" de l'application à l'utilisateur
        Erreurs, simulations, confirmation de bonne exécution de commande, etc.
    '''

    def __init__(self, root, title, values) :

        Frame.__init__(self, root)

        self.title = title
        self.values = values

        self.build()

    def build(self) :
        '''
            Création et mise en place de tous les widgets de la page
        '''
        
        self.clear()

        # titre
        title = Label(self, text=self.title)
        title.pack()

        # messages
        for val in self.values :
            label = Label(self, text=val)
            label.pack()

    def clear(self) :
        """
            permet de supprimer tous les objets de la frame
        """
        for widget in self.winfo_children() :
            widget.destroy()

    def set_title(self, title) :
        self.title = title
        return self.title
    
    def set_values(self, values) : 
        self.values = values
        return self.values