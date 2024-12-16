# COMPUTATIONAL METHODS AND TOOLS - PROJECT 

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
- "*docs/*" contains informations on the datasets
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
  - Computes to extract data from the year 1979 to the year 2023, it takes Sea Ice Extent, CO2 emissions, ... which are stored in two files, one for the Northern Hemisphere and for the Southern Hemisphere.
- "*Main.c*":
  - Uses the other .c programs in "*src/*". They define various function to calculate the linear regression, quadratic regression, multiple regression, calculate R squared and calculate RMSE.
  - After the calculations, it stores the estimated y values, "*regression_results.txt*" containing the regression models and the R squared and RMSE values for each in "*outputs/*" and the residuals in "*processed_data/*".
- "*Significance_Tests.py*":
  - //////////////////////////////////////////////////////////////////////////////////// NOT SURE, PLEASE COMPLETE <3 ///////////////////////////////
- "*Visualisation.py*":
  - Plots the different regressions for each hemisphere and puts them in "*outputs/*".
- "*Predictions.py*":
  - Plots 3 different prediction scenarios; SSP1, SSP3 and SSP5. They are also stored in outputs.


## Instructions

To reproduce results in the report, these steps should be followed:

1. Go to the makefile to ensure the Python interpreter selected is yours (eg. PYTHON = your_python_interpreter_path).
2. Open the terminal from the project root directory (location of this README.md file). You can check this is the case by typing:
    ```
    ls
    ```
    The terminal should return:
    ```
    data  docs  makefile  README.md  src
    ```
3. Run the following line in the terminal:
    ```
    make
    ```
The program will run automatically, and will open a plotting window with 2 graphs. 
Once you close the window, the program cleans up (eg. the executable file) and terminates automatically.

## Requirements
///////////////////////////////////////////////////////////////////////////////////////////////////// STILL NEED TO CHANGE ///////////////////////////
**Python**
Versions of Python used: 
```
$ python --version
Python 3.12.2
```

Tools/Modules required: 
- os
- pandas
- numpy
- matplotlib.pyplot
- matplotlib.ticker import MaxNLocator
- scipy.interpolate import interp1d
- scipy.stats

**C**
Version of C used:
```
$ gcc --version
gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
```

Tools/Modules required:
- <stdio.h>
- <math.h>
- <string.h>
- <stdlib.h>

**In case of errors**
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

**To check the packages already installed:**
Use:
```
conda list
```

## Credits
///////////////////////////////////////////////////////////////////////////////////////////////////// STILL NEED TO CHANGE ///////////////////////////

Us crediting??? CHECKKKKKKKKKK!!!!!!!!!!!!!!!


`teacher comment`
Using the `sys.path[0]` and `ROOT` convention as shown in this project example circumvents this ambiguity by anchoring all paths to `ROOT`.


