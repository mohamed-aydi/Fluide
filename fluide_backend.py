"""Fluide.ENIS - backend Python (version simple, pour la présentation).

Trois problèmes, trois fonctions. Aucune bibliothèque à installer.
Lancer :  python fluide_backend.py
"""
import math

G = 9.81  # accélération de la pesanteur (m/s²)

# Diamètres commerciaux indicatifs (mm)
DN_MM = [20, 25, 32, 40, 50, 63, 75, 90, 110, 125, 160, 200, 250, 315, 400, 500]


def vanne_circulaire(D, yg, rho=1000):
    """Problème 1 : poussée sur une vanne circulaire verticale immergée.
    D = diamètre (m), yg = profondeur du centre (m), rho = masse volumique (kg/m3)."""
    A = math.pi * D**2 / 4            # aire (m²)
    F = rho * G * yg * A              # poussée (N)
    I = math.pi * D**4 / 64           # inertie centrale (m4)
    yp = yg + I / (yg * A)            # centre de poussée (m)
    return {"A": A, "F": F, "I": I, "yp": yp}


def pression_plongeur(h, rho=1030, patm=101300):
    """Problème 2 : pression subie par un plongeur.
    h = profondeur (m), rho = masse volumique (kg/m3), patm = pression atmosphérique (Pa)."""
    p_rel = rho * G * h               # pression relative (Pa)
    return {"p_rel": p_rel, "p_abs": patm + p_rel}


def conduite_remplissage(V, t_heures, vmax):
    """Problème 3 : diamètre d'une conduite de remplissage.
    V = volume (m3), t_heures = durée (h), vmax = vitesse maximale (m/s)."""
    Q = V / (t_heures * 3600)         # débit (m3/s)
    A = Q / vmax                      # section minimale (m²)
    D = math.sqrt(4 * A / math.pi)    # diamètre minimal (m)
    dn = next(d for d in DN_MM if d / 1000 >= D)   # diamètre commercial supérieur
    v_reelle = Q / (math.pi * (dn / 1000) ** 2 / 4)
    return {"Q": Q, "A": A, "D": D, "DN_mm": dn, "v_reelle": v_reelle}


if __name__ == "__main__":
    print("1 = Vanne circulaire   2 = Plongeur   3 = Conduite de remplissage")
    choix = input("Votre choix : ")
    if choix == "1":
        D = float(input("Diamètre D (m) : "))
        yg = float(input("Profondeur du centre yG (m) : "))
        print(vanne_circulaire(D, yg))
    elif choix == "2":
        h = float(input("Profondeur h (m) : "))
        print(pression_plongeur(h))
    elif choix == "3":
        V = float(input("Volume V (m3) : "))
        t = float(input("Durée (h) : "))
        vmax = float(input("Vitesse maximale (m/s) : "))
        print(conduite_remplissage(V, t, vmax))
    else:
        print("Choix inconnu.")
