
# -*- coding: utf-8 -*-


class Regle : 
    """
        Permet de créer une règle de renommage
    """
    def __init__(self,amorce='aucune',apartirde='', prefixe='',postfixe='',nomFichier=True,extensions=[]) :
        '''
            Constructeur de la classe
            Prend en paramètre les différentes variables d'une Règle : type d'amorce, valeur initiale de l'amorce, préfixe, nom personnalisé, suffixe, extensions concernées
        '''
        self.amorce = amorce                        # Aucun, lette ou chiffre | amorce de renommage
        self.apartirde = apartirde                  # texte
        self.prefixe = prefixe                      # texte
        self.postfixe = postfixe                    # texte
        self.nomFicher = nomFichier                 # True or String
        self.extensions = extensions                # liste ou dictionnaire ou set. 

    def __str__(self) :
        return "Class : Regle. Type d'amorce : {}, début d'amorce : {}, préfixe : {}, postfixe : {}, nom du fichier : {}, extensions : {}".format(
                self.amorce, self.apartirde, self.prefixe, self.postfixe, self.nomFicher, self.extensions)

    # getters

    def get_amorce(self) :
        return self.amorce

    def get_apartide(self) :
        return self.apartirde 

    def get_prefixe(self) :
        return self.prefixe

    def get_postfixe(self) :
        return self.postfixe

    def get_nomFichier(self) :
        return self.nomFicher

    def get_extensions(self) :
        return self.extensions

    # setters

    def set_amorce(self, amorce) :
        self.amorce = amorce
        return self.amorce

    def set_apartirde(self, apartirde) :
        self.apartirde = apartirde
        return self.apartirde 

    def set_prefixe(self, prefixe) :
        self.prefixe = prefixe
        return self.prefixe

    def set_postfixe(self, postfixe) :
        self.postfixe = postfixe
        return self.postfixe

    def set_nomFichier(self, nomFichier) :
        self.nomFicher = nomFichier
        return self.nomFicher

    def set_extensions(self, extensions) :
        self.extensions = extensions
        return self.extensions