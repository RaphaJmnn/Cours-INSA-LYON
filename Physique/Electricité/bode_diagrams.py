import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqs

def filtre_passe_bas(R, C):
    """
    Fonction de transfert d'un filtre passe-bas du premier ordre.
    H(s) = 1 / (1 + sRC)
    """
    num = [1]
    den = [R * C, 1]
    return num, den

def filtre_passe_haut(R, C):
    """
    Fonction de transfert d'un filtre passe-haut du premier ordre.
    H(s) = sRC / (1 + sRC)
    """
    num = [R * C, 0]
    den = [R * C, 1]
    return num, den

def filtre_passe_bande(R1, C1, R2, C2):
    """
    Fonction de transfert d'un filtre passe-bande du premier ordre.
    """
    num = [R2 * C2, 0]
    den = [R1 * C1 + R2 * C2, 1]
    return num, den

def filtre_coupe_bande(R1, C1, R2, C2):
    """
    Fonction de transfert d'un filtre coupe-bande du premier ordre.
    """
    num = [R1 * C1 + R2 * C2, 1]
    den = [R1 * C1 + R2 * C2, 1]
    return num, den

def tracer_reponse_frequence(num, den, R, C):
    """
    Trace la réponse en fréquence du filtre avec la phase et l'asymptote du gain.
    """
    w, h = freqs(num, den, worN=np.logspace(1, 6, 1000))
    phase = np.angle(h, deg=True)
    gain_db = 20 * np.log10(abs(h))
    
    # Calcul de la fréquence de coupure
    fc = 6 / (2 * np.pi * R * C)
    
    # Génération de l'asymptote
    w_asymptote = np.array([min(w), fc, max(w)])
    
    # Adaptation de l'asymptote en fonction du type de filtre
    if num[0] == 1:  # Filtre passe-bas
        gain_asymptote = np.array([0, 0, -20 * np.log10(w_asymptote[2]/fc)])
    else:  # Filtre passe-haut
        gain_asymptote = np.array([-20 * np.log10(fc/w_asymptote[0]), 0, 0])
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 6))
    
    # Tracé du gain
    ax1.semilogx(w, gain_db, label='Gain réel')
    ax1.semilogx(w_asymptote, gain_asymptote, '--r', label='Asymptote')  # Courbe asymptotique en rouge pointillé
    ax1.set_xlabel('Fréquence (Hz)')
    ax1.set_ylabel('Gain (dB)')
    ax1.set_title('Réponse en fréquence - Gain')
    ax1.grid(which='both')
    ax1.legend()
    
    # Tracé de la phase
    ax2.semilogx(w, phase, 'r', label='Phase')
    ax2.set_xlabel('Fréquence (Hz)')
    ax2.set_ylabel('Phase (degrés)')
    ax2.set_title('Réponse en fréquence - Phase')
    ax2.grid(which='both')
    ax2.legend()
    
    plt.tight_layout()
    plt.show()

# Exemple d'utilisation
R, C = 1000, 1e-6  # Résistance en ohms, Capacité en farads
num, den = filtre_passe_haut(R, C)
tracer_reponse_frequence(num, den, R, C)