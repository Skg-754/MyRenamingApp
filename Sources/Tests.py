import unittest

from Action import *
from ListeRegles import *
from Regle import *
from Renommage import * 
from MyRenamingApp import *
import os

class Test(unittest.TestCase) :                           # on instancie une classe qui hérite de TestCast

    def setUp(self) :                                       # appelée à chaque exécution d'une function test_
        '''
             Function appelée au début d'un  d'un test
        '''
        # print('test started')
        self.myRule1 = Regle()
        self.myRule2 = Regle(amorce='chiffre',nomFichier='nomFichierModifé',extensions=[])
        self.myRule3 = Regle(amorce='lettre',apartirde='abc', prefixe='-prefixe-',postfixe='--sufixe--',nomFichier=True,extensions=['.txt, .png'])
        self.myAction1 = Action('./tests',self.myRule1)
        self.myAction3 = Action('./tests',self.myRule3)
        self.myRenommage1 = Renommage('./tests',self.myRule1)
        self.testFile = 'test_bkp'
        self.myList = ListeRegles(self.testFile)


    def tearDown(self) :
        '''
            Function appelée à la fin d'un test
        '''
        # print("test ended : "+str(id(self)))

    #__________Action__________

    def test_Action_simule(self) :
        '''
            Class : Action - Function  : simule
        '''
        self.myRule1.set_extensions(['.txt'])
        self.myRule1.set_amorce('chiffre')
        self.myRule1.set_nomFichier(False)
        result = self.myAction1.simule()
        self.assertEqual(result[0],True)            #  True si la simulatation est correcte
        self.assertEqual(result[1],{0: ('Nouveau document 2.txt', '000.txt'), 1: ('Nouveau document 3.txt', '001.txt'), 2: ('Nouveau document.txt', '002.txt')})    # résultat de la somulation
        self.assertEqual(result[1],self.myAction1.newNames)         # vérification du stockage du résultat
        self.myRule1.set_apartirde('999')
        result = self.myAction1.simule()
        self.assertEqual(result[0],False)            # erreur car l'amorce n'est pas assez grande pour le nombre de fichiers


    #__________ListeRegles__________

    def test_ListeRegles_sauvegarder(self) :
        '''
            Class : ListeRegles - Function  : sauvegarder
        '''
        
        if os.path.isfile(self.testFile) :                      # supression du fichier de bkp s'il existe
            os.remove(self.testFile)
        self.myList.set_fichier(self.testFile)                  # configuration du fichier de bkp dans l'objet    
        self.assertFalse(os.path.isfile(self.testFile))
        self.myList.sauvegarder('regle1',self.myRule1)          # sauvegarde de trois règles
        self.myList.sauvegarder('regle2',self.myRule2)
        self.myList.sauvegarder('regle3',self.myRule3)
        self.assertTrue(os.path.isfile(self.testFile))
        myFile = open(self.testFile,'rb')                       # lecture du fichier bkp
        result =  pickle.load(myFile)
        myFile.close()
        self.assertEqual(len(result),3)         # 3 élements dans le dictionnaire sérialisé du fichier

    def test_ListeRegles_charger(self) :
        '''
            Class : ListeRegles - Function  : charger
        '''
        self.test_ListeRegles_sauvegarder()
        myList2 = ListeRegles(self.testFile)     
        myList2.set_regles([])
        self.assertEqual(len(myList2.get_regles()),0)       
        myList2.charger()                                       
        self.assertEqual(len(myList2.get_regles()),3)

    def test_ListeRegles_supprimer(self) :
        '''
            Class : ListeRegles - Function  : supprimer
        '''
        self.myList.set_fichier(self.testFile)
        self.myList.charger()  
        self.assertEqual(len(self.myList.get_regles()),3)       
        self.myList.supprimer('regle1')                    
        self.assertEqual(len(self.myList.get_regles()),2)    
        self.myList.supprimer('regle2')
        self.assertEqual(len(self.myList.get_regles()),1)       
        self.myList.supprimer('regle3')                             
        self.assertEqual(len(self.myList.get_regles()),0) 

            
    def test_ListeRegles_sauvegarderTout(self) :
        '''
            Class : ListeRegles - Function  : sauvegarderTout
        '''
        customRules = {}   
        customRules['regle1'] = self.myRule1
        customRules['regle2'] = self.myRule2
        customRules['regle3'] = self.myRule2
        if os.path.isfile(self.testFile) :                      # supression du fichier de bkp s'il existe
            os.remove(self.testFile)
        self.myList.set_regles(customRules)
        self.myList.set_fichier(self.testFile)
        self.assertFalse(os.path.isfile(self.testFile))
        self.myList.sauvegarderTout()
        self.assertTrue(os.path.isfile(self.testFile))
        self.assertEqual(len(self.myList.get_regles()),3)
       


    def test_ListeRegles_get_rule(self) :
        '''
            Class : ListeRegles - Function  : get_rule
        '''
        self.myList.set_fichier(self.testFile)
        self.myList.charger()
        rule = self.myList.get_rule('regle1')
        self.assertTrue(isinstance(rule,Regle))
        self.assertEqual(str(rule),str(self.myRule1))


    #__________ListeRegles__________
    def test_Regle_init(self) :
        '''
            Class : Regle - Function  : __init__
        '''
        regle = Regle()
        self.assertTrue(regle,Regle)
        self.assertEqual(str(regle),"Class : Regle. Type d'amorce : aucune, début d'amorce : , préfixe : , postfixe : , nom du fichier : True, extensions : []")

    #__________Renommage__________
    def test_Renommage_renommer(self) : 
        '''
            Class : Renommage - Function  : renommer
        '''
        self.myRenommage1.simule()
        self.assertEqual(self.myRenommage1.renommer(),7)        


if __name__ == '__main__' :
    unittest.main()