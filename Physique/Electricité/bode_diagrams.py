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
    w_asymptote = np.array([min(w), omega_c, max(w)])
    gain_asymptote = np.array([0, 0, -20 * np.log10(w_asymptote[2] / omega_c)])

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

    plt.xlabel('Pulsation ω (rad/s)')
    plt.ylabel('Gain (dB)')
    plt.title('Réponse en fréquence - Gain')
    plt.grid(which='both')
    plt.legend()
    
    # Sauvegarde du graphique du gain
    plt.savefig(rf'Physique/Electricité/bode diagrams/filtre_passe_bas_gain.png', dpi=300)
    plt.show()

    # Tracé de la phase en fonction de la pulsation
    plt.figure(figsize=(7, 4))
    plt.semilogx(w, phase, 'r', label='Phase')

    # Ajouter la ligne verticale pour ω_c
    plt.axvline(omega_c, color='g', linestyle='--', linewidth=0.9, label=r'$\omega_c$')

    plt.xlabel('Pulsation ω (rad/s)')
    plt.ylabel('Phase (degrés)')
    plt.title('Réponse en fréquence - Phase')
    plt.grid(which='both')
    plt.legend()
    
    # Sauvegarde du graphique de la phase
    plt.savefig(rf'Physique/Electricité/bode diagrams/filtre_passe_bas_phase.png', dpi=300)
    plt.show()

# Exemple d'utilisation
R, C = 1000, 1e-6  # Résistance en ohms, Capacité en farads
num, den = filtre_passe_bas(R, C)
tracer_reponse_frequence(num, den, R, C)
