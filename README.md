# COMPUTATIONAL METHODS AND TOOLS - PROJECT 
Authors: BÄCHLER Alicia and PRATS-GENRE Chloé
## Project Description

This program explores the relationship between sea ice extent and environmental factors such as CO2 emissions, temperature, and precipitation over the period from 1979 to 2023. Using data from both hemispheres, we discover a strong linear correlation between Arctic sea ice extent and global CO2 emissions which allows us to make future predictions through a simple regression. However, Antarctic sea ice extent proves more complex which makes us use a polynomial regression with multiple data inputs.

The program will:
1. Read in input
   - sea ice extent from the north and south hemisphere in "*data/Sea_Ice_index_Monthly_Data_by_Year_G02135.xlsx*",
   - CO2 yearly global emission data in "*data/IEA_EDGAR_CO2_1970_2023.xlsx*",
   - precipitation data in the southern hemisphere in "*data/precipitations.csv*", and
   - average annual ocean temperature in the southern hemisphere (60S.90S) "*data/aravg.ann.ocean.90S.60S.v6.0.0.202410.asc*".
2. Calculates different types of regressions (linear, multiple and quadratics).
3. Calculate t-tests for the regressions ("*outputs/test_results.txt*").
4. Plots graphs, and save the figures in "*outputs*".
5. Make predictions for the Northern Hemisphere.


## Project structure

- "*data/*" contains input data
- "*outputs/*" contains program outputs
- "*processed_data/*" contains the intermidiate data tables 
- "*src/*" contains the program codes

### Inputs and outputs

Inputs:
- "*data/Sea_Ice_index_Monthly_Data_by_Year_G02135.xlsx*" is a Excel file. 
- "*data/IEA_EDGAR_CO2_1970_2023.xlsx*" is a Excel file.
- "*data/precipitations.csv*" is a comma-delimited file.
- "*data/aravg.ann.ocean.90S.60S.v6.0.0.202410.asc*" is a space-delimited file.

Processed Data: (once the code is run)
- "*processed_data/coefficient.txt*" is a text file
- "*processed_data/NH_Data.csv*" is comma-delimited file.
- "*processed_data/SH_Data.csv*" is comma-delimited file.
- "*processed_data/residuals.csv*" is comma-delimited file.

Outputs: (once the code is run)
- "*outputs/1_Correlations.png*" is a image file.
- "*outputs/2_Year_vs_IceExtent.png*" is an image file.
- "*outputs/3_NH_Linear_Regression_plot.png*" is an image file.
- "*outputs/4_SH_Linear_Regression_plot.png*" is an image file.
- "*outputs/5_SH_Quadratic_Regression_plot.png*" is an image file.
- "*outputs/6_SH_Multiple_Regression_plot.png*" is an image file.
- "*outputs/7_NH_Predictions.png*" is an image file.
- "*outputs/regression_results.txt*" is a text file.
- "*outputs/test_results.txt*" is a text file.
- "*outputs/yestimations.csv*" is a comma-delimited file.
 
### Implementation details
 
**Overview:**
- Python handles most of the I/O, which means pulling the data and formatting them into 2 distinct CSV documents; one for the Northern Hemisphere data and one for the Southern Hemisphere data. 
- The regression calculations are done by C. It stores the estimated values in "*outputs/*".
- Python handles the t-tests, visualisation and prediction.

**Structure:** In the directory "*src/*":
- "*Extract_Data.py*":
  - Reads in the files from "*data/*"
  - Computes to extract data from the year 1979 to the year 2023, it takes Sea Ice Extent, CO2 emissions and Precipitations and sea temperature in the Southern Hemisphere. They are stored in two files, one for the Northern Hemisphere and one for the Southern Hemisphere.
- "*Main.c*":
  - Uses the other .c programs in "*src/*". They define various function to calculate the linear regression, quadratic regression, multiple regression, calculate R squared and calculate RMSE.
  - After the calculations, it stores the estimated y values, "*regression_results.txt*" containing the regression models and the R squared and RMSE values for each in "*outputs/*" and the residuals in "*processed_data/*".
- "*Significance_Tests.py*":
  - Performs F-tests and t-tests using the loaded residuals.csv, and coefficients.txt to evaluate the significance of the regression model and its coefficients. It stores the test results in "*test_results.txt*" in "*outputs/*" .
- "*Visualisation.py*":
  - Plots the different regressions for each hemisphere and puts them in "*outputs/*".
- "*Predictions.py*":
  - Plots 3 different prediction scenarios; SSP1, SSP3 and SSP5. They are also stored in outputs.
    - SSP1: represents a sustainable trajectory with fast CO2 reductions and global cooperation.
    - SSP3: A fragmented world with high challenges to both mitigation and adaptation.
    - SSP5: A future world with high emissions, minimal cooperation, and significant warming.


## Instructions

To reproduce results in the report, these steps should be followed:

1. In the GitHub repository, click, on the right hand side, the green box calles "*<> Code*", and "*Download .zip*" and save in your local file manager.
2. Unzip the folder.
3. Edit the makefile at line 20 to change the Python interpreter to be your own. 
   For example:
   ```
    PYTHON = User/home/bin/python3
   ```
4. Open the terminal from the project root directory (location of this README.md file). You can check this is the case by typing:
    ```
    ls
    ```
    The terminal should return:
    ```
    data  makefile  README.md  src
    ```
5. Run the following line in the terminal:
    ```
    make
    ```
The program will run automatically, and will open a plotting window with 2 graphs. 
Once you close the window, the program cleans up (eg. the executable file) and terminates automatically.

## Requirements
It is important to note that the command 'make' is not compatible with Windows.
### **Python**
Versions of Python used: 
```
$ python --version
Python 3.12.2
```

Modules required: 
- os
- pandas
- numpy
- matplotlib
- scipy

**In case of errors** \
In case of a missing module.
Use:
 ```
 conda install {module name}
```
This should install the module.


In case of the following error:
MESA-LOADER: failed to open: iris / swrast

Use:
```
 conda install -c conda-forge libstdcxx-ng
```
**To check the packages already installed:** \
Use:
```
conda list
```

### **C** 
Version of C used:
```
$ gcc --version
gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
```

Libraries required:
- <stdio.h>
- <math.h>
- <string.h>
- <stdlib.h>


## Credits
### **Data**
- "*Sea_Ice_index_Monthly_Data_by_Year_G02135.xlsx*":
  - Fetterer, F., Knowles, K., Meier, W. N., Savoie, M. & Windnagel, A. K. (2017). Sea Ice Index. (G02135, Version 3). [Sea_Ice_index_Monthly_Data_by_Year_G02135]. Boulder, Colorado USA. National Snow and Ice Data Center. https://doi.org/10.7265/N5K072F8. [NH-Extent, SH-Extent]. Date Accessed 12-11-2024.

- "*IEA_EDGAR_CO2_1970_2023.xlsx*":
  - EDGAR (Emissions Database for Global Atmospheric Research) Community GHG Database a collaboration between the European Commission, Joint Research Centre (JRC), the International Energy Agency (IEA), and comprising IEA-EDGAR CO2, EDGAR CH4, EDGAR N2O, EDGAR F-GASES version EDGAR_2024_GHG (2024) European Commission. EDGAR report webpage (https://edgar.jrc.ec.europa.eu/report_2024) and EDGAR_2024_GHG website (https://edgar.jrc.ec.europa.eu/dataset_ghg2024)
  - IEA-EDGAR CO2 (v3), a component of the EDGAR (Emissions Database for Global Atmospheric Research) Community GHG database version EDGAR_2024_GHG (2024) including or based on data from IEA (2023) Greenhouse Gas Emissions from Energy, www.iea.org/statistics, as modified by the Joint Research Centre.

- "*precipitations.csv*":
  - NOAA National Centers for Environmental information, Climate at a Glance: Global Time Series, published December 2024, retrieved on November 12, 2024 from https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series 

- "*aravg.ann.ocean.90S.60S.v6.0.0.202410.asc*":
  - Huang, B., X. Yin, M. J. Menne, R. Vose, and H. Zhang, NOAA Global Surface Temperature Dataset (NOAAGlobalTemp), Version 6.0.0 [aravg.ann.ocean.90S.60S.v6.0.0.202410]. NOAA National Centers for Environmental Information. https://doi.org/10.25921/rzxg-p717

- SSP scenarios:
  - IPCC, 2023: Sections. In: Climate Change 2023: Synthesis Report. Contribution of Working Groups I, II and III to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change [Core Writing Team, H. Lee and J. Romero (eds.)]. IPCC, Geneva, Switzerland, pp. 35-115, doi: 10.59327/IPCC/AR6-9789291691647

### **Code**
In the code "*multiple_regression.c*": 
- Matrix Inversion (Gauss-Jordan Method):
  This implementation was inspired by the examples provided on Rosetta Code.
  - Link: [Gauss-Jordan Matrix Inversion - Rosetta Code](https://rosettacode.org/wiki/Gauss-Jordan_matrix_inversion)

Portions of this code were developed with the assistance of GitHub Copilot, which provided suggestions and solutions to improve and address issues. These suggestions were reviewed and adapted as needed to meet the project's requirements. Any similarity to third-party code is unintentional.


