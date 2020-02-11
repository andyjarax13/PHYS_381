import os
import numpy as np
import scipy.constants as c
from scipy.stats import linregress
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("lab1.csv")
df = df[df["Direction"] == " A"]
df_A = df[df["Direction"] == " A"]
df_P = df[df["Direction"] == " P"]

R = df["R"]
R_A = df_A["R"]
R_P = df_P["R"]

I = df["I"]
I_A = df_A["I"]
I_P = df_P["I"]

I_e = df["I_e"]*2
I_e_A = df_A["I_e"]
I_e_P = df_P["I_e"]

V = df["V"]
V_A = df_A["V"]
V_P = df_P["V"]

V_e = df["V_e"]*30
V_e_A = df_A["V_e"]
V_e_P = df_P["V_e"]

N = 72 # Coils
a = 0.33 # Radius of coil
Be = -36.11e-6 # [T]
Be_e = 2e-6
Bh = (8*c.mu_0*N*I)/((125)**(1/2)*a)
x = (R**2*(Be + Bh)**2)/2
x_e = (   (I_e**2)*(R**2*(Bh/I)*(Bh+Be))**2 + (Be_e**2)*(R**2*(Bh+Be))**2   )**(1/2)
e_m = V/x
e_m_actual = 1.758820e11
error = (e_m - e_m_actual)/e_m_actual

print(e_m, error)

m, b, r_value, p_value, std_err = linregress(x, V)
print(type(m))


linear = m * np.linspace(min(x), max(x), len(x)) + b
x2 = np.linspace(min(x), max(x), len(x))

plt.figure(figsize=(10,5))
plt.plot(x2, linear, "g")
plt.errorbar(x, V, V_e, x_e, ".r", ecolor="blue", capsize=0)
#plt.xscale("log")
#plt.yscale("log")
plt.title("Collector Curve for $I_b$")
plt.xlabel("$x_{ce}~[V]$")
plt.ylabel("$V_{accel}~[V]$")
plt.grid()
plt.tight_layout()
plt.savefig("lab1_1")



error = 100*(m - e_m_actual)/e_m_actual
print(error)
print(linregress(x, V))