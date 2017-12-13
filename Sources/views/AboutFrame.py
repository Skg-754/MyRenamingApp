from tkinter import *

class AboutFrame(Frame):
    '''
        Frame : Contient la page "ABOUT", 
        Affiche le nom du concepteur du logiciel, la version
    '''
    def __init__(self, root) :

        Frame.__init__(self, root)
        self.build()

    def build(self) :
        '''
            Création et mise en place de tous les widgets de la page
        '''
        titleLabel = Label(self, text="MyRenamingApp")
        versionLabel = Label(self, text="v0.0.0.0.0.0.0.0.0.1")
        authorLabel = Label(self, text="Developped by Simon Grosz")

        titleLabel.pack()
        versionLabel.pack()
        authorLabel.pack()