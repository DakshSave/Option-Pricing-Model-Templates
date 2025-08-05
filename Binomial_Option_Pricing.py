#BINOMIAL OPTION PRICING MODEL


import numpy as np


'''
Binomial Tree Formula

Call Option:
    C = max(S − K, Discounted Expected Value from Next Step)

Put Option:
    P = max(K − S, Discounted Expected Value from Next Step)

Parameters:
    S  = Current Stock Price
    K  = Strike Price
    T  = Time to Maturity (in % of years)
    r  = Risk-Free Interest Rate
    σ  = Volatility (Standard Deviation of Returns)
    n  = Number of time steps in the binomial tree
'''


S = _   # Replace the underscore with the Current Stock Price.
K = _   # Replace the underscore with the Strike Price.
T = _   # Replace the underscore with the Time to Maturity (in % of years).
r = _   # Replace the underscore with the Risk-Free Interest Rate.
σ = _   # Replace the underscore with the Volatility (Standard Deviation).
n = _   # Replace the underscore with the Number of Steps in the Tree.


def binomial_call(S, K, T, r, σ, n):
    dt = T / n
    u = np.exp(σ * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)
    disc = np.exp(-r * dt)

    ST = np.array([S * u**j * d**(n - j) for j in range(n + 1)])
    option = np.maximum(0, ST - K)

    for i in range(n - 1, -1, -1):
        ST = ST[:i+1] / u
        option = disc * (p * option[1:] + (1 - p) * option[:-1])
        option = np.maximum(option, ST - K) 

    return option[0]

def binomial_put(S, K, T, r, σ, n):
    dt = T / n
    u = np.exp(σ * np.sqrt(dt))
    d = 1 / u
    p = (np.exp(r * dt) - d) / (u - d)
    disc = np.exp(-r * dt)

    ST = np.array([S * u**j * d**(n - j) for j in range(n + 1)])
    option = np.maximum(0, K - ST)

    for i in range(n - 1, -1, -1):
        ST = ST[:i+1] / u
        option = disc * (p * option[1:] + (1 - p) * option[:-1])
        option = np.maximum(option, K - ST)  
        
    return option[0]

print(binomial_call(S, K, T, r, σ, n))
print(binomial_put(S, K, T, r, σ, n))


# IMPORTANT - This code will show error until the underscores are filled.
