# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.ttk import *
from ListeRegles import *

class RuleFrame(Frame):
    '''
        Frame : Contient la formulaire permettant de créer une règle de renomamge
    '''

    def __init__(self, root) :

        Frame.__init__(self, root)

        # Valeurs des différents forumalaires
        self.amorceVal = StringVar()
        self.apartirdeVal = StringVar()
        self.prefixeVal = StringVar()
        self.modeFichierVal = IntVar()
        self.nomFicherVal = StringVar()
        self.postfixeVal = StringVar()
        self.extensionsVal = StringVar()

        self.build()

    def build(self) :
        '''
            Création et mise en place de tous les widgets de la page
        '''
        # amorce List "Aucun, chiffre, lettre"
        amorceListLabel = Label(self, text="Amorce")
        amorceListChoices = ('aucune','chiffre','lettre')
        self.amorceListInput = Combobox(self, textvariable=self.amorceVal, values=amorceListChoices, state='readonly', width=10) 
        self.amorceListInput.current(0)
        amorceListLabel.grid(row=1,column=2)
        self.amorceListInput.grid(padx=5,pady=(0,10),row=2,column=2)

        # amorce Form "A partir de"
        amorceLabel = Label(self, text="A partir de")
        self.amorceInput = Entry(self, textvariable=self.apartirdeVal, width=10)
        amorceLabel.grid(row=3,column=2)
        self.amorceInput .grid(padx=5,pady=(0,10),row=4,column=2)


        # prefixe
        prefixeLabel = Label(self,text="Préfixe")
        self.prefixeInput = Entry(self,textvariable=self.prefixeVal, width=10)
        prefixeLabel.grid(row=1,column=3)
        self.prefixeInput.grid(padx=5, pady=(0,10), row=2,column=3)

        # Fichier
        fichierLabel = Label(self,text="Nom du Fichier")
        fichierBtn1 = Radiobutton(self, text="   Nom Original", variable=self.modeFichierVal, value=0)
        fichierBtn2 = Radiobutton(self, text=" ", variable=self.modeFichierVal, value=1)
        self.fichierInput = Entry(self, textvariable=self.nomFicherVal, width=10)
        fichierLabel.grid(padx=5,row=1,column=4, columnspan = 2)
        fichierBtn1.grid(padx=5,row=2,column=4,columnspan = 2)
        fichierBtn2.grid(padx=(5,0),row=3,column=4)
        self.fichierInput.grid(row=3,column=5)

        # Sufixe
        postLabel = Label(self,text="Postfixe")
        self.postInput = Entry(self,textvariable=self.postfixeVal, width=10)
        postLabel.grid(row=1,column=6)
        self.postInput.grid(padx=5, pady=(0,10), row=2,column=6)

        # Extensions
        extLabel = Label(self,text="Extensions Concernées")
        self.extInput = Entry(self,textvariable=self.extensionsVal, width=10)
        extLabel.grid(row=1,column=7)
        self.extInput.grid(padx=5, pady=(0,10), row=2,column=7)

    def loadRule(self, name) :
        '''
            Permet de charger la règle dont le nom est en paramètre et de remplir le formulaire en fonction
        '''

        listeRegles = ListeRegles()
        rule = listeRegles.get_rule(name)

        if rule.get_amorce() == 'chiffre' :
            self.amorceListInput.current(1)
        elif rule.get_amorce() == 'lettre' :
            self.amorceListInput.current(2)
        elif rule.get_amorce() == 'aucun' :
            self.amorceListInput.current(0)

        self.amorceInput.delete(0,'end')
        self.amorceInput.insert(0,rule.get_apartide())

        self.prefixeInput.delete(0,'end')
        self.prefixeInput.insert(0,rule.get_prefixe())

        self.fichierInput.delete(0,'end')
        if isinstance(rule.get_nomFichier(),str) :
           
            self.fichierInput.insert(0,rule.get_prefixe())
            self.modeFichierVal.set(1)
        else :
            self.modeFichierVal.set(0)

        self.postInput.delete(0,'end')
        self.postInput.insert(0,rule.get_postfixe())

        if rule.get_extensions() :
            ext = ''
            for extension in rule.get_extensions() :
                ext += extension+', '
            ext = ext[:-2]
            self.extInput.delete(0,'end')
            self.extInput.insert(0,ext)


    def get_allInputs(self) : 
        """
            Retourne un dictionnaire contenant toutes les variables input du formulaire
        """
        allInput = {}
        allInput['amorce'] = self.amorceVal
        allInput['apartirde'] = self.apartirdeVal
        allInput['prefixe'] = self.prefixeVal
        allInput['modeFichier'] = self.modeFichierVal
        allInput['nomFichier'] = self.nomFicherVal
        allInput['postfixe'] = self.postfixeVal
        allInput['extensions'] = self.extensionsVal
        
        return allInput
