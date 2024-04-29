def inverse(chaine):
    if isinstance(chaine,int):
        raise ValueError("Vous devez passer une chaine de caractères")
    for element in chaine:
        if not isinstance(element,str) :
            raise ValueError("Vous devez passer une chaine de caractères")
    if len(chaine)==4 and isinstance(chaine,list):
         chaine.pop()
         
    chaine="".join(chaine)
    return chaine[::-1]

if __name__== "__main__": # si j'execute ce fichier directement et non par import
    print(inverse(["a","b","c","d"]))
    print(inverse(["a","b",0,"d"]))
    print(inverse(["hello"]))
    