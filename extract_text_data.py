## Extract Data from Text File
import pandas as pd

data_folder = 'data/'
output_folder = 'outputs/'

# Create input and output file
input = 'nino'
output = 'nino.csv'

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



