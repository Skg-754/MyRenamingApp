# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import filedialog

class HeaderFrame(Frame):
    '''
        Frame : Contient le fomulaire du haut des pages "Renommer" et "Créér une règle"
    '''
    def __init__(self, root, mainTitle, formTitle) :

        Frame.__init__(self, root)
        self.mainTitle = mainTitle
        self.formTitle = formTitle
        self.formVal = StringVar()

        self.build()

    def build(self) :
        '''
            Création et mise en place de tous les widgets de la page
        '''

        #Titre principal
        self.mainTitleLabel = Label(self, text=self.mainTitle)
        self.mainTitleLabel.grid(padx="20",column=2,row=2)

        #Formulaire
        self.formTitleLabel = Label(self,text=self.formTitle)
        self.formTitleLabel.grid(row=1,column=3)

        self.formInput = Entry(self, textvariable=self.formVal)
        self.formInput.grid(row=2,column=3)

        if self.formTitle == 'Nom du répertoire' : 
            formButton = Button(self, text="browse", command=self.browse)
            formButton.grid(row=2,column=4)

        # Image
        logoFile = PhotoImage(file='views/surprised.png')
        logo = Label(self, image=logoFile)
        logo.image = logoFile
        logo.grid(padx=40,row=1,column=5,rowspan=2)
         
    def browse(self) :
        '''
            Fonction permettant de browser un dossier
            Affiche ensuite de résultat dans le champ dossier
        '''
        path = filedialog.askdirectory()
        self.formInput.delete(0,'end')
        self.formInput.insert(0,path)

    def get_formVal(self) :

        return self.formVal

    def set_mainTitle(self, mainTitle) :
        self.mainTitle = mainTitle
        self.mainTitleLabel.configure(text=self.mainTitle)
        return self.mainTitle

    def set_formTitle(self, formTitle) :
        self.formTitle = formTitle
        self.formTitleLabel.configure(text=self.formTitle)
        return self.formTitle
