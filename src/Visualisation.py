# ==========================================================================================================
# Description: This script is used to visualise the data and the results of the different Regression model.
# ==========================================================================================================

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

data_folder = './processed_data/'
output_folder = './outputs/'

# ------------------------ Load data (observations and estimation) ------------------------

observations_nh = pd.read_csv(os.path.join(data_folder, 'NH_Data.csv'), usecols=['Sea_Ice_Extent'])  # Observation of Northern Hemisphere
observations_sh = pd.read_csv(os.path.join(data_folder, 'SH_Data.csv'), usecols=['Sea_Ice_Extent'])  # Observation of Southern Hemisphere
co2 = pd.read_csv(os.path.join(data_folder, 'NH_Data.csv'), usecols=['CO2'])  # CO2 emissions
year = pd.read_csv(os.path.join(data_folder, 'NH_Data.csv'), usecols=['Year'])  # Year
estimations = pd.read_csv(os.path.join(output_folder, 'yestimations.csv'))  # Estimations of Northern Hemisphere
estimations = pd.read_csv(os.path.join(output_folder, 'yestimations.csv'))  # Estimations of Northern Hemisphere

# Ensure that the columns exist in the estimation file
if 'Estim_North_linReg' in estimations.columns and 'Estim_South_LinReg' in estimations.columns and 'Estim_South_polyReg' in estimations.columns and 'Estim_South_multiReg':
    y_estim_nh = estimations['Estim_North_linReg']
    y_estim_sh = estimations['Estim_South_LinReg']
    y_estim_sh_poly = estimations['Estim_South_polyReg']
    y_estim_sh_multi = estimations['Estim_South_multiReg']
    print("Estimation columns found and extracted.")
else:
    print("Estimation columns are missing in the CSV file.")
    exit(1)

# # Extraire les colonnes nécessaires pour les observations
# if 'NH_Extent' in observations_nh.columns and 'SH_Extent' in observations_sh.columns:
#     y_obs_nh = observations_nh['NH_Extent']  # Observations de l'Hémisphère Nord
#     y_obs_sh = observations_sh['SH_Extent']  # Observations de l'Hémisphère Sud
#     print("Colonnes 'Year' trouvées et extraites pour les observations.")
# else:
#     print("Les colonnes 'Year' sont manquantes dans les fichiers d'observations.")
#     exit(1)

#----------------------- Plot for Northern Hemisphere ------------------------

# Créer une figure avec deux sous-graphiques côte à côte
fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 6))

# Plot yN vs co2
ax1.scatter(co2, observations_nh, label='Observations NH', color='blue')
ax1.plot(co2, y_estim_nh, label='Linear Regression Model', color='red')
ax1.set_xlabel('Carbon Dioxide (Gt)', fontsize=12)
ax1.set_ylabel('Ice Surface North (million km²)', fontsize=12)
ax1.set_title('Global CO2 emissions vs Sea Ice Extent (Northern Hemisphere)')
ax1.legend(loc='lower left')
ax1.grid(True)

# Plot yN vs year
ax2.scatter(year, observations_nh, label='Observations NH', color='blue')
ax2.plot(year, y_estim_nh, label='Estimations NH', color='red')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Ice Surface North (million km²)', fontsize=12)
ax2.set_title('Year vs Sea Ice Extent (Northern Hemisphere)')
ax2.legend(loc='lower left')
ax2.grid(True)
plt.savefig('outputs/2_Year_vs_IceExtent_NH.png')
# Save the plot
plt.savefig(output_folder + '3_NH_Linear_Regression_plot.png')

# ----------------------- Plot for Southern Hemisphere ------------------------

#--------------------------
# Linear regression model
#--------------------------

fig2, (ax3, ax4) = plt.subplots(1, 2, figsize=(20, 6))

# Plot yS vs CO2
ax3.scatter(co2, observations_sh, label='Observations SH', color='blue') 
ax3.plot(co2, y_estim_sh, label='Linear Regression Model', color='red')  
ax3.set_xlabel('Carbon Dioxide (Gt)', fontsize=12)
ax3.set_ylabel('Ice Surface (million km²)', fontsize=12)
ax3.set_title(' Global CO2 emissions vs Sea Ice Extent (Southern Hemisphere)')
ax3.legend(loc ='lower left')
ax3.grid(True)

# Plot yS vs year
ax4.scatter(year, observations_sh, label='Observations SH', color='blue')
ax4.plot(year, y_estim_sh, label='Linear Regression Model', color='red')
ax4.set_xlabel('Year', fontsize=12)
ax4.set_ylabel('Ice Surface (million km²)', fontsize=12)
ax4.set_title('Year vs Sea Ice Extent (Southern Hemisphere)')
ax4.legend(loc='lower left')
ax4.grid(True)
plt.savefig( output_folder + '4_SH_Linear_Regression_plot.png')

# ------------------------------
# Multi-linear regression model
# ------------------------------

# Plot yS vs year
plt.figure(figsize=(10, 6))
plt.scatter(year, observations_sh, label='Observations SH', color='blue')
plt.plot(year, y_estim_sh_multi, label='Multiple Regression Model', color='red')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Ice Surface (million km²)', fontsize=12)
plt.title('Year vs Sea Ice Extent (Southern Hemisphere)')
plt.legend(loc='lower left')
plt.grid(True)
plt.savefig( output_folder + '6_SH_Multiple_Regression_plot.png')

# ---------------------------
# Quadratic regression model
# ---------------------------

fig4, (ax7, ax8) = plt.subplots(1, 2, figsize=(20, 6))

# Plot yS vs CO2
ax7.scatter(co2, observations_sh, label='Observations SH', color='blue') 
ax7.plot(co2, y_estim_sh_poly, label='Quadratic Regression Model', color='red')  
ax7.set_xlabel('Carbon Dioxide (Gt)', fontsize=12)
ax7.set_ylabel('Ice Surface (million km²)', fontsize=12)
ax7.set_title(' Global CO2 emissions vs Sea Ice Extent (Southern Hemisphere)')
ax7.legend(loc ='lower left')
ax7.grid(True)

# Plot yS vs year
ax8.scatter(year, observations_sh, label='Observations SH', color='blue')
ax8.plot(year, y_estim_sh_poly, label='Quadratic Regression Model', color='red')
ax8.set_xlabel('Year', fontsize=12)
ax8.set_ylabel('Ice Surface (million km²)', fontsize=12)
ax8.set_title('Year vs Sea Ice Extent (Southern Hemisphere)')
ax8.legend(loc='lower left')
ax8.grid(True)
plt.savefig( output_folder + '5_SH_Quadratic_Regression_plot.png')

print('Plots saved.')

