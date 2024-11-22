## Extract the data we need from the datasets from the internet

# import the libraries needed
import pandas as pd

# Read the Excel file into a DataFrame
df_nh = pd.read_excel('Sea_Ice_Index_Monthly_Data_by_Year_G02135_v3.0.xlsx', sheet_name='NH-Extent')  # Adjust the sheet_name as needed
df_sh = pd.read_excel('Sea_Ice_Index_Monthly_Data_by_Year_G02135_v3.0.xlsx', sheet_name='SH-Extent') 
df_co2 = pd.read_excel('IEA_EDGAR_CO2_1970_2023.xlsx', sheet_name='IPCC 2006')

# Display the DataFrame
# print(df_nh.head())
# print(df_sh.head())
# print(df_co2.head())

# Define the columns and rows we want
df_nhcut= df_nh.iloc[2:48,15:16]
df_shcut= df_sh.iloc[2:48,15:16]
df_co2cut= df_co2.iloc[9:3539, 17:63]

print('new dataframe')
print(df_nhcut.head())
# print(df_co2cut.head())

sum_co2 = df_co2cut.sum()

print('sum df table')
print(sum_co2)

print('creating csv file')
# sum_co2.to_csv('summed_co2.csv', index=False)







