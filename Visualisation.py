import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load data (observations and estimation)
observations_nh = pd.read_csv('outputs/sea_ice_nh.csv')  # Observation of Northern Hemisphere
observations_sh = pd.read_csv('outputs/sea_ice_sh.csv')  # Observation of Southern Hemisphere
co2_data = pd.read_csv('outputs/summed_co2.csv')  # Emissions de CO2
estimations = pd.read_csv('outputs/yestimation.csv')  # Estimations of Northern Hemisphere

# CO2 = co2_data['CO2_Mass']
# t = co2_data['Year']

# y_obs_nh = observations_nh['Annual']  # Observations de l'Hémisphère Nord
# y_obs_sh = observations_sh['Annual']  # Observations de l'Hémisphère Nord
# y_estim_nh = estimations["Estim_North_linReg"]  # Estimations of Northern Hemisphere
# y_estim_sh = estimations['Estim_South_LinReg']  # Estimations of Southern Hemisphere
# y_estim_sh_poly = estimations['Estim_South_polyReg']  # Estimations


# Assure-toi que les colonnes existent et contiennent des valeurs valides
if 'Year' in co2_data.columns and 'CO2_Mass' in co2_data.columns:
    t = co2_data['Year']
    CO2 = co2_data['CO2_Mass']
    print("Colonnes 'Year' et 'CO2_Mass' trouvées et extraites.")
else:
    print("Les colonnes 'Year' ou 'CO2_Mass' sont manquantes dans le fichier CSV.")
    exit(1)

# Assurez-vous que les colonnes existent dans le fichier d'estimations
if 'Estim_North_linReg' in estimations.columns and 'Estim_South_LinReg' in estimations.columns and 'Estim_South_polyReg' in estimations.columns:
    y_estim_nh = estimations['Estim_North_linReg']
    y_estim_sh = estimations['Estim_South_LinReg']
    y_estim_sh_poly = estimations['Estim_South_polyReg']
    print("Colonnes d'estimations trouvées et extraites.")
else:
    print("Les colonnes d'estimations sont manquantes dans le fichier CSV.")
    exit(1)
# Extraire les colonnes nécessaires pour les observations
if 'Year' in observations_nh.columns and 'Year' in observations_sh.columns:
    y_obs_nh = observations_nh['Year']  # Observations de l'Hémisphère Nord
    y_obs_sh = observations_sh['Year']  # Observations de l'Hémisphère Sud
    print("Colonnes 'Year' trouvées et extraites pour les observations.")
else:
    print("Les colonnes 'Year' sont manquantes dans les fichiers d'observations.")
    exit(1)

#Plot yN vs CO2 with y_estim_nh
plt.figure(figsize=(10, 6))
plt.scatter(CO2, y_obs_nh, label='Observations NH', color='blue') 
plt.plot(CO2, y_estim_nh, label='Linear Regression Model', color='red')  
plt.xlabel('Carbon Dioxide (Gt)', fontsize=12)
plt.ylabel('Ice Surface (million km²)', fontsize=12)
plt.title(' Global CO2 emissions vs Arctic Sea Ice Extent (Northern Hemisphere)')
plt.legend(loc ='upper right')
plt.grid(True)
plt.savefig('outputs/LinearReg_CO2_vs_ICE_NH_year.png')

#Plot yS vs CO2 with y_estim_sh
plt.figure(figsize=(10, 6))
plt.scatter(CO2, y_obs_sh, label='Observations SH', color='blue') 
plt.plot(CO2, y_estim_sh, label='Linear Regression Model', color='red')  
plt.xlabel('Carbon Dioxide (Gt)', fontsize=12)
plt.ylabel('Ice Surface (million km²)', fontsize=12)
plt.title(' Global CO2 emissions vs Arctic Sea Ice Extent (Southern Hemisphere)')
plt.legend(loc ='upper right')
plt.grid(True)
plt.savefig('outputs/LinearReg_CO2_vs_ICE_SH_year.png')

#Plot yN vs t with y_estim_nh
plt.figure(figsize=(10, 6))
plt.scatter(t, y_obs_nh, label='Observations NH', color='blue')
plt.plot(t, y_estim_nh, label='Estimations NH', color='red')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Ice Surface (million km²)', fontsize=12)
plt.title('Year vs Sea Ice Extent (Northern Hemisphere)')
plt.legend(loc='upper right')
plt.grid(True)
plt.savefig('outputs/Year_vs_IceExtent_NH.png')

#Plot yS vs t with y_estim_sh
plt.figure(figsize=(10, 6))
plt.scatter(t, y_obs_sh, label='Observations SH', color='blue')
plt.plot(t, y_estim_sh, label='Estimations SH', color='red')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Ice Surface (million km²)', fontsize=12)
plt.title('Year vs Sea Ice Extent (Southern Hemisphere)')
plt.legend(loc='upper right')
plt.grid(True)
plt.savefig('outputs/Year_vs_IceExtent_SH.png')

#Plot ySpoly vs CO2 with y_estim_sh
plt.figure(figsize=(10, 6))
plt.scatter(CO2, y_obs_sh, label='Observations SH', color='blue')
plt.plot(CO2, y_estim_sh_poly, label='Polynomial Regression SH', color='green')
plt.xlabel('Carbon Dioxide (Gt)', fontsize=12)
plt.ylabel('Ice Surface (million km²)', fontsize=12)
plt.title('CO2 Emissions vs Sea Ice Extent (Southern Hemisphere) - Polynomial Regression')
plt.legend(loc='upper right')
plt.grid(True)
plt.savefig('outputs/CO2_vs_IceExtent_SH_Poly.png')

# Plot ySpoly vs t
plt.figure(figsize=(10, 6))
plt.scatter(t, y_obs_sh, label='Observations SH', color='blue')
plt.plot(t, y_estim_sh_poly, label='Polynomial Regression SH', color='green')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Ice Surface (million km²)', fontsize=12)
plt.title('Year vs Sea Ice Extent (Southern Hemisphere) - Polynomial Regression')
plt.legend(loc='upper right')
plt.grid(True)
plt.savefig('outputs/Year_vs_IceExtent_SH_Poly.png')

print("Plot saved in outputs folder")

