
# -*- coding: utf-8 -*-
import re
# utilitaires maison pour l'incrémentation des amorces et la vérification de la validité des noms de fichier

def increment(amorce, nb) :
    """
        permet de réaliser l'incrémentation à partir du amorce
        amorce numérique 
        amorce alphabétique
        retourne une liste contenant les différentes valeurs
        >>> increment('abc',10)
        ['abc', 'abd', 'abe', 'abf', 'abg', 'abh', 'abi', 'abj', 'abk', 'abl']
        >>> increment('azz',3)
        ['azz', 'baa', 'bab']
        >>> increment('ZZZ',10)     #in case of out of range error. 
        False
        >>> increment('aZ9',5)
        ['aZ9', 'bA0', 'bA1', 'bA2', 'bA3']
    """

    count = 1
    charList = []
    resultList = []
    resultList.append(amorce)

    for char in amorce :
        charList.append(char)

    outOfRange = False

    while count < nb  : 
     
        index = 1    
        result = nextChar(charList[-index])
        charList[-index] = result[0]

        while result[1] :
            index += 1
            if index <= len(charList) :
                result = nextChar(charList[-index])      
                charList[-index] = result[0]
            else :
                outOfRange = True      
                break            

        if(outOfRange) :
            break
        else :
            count += 1
            resultList.append(''.join(charList))
   
    if outOfRange :
        return False
    else :
        return resultList

def nextChar(char) :
    """
        Prend un caractère alphanumérique et l'incrémente dans les espaces a-z, A-Z et 0-9
        Retourne un tuple comprent la valeur incrémentée et un boolean à True si on a bouclé
    """
    end = False
    if char.isalpha() :  
        if char.isupper() :
            #ASCII to 65 to 90
            if ord(char)+1 <= 90 :
                char = chr(ord(char)+1)
            else :
                char = 'A'
                end = True
        elif char.islower() :
            #ASCII 97 to 122
            if ord(char)+1 <= 122 :
                char = chr(ord(char)+1)
            else :
                char = 'a'
                end = True
        else :
            print("invalid char")
    elif char.isdigit() :
        #ASCII 48 to 57
        if ord(char)+1 <= 57 :
            char = chr(ord(char)+1)
        else :
            char = '0'
            end = True
    return (char, end)
       
def valid_filename_characters (string) : 
    """
        Vérifie que la chaîne de caractère ne contienne pas de caractères interdits pour les noms de fichiers / dossiers
    """
    forbidden = re.compile(r'[<>:\"\\\/?*]')
    matches = re.findall(forbidden,string)
    if len(matches) != 0 :
        return False
    else :
        return True

if __name__ == '__main__' :
    import doctest
    doctest.testmod()