#======================================================================================================================
# Description: This script uses linear regression coefficients to predict future CO2 emissions and sea ice extent according to 3 IPCC scenarios
#======================================================================================================================

# Import de modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Set I/O folder names
data_folder = './processed_data/'
output_folder = './outputs/'

# Function to interpolate emissions
def interpolate_emissions(years, emissions, target_years):
    """Interpolate emissions for target years."""
    interp_func = interp1d(years, emissions,kind='linear', fill_value="extrapolate")
    return interp_func(target_years)

# Read linear regression coefficients from the text file
coefficients = {}
with open(data_folder + 'coefficients.txt', 'r') as f:
    for line in f:
        name, value = line.split('=')
        coefficients[name.strip()] = float(value.strip())

# Selecte the coefficients
m = coefficients['mN']
b = coefficients['bN']

# Target years
target_years = range(2023, 2101, 1)

#----------------------- Predictions plots ------------------------

# optimistic scenario : SSP1
years_spp1 = np.array([2023, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100])
emissions_ssp1 = np.array([39,37,28,20,11,5, -4,-10,-10])
emissions_interp_ssp1 = interpolate_emissions(years_spp1, emissions_ssp1, target_years)

# Intermediate scenario: SSP3
years_ssp3 = np.array([2023, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100])
emissions_ssp3 = np.array([39,47,55,60,65,69,72,78,81])
emissions_interp_ssp3 = interpolate_emissions(years_ssp3, emissions_ssp3, target_years)

# Pessimistic scenario: SSP5
years_ssp5 = np.array([2023, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100])
emissions_ssp5 = np.array([39, 49, 62, 78, 93, 115,127,130,125])
emissions_interp_ssp5 = interpolate_emissions(years_ssp5, emissions_ssp5, target_years)

# Plot the predictions
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 6))

# Display the results of CO2 emmissions over time 
ax1.plot(target_years, emissions_interp_ssp1, label='Optimistic Scenario (SSP1)', color='green')
ax1.plot(target_years, emissions_interp_ssp3, label='Intermediate Scenario (SSP3)', color='orange')
ax1.plot(target_years, emissions_interp_ssp5, label='Pessimistic Scenario (SSP5)', color='red')
ax1.set_xlabel('Years')
ax1.set_ylabel('CO₂ Emissions [Gt/year]')
ax1.set_title('CO₂ Emission Scenarios from 2023 to 2100')
ax1.legend()
ax1.grid(True)

# Calculate sea ice extent for each scenario
sea_ice_extent_ssp1 = m * emissions_interp_ssp1 + b
sea_ice_extent_ssp3 = m * emissions_interp_ssp3 + b
sea_ice_extent_ssp5 = m * emissions_interp_ssp5 + b

# Plot sea ice extent over time
ax2.plot(target_years, sea_ice_extent_ssp1, label='Optimistic Scenario (SSP1)', color='green')
ax2.plot(target_years, sea_ice_extent_ssp3, label='Intermediate Scenario (SSP3)', color='orange')
ax2.plot(target_years, sea_ice_extent_ssp5, label='Pessimistic Scenario (SSP5)', color='red')
ax2.set_xlabel('Years')
ax2.set_ylabel('Sea Ice Extent [Million km²]')
ax2.set_title('Sea Ice Extent Scenarios from 2023 to 2100 (North Pole)')
ax2.legend()
ax2.grid(True)

plt.savefig(output_folder + '6_NH_Predictions_plot.png')
plt.show()
print('Predictions ploted and saved.')

#----------------------- Predictions file ----------------------------

# Read data file and select the data
data_nh = pd.read_csv(data_folder + 'NH_Data.csv', delimiter=',')

year_existing = data_nh['Year'].values
y_existing = data_nh['Sea_Ice_Extent'].values
CO2_existing = data_nh['CO2'].values

# Combine existing data and predictions
all_years = np.concatenate((year_existing, target_years))
all_y_ssp1 = np.concatenate((y_existing, sea_ice_extent_ssp1))
all_y_ssp3 = np.concatenate((y_existing, sea_ice_extent_ssp3))
all_y_ssp5 = np.concatenate((y_existing, sea_ice_extent_ssp5))
all_CO2_ssp1 = np.concatenate((CO2_existing, emissions_interp_ssp1)) 
all_CO2_ssp3 = np.concatenate((CO2_existing, emissions_interp_ssp3))
all_CO2_ssp5 = np.concatenate((CO2_existing, emissions_interp_ssp5))

# Create a DataFrame with all the data
extended_data = pd.DataFrame({
    'Year': all_years,
    'y_SSP1': all_y_ssp1,
    'y_SSP3': all_y_ssp3,
    'y_SSP5': all_y_ssp5,
    'CO2_SSP1': all_CO2_ssp1,
    'CO2_SSP3': all_CO2_ssp3,
    'CO2_SSP5': all_CO2_ssp5
})

# Save the DataFrame to a CSV file
extended_data.to_csv(f'{output_folder}/predictions_data.csv', index=False)
print(f"Extended predictions saved to {output_folder}/predictions_data.csv")





