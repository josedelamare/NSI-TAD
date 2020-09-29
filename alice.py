# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:19:42 2020

@author: José
"""

# =============================================================================
# On définit une liste en utilisant différentes fonctions
# =============================================================================

def creer():
    """ On génère un tableau vide """
    return []

def ajouter_queue(n, t):
    """ insère l'élément n en queue de la liste """
    if len(t) == 0:
        new_t = [n]
    else:
        new_t = (len(t)+1)*[None]
        for i in range(0, len(t), 1):
            new_t[i] = t[i]
        new_t[len(t)] = n
    return new_t

def ajouter_tete(n, t):
    """ insère l'élément n en tête de la liste """
    if len(t) == 0:
        new_t = [n]
    else:
        new_t = t + [None]
        for i in range(len(t)-1, -1, -1):
            new_t[i+1] = t[i]
        new_t[0] = n
    return new_t

def ajouter_ici(n, i, t):
    """ insère l'élément n à l'indice i dans la liste """
    if len(t) == 0:
        new_t = [n]
    else:
        new_t = t + [None]
        for j in range(len(t)-1, i-1, -1):
            new_t[j+1] = t[j]
        new_t[i] = n
    return new_t

def est_present(element, t):
    """ recherche element dans t """
    for elt in t:
        if elt == element:
            return True
    return False
