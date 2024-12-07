## Adjust the data file
# By adjusting, it is not meant that we changed the data, we merly changed the setup
# of the data to match with the rest of our datasets.

import pandas as pd

data_folder = 'data/'
output_folder = 'outputs/'

# Create input and output file
input = 'aao.csv'
output = 'aao_adjusted.csv'

aao_df = pd.read_csv(data_folder + input)
aao_df.rename(columns={'  from AAO  missing value -9999 https://psl.noaa.gov/data/timeseries/month/': 'Std_AAO'}, inplace=True)

# Edit
aao_df['Date'] = aao_df['Date'].str.slice(0,-3)
aao_df['Std_AAO'] = aao_df['Std_AAO'].astype(str).str.strip()

#print(f'm{aao_df['Std_AAO'][1]}m')


# Save the edited DataFrame to a new CSV file
aao_df.to_csv(output_folder + output, index=False)





