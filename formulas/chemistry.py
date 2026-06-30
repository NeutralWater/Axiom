def density(mass, volume):
    return mass / volume


def molarity(moles, liters):
    return moles / liters


def molality(moles, kilograms):
    return moles / kilograms


def dilution(M1, V1, M2=None, V2=None):
    if M2 is None and V2 is not None:
        return (M1 * V1) / V2

    if V2 is None and M2 is not None:
        return (M1 * V1) / M2

    return None


def heat(mass, specific_heat, delta_temp):
    return mass * specific_heat * delta_temp


def specific_heat(q, mass, delta_temp):
    return q / (mass * delta_temp)


def boyles_law(P1, V1, P2=None, V2=None):
    if P2 is None and V2 is not None:
        return (P1 * V1) / V2

    if V2 is None and P2 is not None:
        return (P1 * V1) / P2

    return None


def charles_law(V1, T1, V2=None, T2=None):
    if V2 is None and T2 is not None:
        return (V1 * T2) / T1

    if T2 is None and V2 is not None:
        return (V2 * T1) / V1

    return None


def gay_lussac_law(P1, T1, P2=None, T2=None):
    if P2 is None and T2 is not None:
        return (P1 * T2) / T1

    if T2 is None and P2 is not None:
        return (P2 * T1) / P1

    return None


def combined_gas_law(P1, V1, T1, P2=None, V2=None, T2=None):
    constant = (P1 * V1) / T1

    if P2 is None and V2 is not None and T2 is not None:
        return (constant * T2) / V2

    if V2 is None and P2 is not None and T2 is not None:
        return (constant * T2) / P2

    if T2 is None and P2 is not None and V2 is not None:
        return (P2 * V2) / constant

    return None


def ideal_gas_law(P=None, V=None, n=None, T=None, R=0.0821):
    if P is None and V is not None and n is not None and T is not None:
        return (n * R * T) / V

    if V is None and P is not None and n is not None and T is not None:
        return (n * R * T) / P

    if n is None and P is not None and V is not None and T is not None:
        return (P * V) / (R * T)

    if T is None and P is not None and V is not None and n is not None:
        return (P * V) / (n * R)

    return None