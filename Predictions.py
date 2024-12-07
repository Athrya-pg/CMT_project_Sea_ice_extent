import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

def interpolate_emissions(years, emissions, target_years):
    """Interpolate emissions for target years."""
    interp_func = interp1d(years, emissions,kind='linear', fill_value="extrapolate")
    return interp_func(target_years)

# Read linear regression coefficients from the text file
coefficients = {}
with open('outputs/coefficients.txt', 'r') as f:
    for line in f:
        name, value = line.split('=')
        coefficients[name.strip()] = float(value.strip())

m = coefficients['mN']
b = coefficients['bN']

# Target years
target_years = range(2023, 2101, 1)

# optimistic scenario : SSP1
years_spp1 = np.array([2023, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100])
emissions_ssp1 = np.array([39,37,28,20,11,5, -4,-10,-10])
emissions_interp_ssp1 = interpolate_emissions(years_spp1, emissions_ssp1, target_years)

# Intermediate scenario (SSP3)
years_ssp3 = np.array([2023, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100])
emissions_ssp3 = np.array([39,47,55,60,65,69,72,78,81])
emissions_interp_ssp3 = interpolate_emissions(years_ssp3, emissions_ssp3, target_years)

# Pessimistic scenario (SSP5)
years_ssp5 = np.array([2023, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100])
emissions_ssp5 = np.array([39, 49, 62, 78, 93, 115,127,130,125])
emissions_interp_ssp5 = interpolate_emissions(years_ssp5, emissions_ssp5, target_years)

# Display the results
plt.figure(figsize=(10, 6))
plt.plot(target_years, emissions_interp_ssp1, label='Optimistic Scenario (SSP1)', color='green')
plt.plot(target_years, emissions_interp_ssp3, label='Intermediate Scenario (SSP3)', color='orange')
plt.plot(target_years, emissions_interp_ssp5, label='Pessimistic Scenario (SSP5)', color='red')
plt.xlabel('Years')
plt.ylabel('CO₂ Emissions (Gt/year)')
plt.title('CO₂ Emission Scenarios from 2023 to 2100')
plt.legend()
plt.grid(True)
plt.show()

# Afficher les résultats dans la console
#for year, emission_ssp1, emission_ssp2, emission_ssp3 in zip(target_years, emissions_interp_ssp1, emissions_interp_ssp3, emissions_interp_ssp5):
#    print(f"Année: {year}, Emission CO₂ SSP1: {emission_ssp1:.2f} Gt, Emission CO₂ SSP2: {emission_ssp2:.2f} Gt, Emission CO₂ SSP3: {emission_ssp3:.2f} Gt")

# Calculate sea ice extent for each scenario
sea_ice_extent_ssp1 = m * emissions_interp_ssp1 + b
sea_ice_extent_ssp3 = m * emissions_interp_ssp3 + b
sea_ice_extent_ssp5 = m * emissions_interp_ssp5 + b

# plot sea ice extent
plt.figure(figsize=(10, 6))
plt.plot(target_years, sea_ice_extent_ssp1, label='Oprimistic Scenario (SSP1)', color='green')
plt.plot(target_years, sea_ice_extent_ssp3, label='Intermediate Scenario(SSP2)', color='orange')
plt.plot(target_years, sea_ice_extent_ssp5, label='Pessimistic Scenario (SSP3)', color='red')
plt.xlabel('Years')
plt.ylabel('Sea Ice Extent (million km²)')
plt.title('Sea Ice Extent Scenarios from 2023 to 2100 (North Pole)')
plt.legend()
plt.grid(True)
plt.show()

# Créer une figure et un axe
fig, ax1 = plt.subplots(figsize=(10, 6))

# Tracer les émissions de CO2 sur l'axe y principal
ax1.plot(target_years, emissions_interp_ssp1, label='Oprimistic Scenario (SSP1) - CO2', color='green', linestyle='--')
ax1.plot(target_years, emissions_interp_ssp3, label='Intermediate Scenario (SSP3) - CO2', color='orange', linestyle='--')
ax1.plot(target_years, emissions_interp_ssp5, label='Pessimistic Scenario (SSP5) - CO2', color='red', linestyle='--')
ax1.set_xlabel('Years')
ax1.set_ylabel('CO₂ Emissions (Gt/year)')
ax1.legend(loc='upper left')
ax1.grid(True)

# Créer un deuxième axe y
ax2 = ax1.twinx()

# Tracer l'étendue de la glace de mer sur le deuxième axe y
ax2.plot(target_years, sea_ice_extent_ssp1, label='Oprimistic Scenario (SSP1) - Glace', color='lightblue')
ax2.plot(target_years, sea_ice_extent_ssp3, label='Intermediate Scenario (SSP3) - Glace', color='blue')
ax2.plot(target_years, sea_ice_extent_ssp5, label='Pessimistic Scenario (SSP5) - Glace', color='darkblue')
ax2.set_ylabel('Sea Ice Extent (million km²)')
ax2.legend(loc='upper right')

# Ajouter un titre
plt.title('CO₂ Emission and Sea Ice Extent Scenarios from 2023 to 2100')

# Afficher le graphique
plt.show()

