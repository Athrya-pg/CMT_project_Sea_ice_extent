import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Charger les données (les observations et les prédictions)
observations_nh = pd.read_csv('sea_ice_nh.csv')  # Observation de l'Hémisphère Nord
observations_sh = pd.read_csv('sea_ice_sh.csv')  # Observation de l'Hémisphère Sud
x = pd.read_csv('summed_co2.csv')  # Emissions de CO2
x = x['CO2_Mass']
predictions_nh = pd.read_csv('LinearReg.csv')  # Prédictions de l'Hémisphère Nord
predictions_sh = pd.read_csv('LinearReg.csv')  # Prédictions de l'Hémisphère Sud
print(predictions_nh.head())

y_obs_nh = observations_nh['Annual']  # Observations de l'Hémisphère Nord
y_obs_sh = observations_sh['Annual']  # Observations de l'Hémisphère Nord
y_pred_nh = predictions_nh["Estim_North"]  # Prédictions de l'Hémisphère Nord
y_pred_sh = predictions_sh['Estim_South']  # Prédictions de l'Hémisphère Nord


plt.scatter(x, y_obs_nh, label='Observations', color='blue')  # Afficher les observations
plt.plot(x, y_pred_nh, label='Linear Regression Model', color='red')  # Afficher les prédictions

plt.xlabel('Carbon Dioxide (Gt)', fontsize=12)
plt.ylabel('Ice Surface (million km²)', fontsize=12)
plt.title(' Global CO2 emissions vs Arctic Sea Ice Extent')
plt.legend(loc ='upper right')
plt.grid(True)
plt.savefig('LinearRegression_CO2vsICE_year.png')
plt.show()

