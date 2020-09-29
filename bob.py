# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:19:42 2020

@author: José
"""


# =============================================================================
# On définit une liste en utilisant différentes fonctions
# =============================================================================
import copy

def creer():
    """ On génère un tableau vide """
    return []

def ajouter_queue(n, t):
    """ insère l'élément n en queue de la liste """
    new_t = copy.deepcopy(t)
    new_t.append(n)
    return new_t

def ajouter_tete(n, t):
    """ insère l'élément n en tête de la liste """
    new_t = copy.deepcopy(t)
    new_t.insert(0, n)
    return new_t

def ajouter_ici(n, i, t):
    """ insère l'élément n à l'indice i dans la liste """
    new_t = copy.deepcopy(t)
    new_t.insert(i, n)
    return new_t

def est_present(element, t):
    """ recherche element dans t """
    for elt in t:
        if elt == element:
            return True
    return False
