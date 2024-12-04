import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Load data (observations and estimation)
observations_nh = pd.read_csv('outputs/sea_ice_nh.csv')  # Observation of Northern Hemisphere
observations_sh = pd.read_csv('outputs/sea_ice_sh.csv')  # Observation of Southern Hemisphere
x = pd.read_csv('outputs/summed_co2.csv')  # Emissions de CO2
x = x['CO2_Mass']
t = x['Year']
estimations_nh = pd.read_csv('yestimation.csv')  # Estimations of Northern Hemisphere
estimations_sh = pd.read_csv('yestimation.csv')  # Estimations of Southern Hemisphere
print(estimations_nh.head())

y_obs_nh = observations_nh['Annual']  # Observations de l'Hémisphère Nord
y_obs_sh = observations_sh['Annual']  # Observations de l'Hémisphère Nord
y_estim_nh = estimations_nh["Estim_North_LinReg"]  # Estimations of Northern Hemisphere
y_estim_sh = estimations_sh['Estim_South_LinReg']  # Estimations of Southern Hemisphere
y_estim_sh_poly = estimations_sh['Estim_South_polyReg']  # Estimations

#Plot yN vs x with y_estim_nh
plt.figure(figsize=(10, 6))
plt.scatter(x, y_obs_nh, label='Observations NH', color='blue') 
plt.plot(x, y_estim_nh, label='Linear Regression Model', color='red')  
plt.xlabel('Carbon Dioxide (Gt)', fontsize=12)
plt.ylabel('Ice Surface (million km²)', fontsize=12)
plt.title(' Global CO2 emissions vs Arctic Sea Ice Extent (Northern Hemisphere)')
plt.legend(loc ='upper right')
plt.grid(True)
plt.savefig('LinearReg_CO2_vs_ICE_NH_year.png')
plt.show()

#Plot yS vs x with y_estim_sh
plt.figure(figsize=(10, 6))
plt.scatter(x, y_obs_nh, label='Observations SH', color='blue') 
plt.plot(x, y_estim_nh, label='Linear Regression Model', color='red')  
plt.xlabel('Carbon Dioxide (Gt)', fontsize=12)
plt.ylabel('Ice Surface (million km²)', fontsize=12)
plt.title(' Global CO2 emissions vs Arctic Sea Ice Extent (Southern Hemisphere)')
plt.legend(loc ='upper right')
plt.grid(True)
plt.savefig('LinearReg_CO2_vs_ICE_SH_year.png')
plt.show()

#Plot yN vs t with y_estim_nh
plt.figure(figsize=(10, 6))
plt.scatter(t, y_obs_nh, label='Observations NH', color='blue')
plt.plot(t, y_estim_nh, label='Estimations NH', color='red')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Ice Surface (million km²)', fontsize=12)
plt.title('Year vs Sea Ice Extent (Northern Hemisphere)')
plt.legend(loc='upper right')
plt.grid(True)
plt.savefig('Year_vs_IceExtent_NH.png')
plt.show()

#Plot yS vs t with y_estim_sh
plt.figure(figsize=(10, 6))
plt.scatter(t, y_obs_sh, label='Observations SH', color='blue')
plt.plot(t, y_estim_sh, label='Estimations SH', color='red')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Ice Surface (million km²)', fontsize=12)
plt.title('Year vs Sea Ice Extent (Southern Hemisphere)')
plt.legend(loc='upper right')
plt.grid(True)
plt.savefig('Year_vs_IceExtent_SH.png')
plt.show()

#Plot ySpoly vs x with y_estim_sh
plt.figure(figsize=(10, 6))
plt.scatter(x, y_obs_sh, label='Observations SH', color='blue')
plt.plot(x, y_estim_sh_poly, label='Polynomial Regression SH', color='green')
plt.xlabel('Carbon Dioxide (Gt)', fontsize=12)
plt.ylabel('Ice Surface (million km²)', fontsize=12)
plt.title('CO2 Emissions vs Sea Ice Extent (Southern Hemisphere) - Polynomial Regression')
plt.legend(loc='upper right')
plt.grid(True)
plt.savefig('CO2_vs_IceExtent_SH_Poly.png')
plt.show()

# Plot ySpoly vs t
plt.figure(figsize=(10, 6))
plt.scatter(t, y_obs_sh, label='Observations SH', color='blue')
plt.plot(t, y_estim_sh_poly, label='Polynomial Regression SH', color='green')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Ice Surface (million km²)', fontsize=12)
plt.title('Year vs Sea Ice Extent (Southern Hemisphere) - Polynomial Regression')
plt.legend(loc='upper right')
plt.grid(True)
plt.savefig('Year_vs_IceExtent_SH_Poly.png')
plt.show()

