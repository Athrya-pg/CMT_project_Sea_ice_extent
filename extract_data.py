## Extract the data we need from the datasets from the internet

# import the libraries needed
import pandas as pd
import matplotlib.pyplot as plt

# Read the Excel file into a DataFrame
df_nh = pd.read_excel('Sea_Ice_Index_Monthly_Data_by_Year_G02135_v3.0.xlsx', sheet_name='NH-Extent')  # Adjust the sheet_name as needed
df_sh = pd.read_excel('Sea_Ice_Index_Monthly_Data_by_Year_G02135_v3.0.xlsx', sheet_name='SH-Extent') 
df_co2 = pd.read_excel('IEA_EDGAR_CO2_1970_2023.xlsx', sheet_name='IPCC 2006')

# Display the DataFrame
# print(df_nh.head())
# print(df_sh.head())
# print(df_co2.head())

# Define the columns and rows we want
df_nhcut= df_nh.iloc[1:46,14:15]
df_shcut= df_sh.iloc[1:46,14:15]
df_co2cut= df_co2.iloc[9:3539, 17:62].reset_index(drop=True)

print('new dataframe')
# print(df_nhcut.head(45))
print(df_co2cut.head())

sum_co2 = df_co2cut.sum()
sum_co2_df = pd.DataFrame(sum_co2, columns=['CO2_Mass'])

# index_range = [x +1979 for x in index_range]
years = list(range(1979, 2024))
sum_co2_df['Year'] = years
df_nhcut['Year'] = years
df_shcut['Year'] = years

print('sum df table')
print(sum_co2_df)

#sum_co2 = sum_co2_df.groupby('Year').sum()
#print(sum_co2.head())

#mmmm

print('creating csv file')
df_nhcut.to_csv('sea_ice_nh.csv', index=False)
df_shcut.to_csv('sea_ice_sh.csv', index=False)
sum_co2_df.to_csv('summed_co2.csv', index=False)


# Plot les correlation 
# Plot sea ice nh x co2

'''
# Plot sea ice sh x co2
sum_co2 = df_co2cut.groupby('Year').sum()
print(sum_co2.head())


# Add a 'Year' column
years = list(range(1979, 2024))
df_nhcut['Year'] = years
df_shcut['Year'] = years
sum_co2['Year'] = years
'''

# Rename columns for clarity
df_nhcut.columns = ['NH_Extent', 'Year']
df_shcut.columns = ['SH_Extent', 'Year']
sum_co2_df.columns = ['CO2_Mass', 'Year']


# Merge the DataFrames on the 'Year' column
merged_nh = pd.merge(df_nhcut, sum_co2_df, on='Year')
merged_sh = pd.merge(df_shcut, sum_co2_df, on='Year')

# Plot the data
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Plot NH Sea Ice Extent vs CO2 Mass
ax1.plot(merged_nh['Year'], merged_nh['NH_Extent'], color='blue', label='NH Sea Ice Extent')
ax1.set_xlabel('Year')
ax1.set_ylabel('NH Sea Ice Extent (million sq km)', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')

ax1_twin = ax1.twinx()
ax1_twin.plot(merged_nh['Year'], merged_nh['CO2_Mass'], color='red', label='CO2 Mass')
ax1_twin.set_ylabel('CO2 Mass (Gt)', color='red')
ax1_twin.tick_params(axis='y', labelcolor='red')

ax1.set_title('NH Sea Ice Extent and CO2 Mass Over Time')
ax1.legend(loc='upper left')
ax1_twin.legend(loc='upper right')

# Plot SH Sea Ice Extent vs CO2 Mass
ax2.plot(merged_sh['Year'], merged_sh['SH_Extent'], color='green', label='SH Sea Ice Extent')
ax2.set_xlabel('Year')
ax2.set_ylabel('SH Sea Ice Extent (million sq km)', color='green')
ax2.tick_params(axis='y', labelcolor='green')

ax2_twin = ax2.twinx()
ax2_twin.plot(merged_sh['Year'], merged_sh['CO2_Mass'], color='red', label='CO2 Mass')
ax2_twin.set_ylabel('CO2 Mass (Gt)', color='red')
ax2_twin.tick_params(axis='y', labelcolor='red')

ax2.set_title('SH Sea Ice Extent and CO2 Mass Over Time')
ax2.legend(loc='upper left')
ax2_twin.legend(loc='upper right')

# Show plot
plt.tight_layout()
plt.show()





