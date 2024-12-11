## CSV Precipitation Data

import pandas as pd

data_folder = 'data/'
output_folder = 'outputs/'

# Create input and output file
input = 'precipitations.csv'
output = 'precipitation_adjusted.csv'

precipitation_df = pd.read_csv(data_folder + input, comment='#')


precipitation_df.rename(columns={'Anomaly' : 'Precipitation'}, inplace=True)
print(precipitation_df)

precipitation_df.to_csv(output_folder+output, index=False)
print('Executed.')

