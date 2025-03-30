import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqs

def filtre_passe_bas(R, C):
    """
    Fonction de transfert d'un filtre passe-bas du premier ordre.
    H(s) = 1 / (1 + jRCω)
    """
    num = [1]
    den = [R * C, 1]
    return num, den

def filtre_passe_haut(R, C):
    """
    Fonction de transfert d'un filtre passe-haut du premier ordre.
    H(s) = jRCω / (1 + jRCω)
    """
    num = [R*C, 0]
    den = [R*C, 1]
    return num, den

def tracer_reponse_frequence(num, den, R, C):
    """
    Trace la réponse en fréquence d'un filtre passe-bas :
    - Gain en fonction de la pulsation ω avec indicateur de ω_0 et point à -3dB
    - Phase en fonction de la pulsation ω
    """
    w, h = freqs(num, den, worN=np.logspace(1, 5, 1000))  # ω = pulsation (rad/s)
    phase = np.angle(h, deg=True)  # Phase en degrés
    gain_db = 20 * np.log10(abs(h))  # Gain en dB

    # Calcul de la pulsation de coupure
    omega_c = 1 / (R * C)  # Pulsation de coupure ωc (rad/s)
    gain_c = -3  # Niveau de coupure à -3 dB

    # Trouver l'indice correspondant à ω_c le plus proche
    idx_c = np.argmin(np.abs(w - omega_c))
    gain_at_wc = gain_db[idx_c]  # Devrait être proche de -3 dB

    # Génération de l'asymptote du gain
    w_asymptote = np.array([max(w), omega_c, min(w)])
    gain_asymptote = np.array([0, 0, 20 * np.log10(w_asymptote[2] / omega_c)])

    # Tracé du gain en fonction de la pulsation
    plt.figure(figsize=(7, 4))
    plt.semilogx(w, gain_db, label='Gain réel')
    plt.semilogx(w_asymptote, gain_asymptote, '--r', label='Asymptote')

     # Ajouter la ligne verticale pour ω_c (plus fine)
    plt.axvline(omega_c, color='g', linestyle='--', linewidth=0.9, label=r'$\omega_c$')

    # Ajouter le point (-3 dB, ω_c)
    plt.plot(omega_c, gain_c, 'bx', label=r'Point à -3 dB')

    # Annotation de ω_c sous l'axe des abscisses
    #plt.text(omega_c, plt.ylim()[0], r'$\omega_c$', fontsize=12, color='g', ha='right', va='bottom')

    # Annotation pente a 20 dB/dec
    plt.text(10**2, -23, r'$20\,dB.s^{-1}$', fontsize=10, color='r', ha='left', va='top')


    plt.xlabel('Pulsation ω (rad/s)')
    plt.ylabel('Gain (dB)')
    plt.title('Diagramme de Bode - Gain')
    plt.grid(which='both')
    plt.legend(loc="lower right")
    
    # Sauvegarde du graphique du gain
    plt.savefig(rf'Physique/Electricité/bode diagrams/filtre_passe_haut_gain.png', dpi=300)
    plt.show()

    # Tracé de la phase en fonction de la pulsation
    plt.figure(figsize=(7, 4))
    plt.semilogx(w, phase, 'r', label='Phase')

    # Ajouter la ligne verticale pour ω_c
    plt.axvline(omega_c, color='g', linestyle='--', linewidth=0.9, label=r'$\omega_c$')

    plt.xlabel('Pulsation ω (rad/s)')
    plt.ylabel('Phase (degrés)')
    plt.title('Diagramme de Bode - Phase')
    plt.grid(which='both')
    plt.legend()
    
    # Sauvegarde du graphique de la phase
    plt.savefig(rf'Physique/Electricité/bode diagrams/filtre_passe_haut_phase.png', dpi=300)
    plt.show()



# filtre passe haut

R, C = 1000, 1e-6  # Résistance en ohms, Capacité en farads
num, den = filtre_passe_haut(R, C)
tracer_reponse_frequence(num, den, R, C)


# filtre passe bas
""""
R, C = 1000, 1e-6  # Résistance en ohms, Capacité en farads
num, den = filtre_passe_bas(R, C)
tracer_reponse_frequence(num, den, R, C)"""

"""""
# diagramme vide 
plt.figure(figsize=(7, 4))
plt.xscale('log')
plt.xlim(6, 1.5e5)
plt.ylim(-3, 93)
plt.xlabel(r'Pulsation $\omega$ (rad/s)')
plt.ylabel('Phase (degrés)')
plt.title('Diagramme de Bode - Phase')
plt.grid(which='both')

# Sauvegarde du graphique du gain
plt.savefig(rf'Physique/Electricité/bode diagrams/bode_phase.png', dpi=300)
plt.show()
"""
