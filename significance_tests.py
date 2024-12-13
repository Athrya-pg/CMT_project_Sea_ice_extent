# ================================================================================================
# Description: This script is used  to perform F-test and t-test to determine the significance of the regression coefficients.
# ================================================================================================

import numpy as np
import pandas as pd
import scipy.stats as stats

data_folder = 'outputs/'

# Load residuals from residuals.csv
data = pd.read_csv(data_folder + 'residuals.csv', delimiter = ',')
residuals_North = data['Residual_North'].values
residuals_South = data['Residual_South'].values

# Load variables in coefficients.txt
# Read linear regression coefficients from the text file
coefficients = {}
with open(data_folder + 'coefficients.txt', 'r') as f:
    for line in f:
        name, value = line.split('=')
        coefficients[name.strip()] = float(value.strip())

# Coefficients for the North model
mN = coefficients['mN']
bN = coefficients['bN']
# Coefficients for the South model
b0 = coefficients['b0']
b1 = coefficients['b1']
b2 = coefficients['b2']
b3 = coefficients['b3']

# Number of observations and coefficients
n = len(residuals_North) 
kN = 2  # (inclut l'intercept)
kS = 4 
# Calculer la somme des carrés des résidus (SSE)
SSE_nh = np.sum(residuals_North**2)
SSE_sh = np.sum(residuals_South**2)

# SST : Somme totale des carrés (nécessite y observé)
yN_data = pd.read_csv(data_folder + 'NH_Data.csv', delimiter= ',')  # Charger y observé
yN = yN_data['Sea_Ice_Extent'].values
yN_mean = np.mean(yN)
SST_nh = np.sum((yN - yN_mean)**2)

yS_data = pd.read_csv(data_folder + 'SH_Data.csv', delimiter= ',')  # Charger y observé
yS = yS_data['Sea_Ice_Extent'].values
yS_mean = np.mean(yS)
SST_sh = np.sum((yS - yS_mean)**2)

# SSR : Somme des carrés expliquée
SSR_nh = SST_nh - SSE_nh
SSR_sh = SST_sh - SSE_sh

# Degrés de liberté
df_model_nh = kN - 1
df_residuals_nh = n - kN

df_model_sh = kS - 1
df_residuals_sh = n - kS

# Statistique F for the North model
F_stat_nh = (SSR_nh / df_model_nh) / (SSE_nh / df_residuals_nh)
f_p_value_nh = 1 - stats.f.cdf(F_stat_nh, df_model_nh, df_residuals_nh)
print(f"F-statistic (NH): {F_stat_nh: .4f}, p-value: {f_p_value_nh: .4e}")

#Calculer l'erreur standard des coefficients for the North model
x_nh = yN_data['CO2'].values
MSE_nh = SSE_nh / df_residuals_nh
se_mN = np.sqrt(MSE_nh / np.sum((x_nh - np.mean(x_nh))**2))
se_bN = np.sqrt(MSE_nh * (1/n + np.mean(x_nh)**2 / np.sum((x_nh - np.mean(x_nh))**2)))

# Calculer les statistiques t et les p-valeurs pour les coefficients
t_value_mN = mN / se_mN
t_value_bN = bN / se_bN
p_value_mN = 2 * (1 - stats.t.cdf(np.abs(t_value_mN), df_residuals_nh))
p_value_bN = 2 * (1 - stats.t.cdf(np.abs(t_value_bN), df_residuals_nh))

print(f"Coefficient mN (NH): t-value = {t_value_mN}, p-value = {p_value_mN: .4e}")
print(f"Coefficient bN (NH): t-value = {t_value_bN}, p-value = {p_value_bN: .4e}")

#-------------------------------------------------------------------------------

# Statistique F for the South model
F_stat_sh = (SSR_sh / df_model_sh) / (SSE_sh / df_residuals_sh)
f_p_value_sh = 1 - stats.f.cdf(F_stat_sh, df_model_sh, df_residuals_sh)
print(f"F-statistic (SH): {F_stat_sh: .4f}, p-value: {f_p_value_sh: .4e}")

# mmm
#Calculer l'erreur standard des coefficients for the South model
MSE_sh = SSE_sh / df_residuals_sh
X_sh = yS_data[['CO2', 'Temperature', 'Precipitation']].values
X_sh = np.hstack((np.ones((X_sh.shape[0], 1)), X_sh)) #pas sûr
XTX_inv_sh = np.linalg.inv(X_sh.T @ X_sh)
se_sh = np.sqrt(MSE_sh * np.diag(XTX_inv_sh))  # Erreurs standards des coefficients

# Calculer les statistiques t et les p-valeurs pour les coefficients
t_values_sh = np.array([b0, b1, b2, b3]) / se_sh
p_values_sh = 2 * (1 - stats.t.cdf(np.abs(t_values_sh), df_residuals_sh))

# Afficher les résultats pour le pôle Sud
for i, (t_val, p_val) in enumerate(zip(t_values_sh, p_values_sh)):
    print(f"Coefficient b{i} (SH): t-value = {t_val:.4f}, p-value = {p_val:.4e}")