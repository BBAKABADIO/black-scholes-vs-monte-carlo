# Pricer Black-Scholes : prix exact d'une option européenne (call ou put)

# 1. Imports
import math
from scipy.stats import norm


# 2. Fonction de calcul du prix
def black_scholes_price(S0, K, r, sigma, T, option_type="call"):
    # Vérification des paramètres
    if S0 <= 0 or K <= 0 or sigma <= 0 or T <= 0:
        raise ValueError("S0, K, sigma and T must be strictly positive")

    # Calcul de d1 et d2
    d1 = (math.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    # Prix selon le type d'option
    if option_type == "call":
        return S0 * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    if option_type == "put":
        return K * math.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)

    raise ValueError("option_type must be 'call' or 'put'")


# 3. Test manuel (attendu : environ 10.4506)
if __name__ == "__main__":
    price = black_scholes_price(S0=100, K=100, r=0.05, sigma=0.20, T=1, option_type="call")
    print(f"Black-Scholes call: {price:.4f}")
