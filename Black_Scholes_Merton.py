#BLACK-SCHOLES-MERTON OPTION PRICING MODEL


import numpy as np
from scipy.stats import norm


'''
Black-Scholes Formula for European Options

Call Option Price:
    C = S • N(d₁) − K • e^(−rT) • N(d₂)

Put Option Price:
    P = K • e^(−rT) • N(−d₂) − S • N(−d₁)

Where:
    d₁ = [ln(S / K) + (r + ½•σ²)•T] / (σ•√T)
    d₂ = d₁ − σ•√T

Parameters:
    S  = Current Stock Price
    K  = Strike Price
    T  = Time to Maturity (in years)
    r  = Risk-Free Interest Rate
    σ  = Volatility (Standard Deviation of Returns)
    N(·) = Cumulative Distribution Function of the Standard Normal Distribution
'''


S = _ #Replace the underscore with the Current Stock Price.
K = _ #Replace the underscore with the Strike Price.
T = _ #Replace the underscore with the time to maturity in % of year.
r = _ #Replace the underscore with the Risk Free Interest Rate.
σ = _ #Replace the underscore with the Standard Deviation.

def black_scholes_merton_call(S, K, T, r, σ):
    d1 = (np.log(S / K) + (r + 0.5 * σ**2) * T) / (σ * np.sqrt(T))
    d2 = d1 - σ * np.sqrt(T)
    call_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price

def black_scholes_merton_put(S, K, T, r, σ):
    d1 = (np.log(S / K) + (r + 0.5 * σ**2) * T) / (σ * np.sqrt(T))
    d2 = d1 - σ * np.sqrt(T)
    put_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put_price

print(black_scholes_merton_call(S, K, T, r, σ))
print(black_scholes_merton_put(S, K, T, r,σ))


#IMPORTANT - This code will show error until the underscores are filled.
