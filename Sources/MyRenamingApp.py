# -*- coding: utf-8 -*-
from tkinter import *
# from tkinter.ttk import *
from Regle import *
from Renommage import * 
from ListeRegles import *
import re
import collections

# Frames communes à toutes les pages = socle de base de la fenêtre principale
from views.ButtonsFrame import *
from views.MessageFrame import *
from views.MenuBar import *

# Frames des différentes pages de l'application
from views.RenamingFilesFrame import *
from views.ListingRulesFrame import *
from views.CreatingRuleFrame import *
from views.AboutFrame import *
from utils import valid_filename_characters

class MyRenomerApp :
    """ 
        Classe Principale de l'application MyRenomerApp
    """

    def __init__(self,root) :
        """
            Prend en paramètre le conteneur sur lequel sera affichée l'interface graphique. 
        """
        self.root = root                            # conteneur de l'application                           
        self.baseView = Frame(self.root)            # conteneur des différentes pages de l'application    


        # Widgets communs à toutes les pages
        self.buttonsFrame = None                    # conteneurs des boutons 
        self.messageFrame = None                    # conteneurs des messages 
        self.menuBar = None                         # barre de menu de l'application


        # Instanciation des différentes pages de l'application
        self.renamingFilesFrame = RenamingFilesFrame(self.baseView)             # page peremttant de renommage des fichiers             
        self.creatingRuleFrame = CreatingRuleFrame(self.baseView)               # page permettant la création de règles
        self.listingRulesFrame = ListingRulesFrame(self.baseView)               # page permettant de lister et rappeler les régles
        self.aboutFrame = AboutFrame(self.baseView)                             # page "About" contenant les infos sur l'application

        # création du menu
        menus = collections.OrderedDict()
        menus['Règles'] = {}
        menus['Règles']['Lister'] = self.listerMenuCallback
        menus['Règles']['Créer'] = self.creerMenuCallback
        menus['?'] = self.aboutMenuCallback

        self.menuBar = MenuBar(menus)
        root.config(menu=self.menuBar)

        # affichage de la page de démarrage
        self.renamingFilesFrame.pack()
        self.baseView.pack()

        # affichage des boutons de la page de démarrage
        buttons = [
            ('Simuler',self.simulerCallback)
            ]
        self.buttonsFrame = ButtonsFrame(self.root,buttons)
        self.buttonsFrame.pack(padx=100,pady=20)

        # Ajout de la frame messages (vide)
        self.messageFrame = MessageFrame(self.root,"",[])
        self.messageFrame.pack(padx=100,pady=20)



    def ruleFromAnalysis(self, inputVar) : 
        """ 
            Analyse le formulaire de règle, vérifie sa validité et instancie l'object Règle correspondant
            Prend en paramètre le dictionnaire retourné par le formualaire de création de règle
            Retourne un objet "Regle"
        """
            
        # suppression des tabs dans les champs texte
        for key,element in inputVar.items() :
            userInput = element.get()
            if isinstance(userInput, str) :                                 # si la variable analysée est une string
                if valid_filename_characters(userInput) :                   # si elle ne contient pas de caractères interdits 
                    inputVar[key] = userInput.expandtabs(0)                 #suppression des éventuels tabs    
                else :                                                             
                    self.messageFrame.set_title("Erreur ! Les caractères suivants ne sont pas autorisés : ")
                    self.messageFrame.set_values(['? < > : " \ ? *'])
                    self.messageFrame.build()

            else :
                inputVar[key] = userInput                                   # mise à jour du dictionaire avec la valeur reformatée

              
        # parsing des extensions        
        if inputVar['extensions'] != '' :
            inputVar['extensions'] = inputVar['extensions'].split(", ") 
        else : 
            inputVar['extensions'] = False

        # traitement de la variable mon fichier.
        if inputVar['modeFichier'] == 0 :
            inputVar['nomFichier'] = True
        else : 
            if inputVar['nomFichier'] == '' :  
                inputVar['nomFichier'] = False              
                # on passe la valeur à False s'il ne faut pas garder le nom original et qu'il n'y a pas de nom personnalisé de renseigné

        
        # appel de la création de la règle
        # amorce=None,apartirde=False, prefixe=False,postfixe=False,nomFichier=True,extensions=[])         
        myRule = Regle(
            amorce = inputVar['amorce'],                                  # "aucune","lettre","chiffre"                       
            apartirde = inputVar['apartirde'],                           # "AAA","000","abc"
            prefixe = inputVar['prefixe'],                               # "" ou "_prefixe_"
            postfixe = inputVar['postfixe'],                             # "" ou "_suffixe_"
            nomFichier = inputVar['nomFichier'],                         # False, True, "nomFichierPersonnalisé"
            extensions = inputVar['extensions']                          # Si vide, on prend tout
            )

        return myRule
      

    # callback de la barre de menus

    def creerMenuCallback(self) :
        '''
            Fonction appelée lors de la sélection du bouton "Créer" dans la barre de menus
            Affiche la page de Création de règle
        '''
        self.clearWidget(self.baseView)                                 # supression de la page actuelle
        self.creatingRuleFrame.pack()                                   # mise en place de la page Création de Regle

        buttons = [                                                     # ajout des boutons
            ('Créer une nouvelle règle', self.creerRegleCallback),
            ('Retour', self.retourCallback)
            ]
        self.buttonsFrame.set_buttons(buttons)
        self.buttonsFrame.build()

        self.messageFrame.clear()                                       # Remise à zéro de la frame message

    def listerMenuCallback(self):
        '''
            Fonction appelée lors de la sélection du bouton "Lister" dans la barre de menus
            Affiche la page de listing des règles
        '''
        self.clearWidget(self.baseView)                                         # supression de la page actuelle
        self.listingRulesFrame = ListingRulesFrame(self.baseView)               # mise en place de la page Création de Regle
        self.listingRulesFrame.pack()

        buttons = [                                                             # ajout des boutons
            ('Selectionner',self.selectionnerRegleCallback),
            ('Supprimer', self.supprimerRegleCallback),
            # ('Créer une nouvelle règle', self.creerRegleCallback),
            ('Retour', self.retourCallback)
            ]
        self.buttonsFrame.set_buttons(buttons)
        self.buttonsFrame.build()

        self.messageFrame.clear()                                       # Remise à zéro de la frame message

    def aboutMenuCallback(self) :
        '''
            Fonction appelée lors de la sélection du bouton "?" dans la barre de menus
            Affiche la page "about" contenant les informations du logiciel
        '''
        self.clearWidget(self.baseView)                                         # supression de la page actuelle
        self.aboutFrame.pack()                                                  # mise en place de la page Création de Regle

        buttons = [                                                             # ajout des boutons
            ('Retour', self.retourCallback)
            ]
        self.buttonsFrame.set_buttons(buttons)
        self.buttonsFrame.build()

        self.messageFrame.clear()                                       # Remise à zéro de la frame message

    # Callback de la page Renommer
   
    def simulerCallback(self) :
        '''
            Fonction appelée lors de la sélection du 'simuler' dans la page "Renommer"
            Récolte les données du formulaire de renommage
            Créé la règle de renommage en fonction des paramètre renseignés par l'utilisateur
            Effectue une simulation de renommage
            Affiche le résultat de la simulation dans la Frame messages OU affiche les erreurs dans la frame messages
        '''

        userEntry = self.renamingFilesFrame.get_allInputs()                     # récupération des entrée utilisateurs depuis la Frame contenant le formulaire
        folder = userEntry['headerVal'].get()                                   # récupération du nom du dossier
        del userEntry['headerVal']
        myRule = self.ruleFromAnalysis(userEntry)                               # Analyse des données utilisateur et création de la règle
 

        self.action = Renommage(folder,myRule)                                  # instanciation d'un objet de renommage
        success,result = self.action.simule()                                   # on effectue une simulation de renommage
        if success :                                                            # mise en forme du resultat de la simulation si OK
            # affichage du résultat de la simulation
            message = []
            for index, val in result.items() : 
                message.append(val[0]+'--->'+val[1])

            buttons = [                                                         # mise en place des boutons Annuler et Renommer
                ('Annuler',self.annulerCallback),   
                ('Renommer',self.renommerCallback)
                ]
            self.buttonsFrame.set_buttons(buttons)
            self.buttonsFrame.build()

            self.messageFrame.set_title("Résultat de la simulation : ")         # affichage du resultat
            self.messageFrame.set_values(message)
            self.messageFrame.build()


        else : 
            # affichage du message d'erreur pour permettre à l'utilisateur de modifier sa règle
            self.messageFrame.set_title("Erreur lors de l'exécution de la simulation : ")
            self.messageFrame.set_values(result)
            self.messageFrame.build()
        
    def annulerCallback(self) :
        """
           Fonction appelée lors de la sélection du 'annuler' dans la page "Renommer" après avoir effectué une simulation
           Retour à l'état initial de la vue 
        """

        buttons = [                                                             # affichage du bouton simuler
            ('Simuler',self.simulerCallback)
            ]
        self.buttonsFrame.set_buttons(buttons)
        self.buttonsFrame.build()

        self.messageFrame.clear()                                               # remise à zéro du messageFrame

    def renommerCallback(self) :
        """
            Fonction appelée lors de la sélection du 'annuler' dans la page "Renommer" après avoir effectué une simulation
            Retour à l'état initial de la vue
            Affichage du message de succès de renommage et du nombre de fichiers renommés
        """
        self.annulerCallback()                                                  # retour à la vue initilase

        success = self.action.renommer()                                        # affichage du résultat du renommage           
        if success :
            self.messageFrame.set_title("Renommage réussi !")
            self.messageFrame.set_values(['%i fichiers renommés'%success])
            self.messageFrame.build()
        else : 
            self.messageFrame.set_title("Oups !!")
            self.messageFrame.set_values(['Aucun fichier n\'a été renommé'])
            self.messageFrame.build()

        return success



    # Callback de la page Créer Règle
    
    def creerRegleCallback(self) : 
        '''
            Fonction appelée lors de la sélection du bouton 'Créer une nouvelle règle' dans la page "Créer Règle"
        ''' 
        self.messageFrame.clear()                                               # remise à zéro du messageFrame

        userEntry = self.creatingRuleFrame.get_allInputs()                      # récupération des entrées utilisateur
        myRuleName = userEntry['headerVal'].get()                               # récupération du nom de la règle à créer

        myRule = self.ruleFromAnalysis(userEntry)                               # analyse et création de la règle

        backup = None
        if myRuleName == "" :                                                   # vérification de la validité du nom de la règle
            self.messageFrame.set_title("Erreur lors de la création de la règle ")
            self.messageFrame.set_values(["Le nom de la règle est requis"])
            self.messageFrame.build()
        else : 
            listeRegles = ListeRegles()
            myList = listeRegles.charger()
            rulesNames = myList.keys()
            if myRuleName in rulesNames :                                       # vérification que le nom de la règle n'est pas déjà utilisé
                self.messageFrame.set_title("Erreur lors de la création de la règle ")
                self.messageFrame.set_values(["Le nom choisis est déjà utilisé"])
                self.messageFrame.build()
            else :                                                              # Réalisation de la sauvegarde de la règle
                backup = listeRegles.sauvegarder(myRuleName, myRule)

        if backup :                                                             # si le backup a eu lieu, affichage du message
            self.messageFrame.set_title("Règle enregistrée !")
            self.messageFrame.set_values([])
            self.messageFrame.build()
        else :
            self.messageFrame.set_title("Erreur lors de la création de la règle")
            self.messageFrame.set_values([])
            self.messageFrame.build()

        return backup

    # callback de la page Lister Règles

    def selectionnerRegleCallback(self) :
        '''
            Fonction appelée lors de la sélection du bouton 'Sélectionner' dans la page "Liste des régles enregistrée"
            Provoque un retour sur la page de Renommage avec la règle sélectionnée appliquée
        '''
        toSelect = self.listingRulesFrame.get_listBox()             # récupération du nom de la règle à sélectionner
        
        self.clearWidget(self.baseView)                             # suppression de la page Liste des Règles
        self.renamingFilesFrame.loadRule(toSelect)                  # application du chargement de la règle dans la page Renommer
        self.renamingFilesFrame.pack()                              # affichage de la page renommer

        buttons = [                                                 # ajout des boutons
            ('Simuler',self.simulerCallback)
            ]
        self.buttonsFrame.set_buttons(buttons)                      
        self.buttonsFrame.build()
    
    def supprimerRegleCallback(self) :
        '''
            Fonction appelée lors de la sélection du bouton 'Supprimer' dans la page "Liste des régles enregistrée"
            Permet la suppression de la règle du fichier de stockage
            Provoque un rafraichissement de la page pour actualiser la liste des règles
        '''
        toDelete = self.listingRulesFrame.get_listBox()                 # récupération du nom de la règle à supprimer
        listeRegles = ListeRegles()                                     # suppression de la règle dans le fichier
        myList = listeRegles.charger()
        listeRegles.supprimer(toDelete)

        self.messageFrame.set_title("Règle supprimée avec succès")      # affichage du message de succès
        self.messageFrame.set_values([])
        self.messageFrame.build() 

        self.clearWidget(self.baseView)                                 # rafraichissement de la Frame de Liste de règles
        self.listingRulesFrame = ListingRulesFrame(self.baseView)
        self.listingRulesFrame.pack()


     # callback génériques

    def retourCallback(self) : 
        '''
            Fonction appelée par les boutons "retour" des différents pages
            Provoque un retour à la page d'accueil de l'application (page Renommage)
        '''
        self.clearWidget(self.baseView)                                 # Suppression de la page actuelle
        self.renamingFilesFrame.pack()                                  # Affichage de la page renommer
        buttons = [                                                     # Ajout des boutons
            ('Simuler',self.simulerCallback)
            ]
        self.buttonsFrame.set_buttons(buttons)
        self.buttonsFrame.build()

    def clearWidget(self,rootWidget) : 
        """
            Permet de supprimer tous les objets du conteneur passé en paramètres
        """
        for widget in rootWidget.winfo_children() :
            if isinstance(widget, MenuBar) != True:
                widget.pack_forget()

if __name__.endswith('__main__'):

    # lancement de l'application
    myWindow = Tk()
    myWindow.title("MyRenamingApp")
    MyRenomerApp(myWindow)
    myWindow.mainloop()