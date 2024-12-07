## Extract the month data from the ice extent dataset and CO2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from sklearn.preprocessing import StandardScaler

data_folder = 'data/'
output_folder = 'outputs/'

# Read the Excel file into a DataFrame
df_nh = pd.read_excel(data_folder + 'Sea_Ice_Index_Monthly_Data_by_Year_G02135_v3.0.xlsx', sheet_name='NH-Extent')  # Adjust the sheet_name as needed
df_sh = pd.read_excel(data_folder + 'Sea_Ice_Index_Monthly_Data_by_Year_G02135_v3.0.xlsx', sheet_name='SH-Extent') 
df_co2 = pd.read_excel(data_folder + 'IEA_EDGAR_CO2_1970_2023.xlsx', sheet_name='IPCC 2006')
print('Excel read.')

# Display the DataFrame
# print(df_nh.head())
#print(df_sh.head())
# print(df_co2.head())

# Define the columns and rows we want
nhcut= df_nh.iloc[1:46,:13].reset_index(drop=True)
shcut= df_sh.iloc[1:46,:13].reset_index(drop=True)
# df_co2cut= df_co2.iloc[9:3539, 17:62].reset_index(drop=True)
print('Dataframe cut.')

nhcut.replace('', np.nan, inplace=True)
shcut.replace('', np.nan, inplace=True)

#print(nhcut.head())
#print(shcut.head())
#print(df_co2cut.head())
print('Data selected.')
#print(pd.to_numeric(nhcut))


# df_nhcut = pd.DataFrame(nhcut, columns=['Annual'])
# df_shcut = pd.DataFrame(shcut, columns=['Annual'])
nhcut.rename(columns={'Unnamed: 0': 'Year'}, inplace=True)
shcut.rename(columns={'Unnamed: 0': 'Year'}, inplace=True)
print('Column renamed.')


melted_nh = pd.melt(nhcut, id_vars=['Year'], var_name='Month', value_name='Value')
melted_sh = pd.melt(shcut, id_vars=['Year'], var_name='Month', value_name='Value')
# melted_nh = melted_nh.sort_values(by='Year' )

# Create a dictionary to map month names to numbers
month_dict = {
    'January': '01', 'February': '02', 'March': '03', 'April': '04',
    'May': '05', 'June': '06', 'July': '07', 'August': '08',
    'September': '09', 'October': '10', 'November': '11', 'December': '12'
}

# Map the month names to numbers
melted_nh['Month'] = melted_nh['Month'].map(month_dict)
melted_sh['Month'] = melted_sh['Month'].map(month_dict)

# Combine the Year and Month columns to create the desired date format
melted_nh['Date'] = melted_nh['Year'].astype(str) + '-' + melted_nh['Month']
melted_sh['Date'] = melted_sh['Year'].astype(str) + '-' + melted_sh['Month']

# Select the desired columns
nh_sorted = melted_nh[['Date', 'Value']]
sh_sorted = melted_sh[['Date', 'Value']]
# Replace blank entries with NaN
#nh_sorted.replace('', np.nan, inplace=True)

nh_sorted.to_csv(output_folder + 'nh_months.csv', index=False)
sh_sorted.to_csv(output_folder + 'sh_months.csv', index=False)
print('Converted to csv file')

#print(nh_sorted)

#mmm


#print(nhcut.head())
#print(shcut.head())

#print('new dataframe')
#print(df_nhcut.head())
#print(df_co2cut.head())


# sum_co2 = df_co2cut.sum()
# sum_co2_df = pd.DataFrame(sum_co2, columns=['CO2_Mass'])
# sum_co2_df.reset_index(drop=True, inplace=True)
#print(sum_co2_df.head())


# index_range = [x +1979 for x in index_range]
#years = list(range(1979, 2024))
# sum_co2_df['Year'] = years
#df_nhcut['Year'] = years
#df_shcut['Year'] = years
#print('Years column added.')
#print(df_nhcut.head())


# Ensure the data is numeric and handle missing values
#df_nhcut['NH_Extent'] = pd.to_numeric(df_nhcut['NH_Extent'], errors='coerce')
#df_shcut['SH_Extent'] = pd.to_numeric(df_shcut['SH_Extent'], errors='coerce')
# sum_co2_df['CO2_Mass'] = pd.to_numeric(sum_co2_df['CO2_Mass'], errors='coerce')
#print('To numeric.')

'''
# Assuming nhcut is a DataFrame with the data you want to scale
nhcut_values = nhcut.values.reshape(-1, 1)  # Reshape to a 2D array if necessary
scaler = StandardScaler()
nhcut['std_NH'] = scaler.fit_transform(nhcut_values).flatten()
''' 

# Exemple de standardisation
# sum_co2_df['std_CO2'] = StandardScaler().fit_transform(np.array(sum_co2).reshape(-1, 1))
#df_nhcut['std_NH'] = StandardScaler().fit_transform(np.array(nhcut).reshape(-1, 1))
#df_shcut['std_SH'] = StandardScaler().fit_transform(np.array(shcut).reshape(-1, 1))
#print(df_shcut.head())
#print(sum_co2_df.head())
#print('Data standardised.')


# Ensuite, effectuer la régression sur x_scaled et y_scaled

#print('creating csv file')
#df_nhcut.to_csv(output_folder + 'sea_ice_nh.csv', index=False)
#df_shcut.to_csv(output_folder + 'sea_ice_sh.csv', index=False)
# sum_co2_df.to_csv(output_folder + 'summed_co2.csv', index=False)
#print('Converted to csv.')





