# ==============================================================================================
# Description: This script is used to extract the data from the different datasets we gathered.
# ==============================================================================================

# Import de modules
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Set I/O folder names
data_folder = './data/'
output_folder = './processed_data'

# Create the folder where the processed data will go
os.makedirs('./outputs', exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# --------- Extracting Data from an Excelsheet (.xlsx) ---------------------------------------------------------------------

# Read the excel file into a dataFrame
df_nh = pd.read_excel(data_folder +'Sea_Ice_Index_Monthly_Data_by_Year_G02135_v3.0.xlsx', sheet_name='NH-Extent')
df_sh = pd.read_excel(data_folder +'Sea_Ice_Index_Monthly_Data_by_Year_G02135_v3.0.xlsx', sheet_name='SH-Extent') 
df_co2 = pd.read_excel(data_folder + 'IEA_EDGAR_CO2_1970_2023.xlsx', sheet_name='IPCC 2006')


# Define the columns and rows we want from the data sheet
df_nhcut= df_nh.iloc[1:46,14:15].reset_index(drop=True)
df_shcut= df_sh.iloc[1:46,14:15].reset_index(drop=True)
df_co2cut= df_co2.iloc[9:3539, 17:62].reset_index(drop=True)


# Rename dataframe columns to fit our needs
df_nhcut.rename(columns={'Annual': 'NH_Extent'}, inplace=True)
df_shcut.rename(columns={'Annual': 'SH_Extent'}, inplace=True)


# Summing individual country CO2 emmissions to get the total CO2 emmissions for each year
# And makine sure it is a dataframe 
sum_co2 = df_co2cut.sum()
sum_co2_df = pd.DataFrame(sum_co2, columns=['CO2'])

# Resting the row index
sum_co2_df.reset_index(drop=True, inplace=True)

# Adjusting the data from Gg to Gt for future calculation purposes
sum_co2_df['CO2'] = sum_co2_df['CO2'] * 0.000001

# Adding a 'Year' column to be able to keep track of the data acurately
years = list(range(1979, 2024))
sum_co2_df['Year'] = years
df_nhcut['Year'] = years
df_shcut['Year'] = years

# Ensure the data is numeric and handle missing values
df_nhcut['NH_Extent'] = pd.to_numeric(df_nhcut['NH_Extent'], errors='coerce')
df_shcut['SH_Extent'] = pd.to_numeric(df_shcut['SH_Extent'], errors='coerce')
sum_co2_df['CO2'] = pd.to_numeric(sum_co2_df['CO2'], errors='coerce')
print('NH, SH, CO2 data processed.')



# --------- Ploting Sea Ice Extent and CO2 Emissions Over Time --------------------------------------------------------------
# We are ploting those graphs to see if it is possible to use a linear regression for our approximation.

# Merge the DataFrames on the 'Year' column for plot construction
merged_nh = pd.merge(df_nhcut, sum_co2_df, on='Year')
merged_sh = pd.merge(df_shcut, sum_co2_df, on='Year')


# Plot the data on 2 figures, one for the Northern Hemisphere and one for the Sourthern Hemisphere
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 6))

## Plot Northern Hemisphere sea ice extent vs CO2
# Sea ice extent over Time
ax1.plot(merged_nh['Year'], merged_nh['NH_Extent'], color='blue', label='NH Sea Ice Extent')
ax1.set_xlabel('Year')
ax1.set_ylabel('NH Sea Ice Extent [Million km²]', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

# CO2 over Time
ax1_twin = ax1.twinx()
ax1_twin.plot(merged_nh['Year'], merged_nh['CO2'], color='red', label='CO2')
ax1_twin.set_ylabel('CO2 [Gt]', color='red')
ax1_twin.tick_params(axis='y', labelcolor='red')

# Set a figure title and legends 
ax1.set_title('Northern Hemisphere\'s Sea Ice Extent and CO2 Emissions Over Time')
ax1.legend(loc='upper left')
ax1_twin.legend(loc='upper right')
plt.grid(True)

# Second plot Sourthern Hemisphere sea ice extent vs CO2
# Sea ice extent over Time
ax2.plot(merged_sh['Year'], merged_sh['SH_Extent'], color='green', label='SH Sea Ice Extent')
ax2.set_xlabel('Year')
ax2.set_ylabel('SH Sea Ice Extent [Million km²]', color='green')
ax2.tick_params(axis='y', labelcolor='green')
ax2.xaxis.set_major_locator(MaxNLocator(nbins=10))

# CO2 over Time
ax2_twin = ax2.twinx()
ax2_twin.plot(merged_sh['Year'], merged_sh['CO2'], color='red', label='CO2')
ax2_twin.set_ylabel('CO2 [Gt]', color='red')
ax2_twin.tick_params(axis='y', labelcolor='red')

# Set a figure title and legends 
ax2.set_title('Southern Hemisphere\'s Sea Ice Extent and CO2 Emissions Over Time')
ax2.legend(loc='upper left')
ax2_twin.legend(loc='upper right')

# Show plot
#plt.tight_layout()
plt.grid(True)
plt.savefig('./outputs/' + '1_Correlations.png')
print('Ploted Correlation. Saved Figure.')
#plt.show()



# --------- Extracting Data from ASC file (.asc) ------------------------------------------------------------

# Set input and output file names
input_1 = 'aravg.ann.ocean.90S.60S.v6.0.0.202410.asc'
output_1 = 'ocean_temp_annual_SPole.csv'

# Make an empty entry list that can be filled
list_entries = []

# Reading the lines of the ASC file into the entry list
with open(data_folder + input_1, 'r') as file:
    content = file.readlines()
    for line in content:
        list_entries.append(line.strip())

# Make an empty list
split_data = []

# An element in list_entries look like this [1850   -0.419871 -999.000000 -999.000000 -999.000000 -999.000000]
# We want to get all the values matched with the year, like this [1850,-0.419871], [1850, -999.000000], [1850, -999.000000], [1850, -999.000000], [1850, -999.000000]
for row in list_entries:
    values = row.strip().split()
    years = values[0]
    for i,value in enumerate(values[1:]):
        split_data.append([f'{years}',value])

# Making the split_data list into a dataframe
temp_df = pd.DataFrame(split_data, columns=['Year','Temperature'])

# -999.000000 signifies there is no data, so we are removing from the dataframe the rows that do not have data
temp_df = temp_df[temp_df['Temperature'] != '-999.000000']

# Choosing the years we need for our analysis
ocean_temp_cut = temp_df[129:174]

# Because we removed columns and cut our dataframe, we reset the row index
ocean_temp_cut.reset_index(drop=True, inplace=True)
print('Temperature data processed.')



# --------- Extracting Data from a CSV file (.csv) ---------------------------------------------------------------------

# Create input and output file
input_2 = 'precipitations.csv'
output_2 = 'precipitation_adjusted.csv'

# Reading the CSV file, while ignoring the comments
precipitation_df = pd.read_csv(data_folder + input_2, comment='#')

# Renaming the column for our convinience 
precipitation_df.rename(columns={'Anomaly' : 'Precipitation'}, inplace=True)
print('Precipitation data processed.')



# --------- Merging the Data -------------------------------------------------------------------------------------------------
# We are merging the data into two distinct files
# One for the northern hemisphere regression and one for the southern hemisphere regression


# Setting the same in and output folder
in_out_folder = './processed_data/'

# Select the desired columns from each dataframe
base_years = df_nhcut['Year']
base_nh = df_nhcut['NH_Extent']  
co2 = sum_co2_df['CO2']  
base_sh = df_shcut['SH_Extent']  
precip = precipitation_df['Precipitation']
temp = ocean_temp_cut['Temperature']


# Combine the selected columns into 2 distinct dataframe (one NH and one for SH)
nh_merged_df = pd.DataFrame({
    'Year': base_years,
    'Sea_Ice_Extent': base_nh,
    'CO2': co2
})

sh_merged_df = pd.DataFrame({
    'Year': base_years,
    'Sea_Ice_Extent': base_sh,
    'CO2': co2,
    'Precipitation' : precip,
    'Temperature' : temp
})


# Define output names
output_nh = 'NH_Data.csv'
output_sh = 'SH_Data.csv'

# Save the merged DataFrame to a new CSV file
nh_merged_df.to_csv(in_out_folder + output_nh, index=False)
sh_merged_df.to_csv(in_out_folder + output_sh, index=False)
print(f"Data saved.")


