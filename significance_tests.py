import numpy as np
import pandas as pd
import scipy.stats as stats

# Load residuals from residuals.csv
data = pd.read_csv('outputs/residuals.csv', delimiter = ',')
residuals_North = data['Residual_North'].values
residuals_South = data['Residual_South'].values

# Load variables in coefficients.txt
# Read linear regression coefficients from the text file
coefficients = {}
with open('outputs/coefficients.txt', 'r') as f:
    for line in f:
        name, value = line.split('=')
        coefficients[name.strip()] = float(value.strip())

mN = coefficients['mN']
bN = coefficients['bN']

n = len(residuals_North) # Number of observations
k = len(coefficients)  # Nombre de coefficients dans le modèle (inclut l'intercept)

# Calculer la somme des carrés des résidus (SSE)
SSE = np.sum(residuals_North**2)

# SST : Somme totale des carrés (nécessite y observé)
y_data = pd.read_csv('outputs/sea_ice_nh.csv', delimiter= ',')  # Charger y observé
yN = y_data['NH_Extent'].values
y_mean = np.mean(yN)
SST = np.sum((yN - y_mean)**2)

# SSR : Somme des carrés expliquée
SSR = SST - SSE

# Degrés de liberté
df_model = k - 1
df_residuals = n - k

# Statistique F
F_stat = (SSR / df_model) / (SSE / df_residuals)
f_p_value = 1 - stats.f.cdf(F_stat, df_model, df_residuals)
print(f"F-statistic: {F_stat}, p-value: {f_p_value}")


#Calculer l'erreur standard des coefficients
MSE = SSE / df_residuals
x_data = pd.read_csv('outputs/summed_co2.csv', delimiter = ',')
x = x_data['CO2_Mass'].values
se_mN = np.sqrt(MSE / np.sum((x - np.mean(x))**2))
se_bN = np.sqrt(MSE * (1/n + np.mean(x)**2 / np.sum((x - np.mean(x))**2)))

# Calculer les statistiques t et les p-valeurs pour les coefficients
t_value_mN = mN / se_mN
t_value_bN = bN / se_bN
p_value_mN = 2 * (1 - stats.t.cdf(np.abs(t_value_mN), df_residuals))
p_value_bN = 2 * (1 - stats.t.cdf(np.abs(t_value_bN), df_residuals))

print(f"Coefficient mN: t-value = {t_value_mN}, p-value = {p_value_mN: .4e}")
print(f"Coefficient bN: t-value = {t_value_bN}, p-value = {p_value_bN: .4e}")