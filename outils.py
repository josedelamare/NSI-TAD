import matplotlib.pyplot as plt
import time
import bob
import alice

def trace_est_present(n):
    """Fonction permettant de comparer le temps d'exécution de la fonction est_present"""
    liste_temps_bob = n*[0]
    liste_temps_alice = n*[0]
    liste_n = [i for i in range(1, n+1, 1)]
    for i in range(1, n+1, 1):
        t = bob.creer()
        for j in range (0, i, 1):
            bob.ajouter_tete(j, t)
        debut = 1000000*time.time()
        bob.est_present(n-1, t)
        fin = 1000000*time.time()
        liste_temps_bob[i-1] = fin - debut
    for i in range(1, n+1, 1):
        t = alice.creer()
        for j in range (0, i, 1):
            alice.ajouter_tete(j, t)
        debut = 1000000*time.time()
        alice.est_present(n-1, t)
        fin = 1000000*time.time()
        liste_temps_alice[i-1] = fin - debut
    plt.plot(liste_n, liste_temps_bob, 'bo', label='implémentation utilisant la méthode de Bob')
    plt.plot(liste_n, liste_temps_alice, 'ro', label='implémentation utilisant la méthode d"Alice')
    plt.legend(loc='upper left')
    plt.show()
    
def trace_ajout_tete(n):
    """Fonction permettant de comparer le temps d'exécution de la fonction creer_tete"""
    liste_temps_bob = n*[0]
    liste_temps_alice = n*[0]
    liste_n = [i for i in range(1, n+1, 1)]
    for i in range(1, n+1, 1):
        t = bob.creer()
        debut = 1000000*time.time()
        for j in range (0, i, 1):
            bob.ajouter_tete(j, t)
        fin = 1000000*time.time()
        liste_temps_bob[i-1] = fin - debut
    for i in range(1, n+1, 1):
        t = alice.creer()
        debut = 1000000*time.time()
        for j in range (0, i, 1):
            alice.ajouter_tete(j, t)
        fin = 1000000*time.time()
        liste_temps_alice[i-1] = fin - debut
    plt.plot(liste_n, liste_temps_bob, 'bo', label='implémentation utilisant la méthode de Bob')
    plt.plot(liste_n, liste_temps_alice, 'ro', label='implémentation utilisant la méthode d"Alice')
    plt.legend(loc='upper left')
    plt.show()
    
def trace_ajout_queue(n):
    """Fonction permettant de comparer le temps d'exécution de la fonction creer_queue"""
    liste_temps_bob = n*[0]
    liste_temps_alice = n*[0]
    liste_n = [i for i in range(1, n+1, 1)]
    for i in range(1, n+1, 1):
        t = bob.creer()
        debut = 1000000*time.time()
        for j in range (0, i, 1):
            bob.ajouter_queue(j, t)
        fin = 1000000*time.time()
        liste_temps_bob[i-1] = fin - debut
    for i in range(1, n+1, 1):
        t = alice.creer()
        debut = 1000000*time.time()
        for j in range (0, i, 1):
            alice.ajouter_queue(j, t)
        fin = 1000000*time.time()
        liste_temps_alice[i-1] = fin - debut
    plt.plot(liste_n, liste_temps_bob, 'bo', label='implémentation utilisant la méthode de Bob')
    plt.plot(liste_n, liste_temps_alice, 'ro', label='implémentation utilisant la méthode d"Alice')
    plt.legend(loc='upper left')
    plt.show()    
