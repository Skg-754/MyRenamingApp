# -*- coding: utf-8 -*-
from tkinter import *

class ButtonsFrame(Frame):
    '''
        Frame : Contient les buttons"
    '''

    def __init__(self, root, buttons) :

        Frame.__init__(self, root)
        self.buttons = buttons


        self.build()

    def build(self) :
        '''
            Création et mise en place de tous les widgets de la page
        '''

        self.clear()
        for button in self.buttons : 
            buttonInput = Button(self,text=button[0], command=button[1])
            buttonInput.pack(side=RIGHT)

    def clear(self) :
        """
            Permet de supprimer tous les objets de la frame
        """
        for widget in self.winfo_children() :
            widget.destroy()

    def set_buttons(self, buttons) : 
        self.buttons = buttons