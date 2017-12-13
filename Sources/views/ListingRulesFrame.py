# -*- coding: utf-8 -*-
from tkinter import *
from ListeRegles import *

class ListingRulesFrame(Frame):
    '''
        Frame : Contient la page "lister les règles", 
    '''

    def __init__(self, root) :

        Frame.__init__(self, root)
        self.rulesList = ListeRegles()
        self.regles = self.rulesList.charger()

        self.build()

    def build(self) :
        '''
            Création et mise en place de tous les widgets de la page
        '''
        mainTitleLabel = Label(self, text='Liste des règles enregsitrées')
        mainTitleLabel.pack()

        self.listBox = Listbox(self)

        for name,rule in self.regles.items() :
            self.listBox.insert(END, name)

        self.listBox.pack()
            
    def get_listBox(self) :
        return self.listBox.get(self.listBox.curselection())

    

            