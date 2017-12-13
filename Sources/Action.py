
# -*- coding: utf-8 -*-
import os
from utils import increment
import re

class Action : 
    '''
        Classe permettant d'effectuer une simulation de renommage en fonction d'un dossier et d'une règle de renommage
    '''
    def __init__(self,nomDuRepetoire,regle) : 
        '''
            Constructeur
            Prend en paramètre le répertoire contenant les fichiers à renommer et la règle de renommage à appliquer aux fichiers
        '''
        self.nomDuRepertoire = nomDuRepetoire
        self.regle = regle
        self.files = []                             # liste des fichiers à renommer
        self.newNames = {}                          # dictionnaire contenant des tuples (ancien nom, nouveau nom) pour chaque fichier à renommer

        # paramètres de la règle de renommage
        self.amorces = None
        self.prefixe = ""
        self.postfixe = ""
        self.fileName = False
        self.errorList = []

    def simule(self) :
        """
            Effectue une simulation de renommage
            Retourne un tuple contenant un boolean en première valeur : True si simulation réussie, False si simulation en erreur
            La deuxième valeur du boolean est :
            Soit un dictionnaire contenant les tuples avec le nom d'origine et le nouveau nom de chaque fichier. 
            Soit une liste des erreurs rencontrées
        """
        # analyse du dossier
        if(os.path.isdir(self.nomDuRepertoire)) :
            self.files = os.listdir(self.nomDuRepertoire)
        else : 
            self.errorList.append("Répertoire non trouvé")


        indexesToRemove = []

        # si un filtre d'extensions est renseigné
        for index,fileName in enumerate(self.files) : 
            if os.path.isdir(self.nomDuRepertoire+os.sep+fileName) :                              # on enlève s'il s'agit d'un dossier
                indexesToRemove.append(index)
            elif fileName.find('.') == -1 :                                                       # on exclue des fichiers sans extensions du renommage
                indexesToRemove.append(index)
            else :
                if self.regle.get_extensions() :    
                    #recherche des index à supprimer
                    fileExtension = fileName.rsplit('.',1)[1]
                    if not ('.'+fileExtension in self.regle.get_extensions()) :
                        indexesToRemove.append(index)
                    
        #suppression des indexs.
        indexesToRemove.reverse()
        for index in indexesToRemove :
            self.files.pop(index)

        # analyse de la rgèle de renommage
        self.analyseRegle()

        temoin = []         # liste temporaire dans laquelle on rentre les nouveaux noms de fichier afin de vérifier qu'il n'y ait pas de doublons
        # simulation du renommage
        for index,file in enumerate(self.files) :
            fileName = file.rsplit('.',1)[0]
            fileExtension = file.rsplit('.',1)[1]

            newName = ""
            if self.amorces :
                newName += self.amorces[index]
            newName += self.prefixe
            if self.fileName :
                if self.fileName == True :
                    newName += fileName
                else :
                    newName += self.fileName
            newName += self.postfixe+"."+fileExtension

            if newName in temoin :
                self.errorList.append('Doublons détectés. Veuillez ajuster votre règle pour éviter les doublons')
            else : 
                self.newNames[index] = (file,newName)
                temoin.append(newName)

        # vérification qu'il n'y a pas de doublons dans les noms de fichiers générés

        # il faut retourner le résultat sous forme de listes pour pouvoir la comparer à un set. 
            
        
        if len(self.errorList) == 0 :
            return (True,self.newNames)
        else : 
            return (False,self.errorList)

    def analyseRegle(self) : 
        """ 
            Analyse la règle et stocke les paramètres dans les attributs de l'objet
            Permet d'éviter de réanalyser complètement la règle pour chaque mot. 
        """
        if self.regle.get_amorce() :                                                            # si la règle contient une amorce                           
            if self.regle.get_amorce() == "lettre" :                                            
                if self.regle.get_apartide() :
                    self.amorces = increment(self.regle.get_apartide(),len(self.files))
                else :
                    self.amorces = increment('aaa',len(self.files))
            elif self.regle.get_amorce() == "chiffre" :
                if self.regle.get_apartide() :
                    self.amorces = increment(self.regle.get_apartide(),len(self.files))
                else :
                    self.amorces = increment('000',len(self.files))
            elif self.regle.get_amorce() == "aucune" :
                self.amorces = ""
        if(self.amorces == False) : 
              self.errorList.append("Amorce trop courte pour le nombre de fichiers à renommer. Essayez de rajouter un caractère")
            

        # analyse du reste de la règle
        if self.regle.get_prefixe() :
            self.prefixe = self.regle.get_prefixe()

        self.fileName = self.regle.get_nomFichier()

        if self.regle.get_postfixe() :
            self.postfixe = self.regle.get_postfixe()

    def __str__(self) :
        return "Class : Action. Nom du répertoire : {}, regle : {}".format(
                self.nomDuRepertoire, self.regle)
    
    # getters

    def get_nomDuRepertoire(self) :
        return self.nomDuRepertoire

    def get_regle(self) :
        return self.regle

    def get_newNames(self) : 
        return self.newNames

    def get_amorces(self) : 
        return self.amorces
    def get_prefixe(self) :
        return self.prefixe
    def get_postfixe(self) : 
        return self.postfixe
    def get_fileName(self) : 
        return self.get_fileName
    def get_errorList(self) : 
        return self.errorList

    # setters

    def set_nomDuRepertoire(self, nomDuRepertoire) :
        self.nomDuRepertoire = nomDuRepertoire
        return self.nomDuRepertoire

    def set_regle(self, regle) :
        self.regle = regle
        return self.regle

