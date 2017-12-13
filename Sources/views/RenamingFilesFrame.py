# -*- coding: utf-8 -*-
from tkinter import *
from views.HeaderFrame import *
from views.RuleFrame import *


class RenamingFilesFrame(Frame):
    '''
        Frame : Contient la page "Renommer les fichiers", 
        Affiche le nom du concepteur du logiciel, la version
    '''
    def __init__(self,root,mainTitle = 'Renommer en lots', formTitle = 'Nom du répertoire') :          
        Frame.__init__(self, root)
        self.headerFrame = None
        self.ruleFrame = None
        self.mainTitle = mainTitle
        self.formTitle = formTitle
        self.build()

    def build(self) :
        '''
            Création et mise en place de tous les widgets de la page
        '''
        self.headerFrame = HeaderFrame(self, self.mainTitle,self.formTitle)
        self.headerFrame.pack(padx=100,pady=20)

        self.ruleFrame = RuleFrame(self)
        self.ruleFrame.pack(padx=100,pady=20)

    def loadRule(self, name) : 
        '''
            Permet de charger une règle dans le formulaire de le frame 'Rule'
        '''
        self.ruleFrame.loadRule(name)

    def get_allInputs(self) :
        '''
            Retourne toutes les entrées des formulaires de la page sous forme de dictionnaire
        '''
        self.headerFrame.get_formVal()

        allInputs = self.ruleFrame.get_allInputs()
        allInputs['headerVal'] = self.headerFrame.get_formVal()

        return allInputs
    