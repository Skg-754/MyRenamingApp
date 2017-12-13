# -*- coding: utf-8 -*-
from tkinter import *
from views.RenamingFilesFrame import *

class CreatingRuleFrame(RenamingFilesFrame):
    '''
        Frame : Contient la page "Créer une règle", 
        Hérité de la page "Renommer en masse"
    '''
    def __init__(self, root) :
        RenamingFilesFrame.__init__(self, root, 'Créer une règle', 'Nom de la règle')

        

