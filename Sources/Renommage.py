
# -*- coding: utf-8 -*-

from Action import *

class Renommage(Action) :
    '''
        Hérité de la classe action
        Ajoute les la possibilité d'effectuer un renommage en lot de fichiers
    '''
    def __init__(self,nomDuRepetoire,regle) : 
        """
            Constructeur hérité
        """
        Action.__init__(self,nomDuRepetoire,regle)

    def renommer(self) :
        """
           Effectue le renommage en lot des fichiers en fonction du résultat de la simulation
           Retourne le nombre de fichiers renommés
        """
        fileNb = 0
        for key,val in self.newNames.items() :
            oldName = self.nomDuRepertoire+os.sep+val[0]
            newName = self.nomDuRepertoire+os.sep+val[1]
            os.rename(oldName,newName)
            fileNb+=1
        return fileNb


