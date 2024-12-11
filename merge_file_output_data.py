## Merge all the data columns into one file
import pandas as pd

in_output = 'outputs/'

# Define the input file paths
file_base_nh = 'sea_ice_nh.csv'
file_co2 = 'summed_co2.csv'
file_base_sh = 'sea_ice_sh.csv'
file_precipitation_sh = 'precipitation_adjusted.csv'
file_temp_sh = 'ocean_temp_annual_SPole.csv'

# Read the individual files into DataFrames
df_nh = pd.read_csv(in_output+file_base_nh)
df_co2 = pd.read_csv(in_output+file_co2)
df_sh = pd.read_csv(in_output+file_base_sh)
df_precip = pd.read_csv(in_output+file_precipitation_sh)
df_temp = pd.read_csv(in_output+file_temp_sh)

# Select the desired columns
base_years = df_nh['Year']
base_nh = df_nh['NH_Extent']  
co2 = df_co2['CO2']  
base_sh = df_sh['SH_Extent']  
precip = df_precip['Precipitation']
temp = df_temp['Temperature']

#print(base_nh)

# Combine the selected columns into a single DataFrame
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


# Display the merged DataFrame
#print(merged_df)

# Save the merged DataFrame to a new CSV file
output_nh = 'NH_Data.csv'
output_sh = 'SH_Data.csv'

nh_merged_df.to_csv(in_output+output_nh, index=False)
sh_merged_df.to_csv(in_output+output_sh, index=False)

print(f"Merged Data")







