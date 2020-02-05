import os
import numpy as np
import scipy.constants as c
from scipy.stats import linregress
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("lab1.csv")
df = df[df["Direction"] == " P"]
R = df["R"]
I = df["I"]
I_e = df["I_e"]
V = df["V"]
V_e = df["V_e"]

print(df)

N = 72 # Coils
a = 0.33 # Radius of coil
Be = 36.11e-6 # [T]
Bh = (8*c.mu_0*N*I)/((125)**(1/2)*a)
x = (R**2*(Be + Bh)**2)/2
e_m = V/x
e_m_actual = 1.758820e11
error = (e_m - e_m_actual)/e_m_actual

print(e_m, error)

plt.figure(figsize=(10,5))
plt.plot(x, V, ".")
#plt.errorbar(x, V, I_e, I_e, "r-o", ecolor="blue", capsize=10)
#plt.xscale("log")
#plt.yscale("log")
plt.title("Collector Curve for $I_b$")
plt.xlabel("$V_{ce}~[V]$")
plt.ylabel("$I_{c}~[A]$")
plt.grid()
plt.tight_layout()
plt.savefig("lab1_1")

m, b, r_value, p_value, std_err = linregress(x, V)

error = 100*(m - e_m_actual)/e_m_actual
print(error)