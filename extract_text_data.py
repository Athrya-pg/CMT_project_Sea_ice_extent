## Extract Data from Text File
import pandas as pd

data_folder = 'data/'
output_folder = 'outputs/'

# Create input and output file
input = 'aravg.ann.ocean.90S.60S.v6.0.0.202410.asc'
output = 'ocean_temp_annual_SPole.csv'

list_entries = []
# Reading an ASCII file
with open(data_folder + input, 'r') as file:
    content = file.readlines()
    #print(content)
    for line in content:
        #print(line.strip())
        list_entries.append(line.strip())
#print(list_entries)

split_data = []

for row in list_entries:
    values = row.strip().split()
    years = values[0]
    for i,value in enumerate(values[1:]):
        split_data.append([f'{years}',value])

temp_df = pd.DataFrame(split_data, columns=['Year','Temperature'])
#if temp_df['Value'] == '-999.000000':
temp_df = temp_df[temp_df['Temperature'] != '-999.000000']
temp_df.reset_index(drop=True, inplace=True)

#print(temp_df[120:130])

ocean_temp_cut = temp_df[129:174]
ocean_temp_cut.reset_index(drop=True, inplace=True)
print(ocean_temp_cut)

ocean_temp_cut.to_csv(output_folder + output, index=False)
print('Accomplished.')



'''
# Read the text file
with open(data_folder + input, 'r') as file:
    rows = file.readlines()

#print(rows[:5])

# Remove headers and things
data_rows = rows[116:161]

# print(data_rows[-5:])
# print(data_rows[:5])

# Select the wanted data
months = ['01','02','03','04','05','06','07','08', '09','10','11','12']
timeXdata = []

for row in data_rows:
    values = row.strip().split()
    years = values[0]
    for i,value in enumerate(values[1:]):
        timeXdata.append([f'{years}-{months[i]}',value])

#print(timeXdata[:5])

# Make into a dataframe
nino_df = pd.DataFrame(timeXdata, columns=['Date','Std_Value'])

# Convert to CSV file
nino_df.to_csv(output_folder+output, index=False)
'''


