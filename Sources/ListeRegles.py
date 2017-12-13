
# -*- coding: utf-8 -*-
import pickle
import os

class ListeRegles :
    """
        Permet la gestion de la liste de règles.
        Sauvegarde, chargement depuis le fichier MyRenamingApp.ini
    """
    def __init__(self, fichier='MyRenamingApp.ini'): 
        '''
            Constructeur
            Charge les règles présentes dans le fichier .ini à son instanciation
        '''
        self.regles = {}
        self.fichier = fichier
        self.charger()          
    
    def charger(self) : 
        '''
            Permet de charger la liste de règles à partir du fichier .ini
            Retourne le dictionnaire conteant les règles chargées (clé = nom de la règle, valeur = règle)
        '''
        if os.path.isfile(self.fichier) :
            myFile = open(self.fichier,'rb')
            self.regles =  pickle.load(myFile)
            myFile.close()
        return self.regles

    def sauvegarder(self, name, rule) :
        '''
            Ajoute la règle passée en paramètre au dictionnaire de règles
            Permet de sauvegarder la liste de règles à partir du fichier .ini
            Retourne le dictionnaire conteant les règles sauvegardées (clé = nom de la règle, valeur = règle)
        '''
        self.regles[name] = rule
        myFile = open(self.fichier,"wb")
        pickle.dump( self.regles,myFile)
        myFile.close()
        return self.regles[name]

    def sauvegarderTout(self) :
        ''' 
            Permet la sauvegarde de la liste complète des règles
            Retourne le dictionnaire conteant les règles sauvegardées (clé = nom de la règle, valeur = règle)
        '''
        myFile = open(self.fichier,"wb")
        pickle.dump(self.regles,myFile)
        myFile.close()
        return self.regles

    def supprimer(self, name) :
        '''
            Permet la supression de la regle dont le nom est passé en paramètre du dictionnaire contenant les règles
            Sauvegarde le dictionnaire ainsi mis à jour
        '''
        del self.regles[name]
        self.sauvegarderTout()
        return self.regles

    def get_rule(self, name) :
        '''
            Retourne la règle dont le nom est passé en paramètre
            Si la règle n'est pas présente dans le dictionnaire, retourne False
        '''
        return self.regles[name]


    def __str__(self) : 
        return "Class : ListeRegles. Fichier de sauvegarde : {}".format(
                self.fichier)

    def get_fichier(self) : 
        return self.fichier
    def get_regles(self) : 
        return self.regles
    def set_fichier(self, fichier) :
        self.fichier = fichier
        return self.fichier        
    def set_regles(self,regles) : 
        self.regles = regles
        return self.regles