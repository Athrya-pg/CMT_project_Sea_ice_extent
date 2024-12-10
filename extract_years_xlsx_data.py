# import the libraries needed
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
nhcut= df_nh.iloc[1:46,14:15].reset_index(drop=True)
shcut= df_sh.iloc[1:46,14:15].reset_index(drop=True)
df_co2cut= df_co2.iloc[9:3539, 17:62].reset_index(drop=True)
print('Dataframe cut.')


#print(nhcut.head())
#print(shcut.head())
#print(df_co2cut.head())
print('Data selected.')
#print(pd.to_numeric(nhcut))

df_nhcut = pd.DataFrame(nhcut, columns=['Annual'])
df_shcut = pd.DataFrame(shcut, columns=['Annual'])
df_nhcut.rename(columns={'Annual': 'NH_Extent'}, inplace=True)
df_shcut.rename(columns={'Annual': 'SH_Extent'}, inplace=True)
print('Is a Dataframe. Column renamed.')

#print('new dataframe')
#print(df_nhcut.head())
#print(df_co2cut.head())


sum_co2 = df_co2cut.sum()
sum_co2_df = pd.DataFrame(sum_co2, columns=['CO2'])
sum_co2_df.reset_index(drop=True, inplace=True)
sum_co2_df['CO2'] = sum_co2_df['CO2'] * 0.000001
# print(sum_co2_df.head())

# index_range = [x +1979 for x in index_range]
years = list(range(1979, 2024))
sum_co2_df['Year'] = years
df_nhcut['Year'] = years
df_shcut['Year'] = years
print('Years column added.')
#print(df_nhcut.head())


# Ensure the data is numeric and handle missing values
df_nhcut['NH_Extent'] = pd.to_numeric(df_nhcut['NH_Extent'], errors='coerce')
df_shcut['SH_Extent'] = pd.to_numeric(df_shcut['SH_Extent'], errors='coerce')
sum_co2_df['CO2'] = pd.to_numeric(sum_co2_df['CO2'], errors='coerce')
print('To numeric.')

'''
# Assuming nhcut is a DataFrame with the data you want to scale
nhcut_values = nhcut.values.reshape(-1, 1)  # Reshape to a 2D array if necessary
scaler = StandardScaler()
nhcut['std_NH'] = scaler.fit_transform(nhcut_values).flatten()
''' 

# Exemple de standardisation
sum_co2_df['std_CO2'] = StandardScaler().fit_transform(np.array(sum_co2).reshape(-1, 1))
df_nhcut['std_NH'] = StandardScaler().fit_transform(np.array(nhcut).reshape(-1, 1))
df_shcut['std_SH'] = StandardScaler().fit_transform(np.array(shcut).reshape(-1, 1))
#print(df_shcut.head())
#print(sum_co2_df.head())
print('Data standardised.')


# Ensuite, effectuer la régression sur x_scaled et y_scaled

#print('creating csv file')
df_nhcut.to_csv(output_folder + 'sea_ice_nh.csv', index=False)
df_shcut.to_csv(output_folder + 'sea_ice_sh.csv', index=False)
sum_co2_df.to_csv(output_folder + 'summed_co2.csv', index=False)
print('Converted to csv.')



'''
# Read the CSV files into DataFrames
df_nhcut = pd.read_csv('sea_ice_nh.csv', names=['NH_Extent', 'Year'])
df_shcut = pd.read_csv('sea_ice_sh.csv', names=['SH_Extent', 'Year'])
sum_co2_df = pd.read_csv('summed_co2.csv', names=['CO2_Mass', 'Year'])


# Ensure the data is numeric and handle missing values
df_nhcut['NH_Extent'] = pd.to_numeric(df_nhcut['NH_Extent'], errors='coerce')
df_shcut['SH_Extent'] = pd.to_numeric(df_shcut['SH_Extent'], errors='coerce')
sum_co2_df['CO2_Mass'] = pd.to_numeric(sum_co2_df['CO2_Mass'], errors='coerce')


# # Drop rows with missing values
# df_nhcut.dropna(inplace=True)
# df_shcut.dropna(inplace=True)
# sum_co2_df.dropna(inplace=True)


# Rename columns for clarity
df_nhcut.columns = ['NH_Extent', 'Year']
df_shcut.columns = ['SH_Extent', 'Year']
sum_co2_df.columns = ['CO2_Mass', 'Year']


# Merge the DataFrames on the 'Year' column
merged_nh = pd.merge(df_nhcut, sum_co2_df, on='Year')
merged_sh = pd.merge(df_shcut, sum_co2_df, on='Year')


# Log-transform the data
merged_nh['log_NH_Extent'] = np.log(merged_nh['NH_Extent'])
merged_nh['log_CO2_Mass'] = np.log(merged_nh['CO2_Mass'])
merged_sh['log_SH_Extent'] = np.log(merged_sh['SH_Extent'])
merged_sh['log_CO2_Mass'] = np.log(merged_sh['CO2_Mass'])
#print(merged_sh.tail())





# # Plot the data
# fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# # Plot NH Sea Ice Extent vs CO2 Mass
# ax1.plot(merged_nh['Year'], merged_nh['NH_Extent'], color='blue', label='NH Sea Ice Extent')
# ax1.set_xlabel('Year')
# ax1.set_ylabel('NH Sea Ice Extent (million sq km)', color='blue')
# ax1.tick_params(axis='y', labelcolor='blue')

# ax1_twin = ax1.twinx()
# ax1_twin.plot(merged_nh['Year'], merged_nh['CO2_Mass'], color='red', label='CO2 Mass')
# ax1_twin.set_ylabel('CO2 Mass (Gt)', color='red')
# ax1_twin.tick_params(axis='y', labelcolor='red')

# ax1.set_title('NH Sea Ice Extent and CO2 Mass Over Time')
# ax1.legend(loc='upper left')
# ax1_twin.legend(loc='upper right')

# # Plot SH Sea Ice Extent vs CO2 Mass
# ax2.plot(merged_sh['Year'], merged_sh['SH_Extent'], color='green', label='SH Sea Ice Extent')
# ax2.set_xlabel('Year')
# ax2.set_ylabel('SH Sea Ice Extent (million sq km)', color='green')
# ax2.tick_params(axis='y', labelcolor='green')
# ax2.xaxis.set_major_locator(MaxNLocator(nbins=10))

# ax2_twin = ax2.twinx()
# ax2_twin.plot(merged_sh['Year'], merged_sh['CO2_Mass'], color='red', label='CO2 Mass')
# ax2_twin.set_ylabel('CO2 Mass (Gt)', color='red')
# ax2_twin.tick_params(axis='y', labelcolor='red')

# ax2.set_title('SH Sea Ice Extent and CO2 Mass Over Time')
# ax2.legend(loc='upper left')
# ax2_twin.legend(loc='upper right')

# # Show plot
# plt.tight_layout()
# plt.savefig('Correlations.png')
# #plt.show()

# # Plot the log-transformed data
# fig, (ax3, ax4) = plt.subplots(2, 1, figsize=(10, 12))

# # Plot log-transformed NH Sea Ice Extent vs CO2 Mass
# ax3.loglog(merged_nh['Year'], merged_nh['NH_Extent'], color='blue', label='Log NH Sea Ice Extent')
# ax3.set_xlabel('Year')
# ax3.set_ylabel('Log NH Sea Ice Extent', color='blue')
# ax3.tick_params(axis='y', labelcolor='blue')

# ax3_twin = ax3.twinx()
# ax3_twin.loglog(merged_nh['Year'], merged_nh['log_CO2_Mass'], color='red', label='Log CO2 Mass')
# ax3_twin.set_ylabel('Log CO2 Mass', color='red')
# ax3_twin.tick_params(axis='y', labelcolor='red')

# ax3.set_title('Log NH Sea Ice Extent and Log CO2 Mass Over Time')
# ax3.legend(loc='upper left')
# ax3_twin.legend(loc='upper right')

# # Plot log-transformed SH Sea Ice Extent vs CO2 Mass
# ax4.loglog(merged_sh['Year'], merged_sh['SH_Extent'], color='green', label='Log SH Sea Ice Extent')
# ax4.set_xlabel('Year')
# ax4.set_ylabel('Log SH Sea Ice Extent', color='green')
# ax4.tick_params(axis='y', labelcolor='green')

# ax4_twin = ax4.twinx()
# ax4_twin.loglog(merged_sh['Year'], merged_sh['CO2_Mass'], color='red', label='Log CO2 Mass')
# ax4_twin.set_ylabel('Log CO2 Mass', color='red')
# ax4_twin.tick_params(axis='y', labelcolor='red')

# ax4.set_title('Log SH Sea Ice Extent and Log CO2 Mass Over Time')
# ax4.legend(loc='upper left')
# ax4_twin.legend(loc='upper right')

# plt.tight_layout()
# plt.show()


'''




