import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


# Constantes du système

R = 2.07  # Ohms
Kt = 13.9e-3  # Nm/A
Ke = 1/(np.pi*689/30)
Jeq = 13.6e-7  # kgm²
# Modélisation de la fonction de transfert
ft = signal.lti([1/Ke], [R*Jeq/(Ke*Kt), 1])

# Calcul du diagramme de Bode
omega = np.logspace(0.8, 3.4, 1000)
w, mag, phase = signal.bode(ft, w=omega)


# Calcul des éléments caractéristiques de la fonction
# Pente finale
# On cherche les valeurs de la dernière décade
amp = mag[np.where(w >= w[-1]/10)]
print("Pente en dB :", amp[-1]-amp[0])  # Afichage de la pente en dB

# Pulsation de coupure
wc = w[np.where(mag <= mag[0]-3)][0]
print("Pulsation de coupure (rad/s):", wc)

# Calcul de l'asymptote
# Pente avec omega en échelle logarithmique
a = (mag[-2]-mag[-1])/(np.log(w[-2])-np.log(w[-1]))
# Pulsation de coupure en échelle logarithmique
x1 = np.log(w[-1])  # Recherche de la valeur de la pulsation de coupure
b = mag[-1]-a*x1
# Valeurs de la tangente
asymp = a*np.log(w)+b
# On limite les valeurs à partir de la pulsation de coupure
asymp = asymp[np.where(mag <= mag[0]-3)]
omega_t = w[np.where(mag <= mag[0]-3)]


# Affichage
fig, ax = plt.subplots()
plt.subplot(211)
plt.title('Diagrammes de Bode')
plt.semilogx(w, mag, lw=2)    # Amplitude
plt.plot([0, wc], [mag[0], mag[0]], color="red",
         lw=0.8)  # Asymptote horizontale
plt.axvline(x=wc, color="orange")
plt.plot(omega_t, asymp, color="red", lw=0.8)  # Asymptote oblique
#plt.xlabel('Pulsation (rad/s)')
plt.ylabel('Amplitude (dB)')
# On force l'affichage des valeurs extrèmes
plt.yticks(np.linspace(mag[0], mag[-1], 5))
plt.grid(which='both')

plt.subplot(212)
plt.semilogx(w, phase)  # Phase
plt.xlabel('Pulsation (rad/s)')
plt.ylabel('Phase (deg)')
plt.yticks(np.linspace(phase[0], phase[-1], 5))  # On force l'affichage de -90
plt.axvline(x=wc, color="orange")  # Pulsation de coupure
plt.grid(which='both')

plt.tight_layout()  # Ajuster le placement des courbes
plt.savefig("Physique/Electricité/fig/bode.pdf")
plt.show()