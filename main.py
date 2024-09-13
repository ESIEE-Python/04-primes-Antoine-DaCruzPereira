'''
ce module sert utiliser la racine carré de la bibliothèque math
'''

from math import sqrt

#### Fonction secondaire


def isprime(p):
    '''
    Retourne un booléen qui indique si le nombre est un nombre premier ou non.

    Arg:
        p:valeur entière positive

    return:
        Boolean object True or False

    '''
    # votre code ici
    premier = True
    if p in (0,1):
        premier = False
    for d in range(2,int(sqrt(p)+1)):
        if p%d == 0:
            premier = False
    return premier

#### Fonction principale


def main():
    '''
    Test la fonction isprime de 0 à 99

    Arg:
        None

    Return:
        None
    '''
    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
