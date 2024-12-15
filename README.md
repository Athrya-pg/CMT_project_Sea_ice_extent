# COMPUTATIONAL METHODS AND TOOLS - PROJECT 

## Project Description

This program explores the relationship between sea ice extent and environmental factors such as CO2 emissions, temperature, and precipitation over the period from 1979 to 2023. Using data from both hemispheres, we discover a strong linear correlation between Arctic sea ice extent and global CO2 emissions which allows us to make future predictions through a simple regression. However, Antarctic sea ice extent proves more complex which makes us use a polynomial regression with multiple data inputs.

The program will:
1. Read in input
   - sea ice extent from the north and south hemisphere in "*data/Sea_Ice_index_Monthly_Data_by_Year_G02135.xlsx*",
   - CO2 yearly global emission data in "*data/IEA_EDGAR_CO2_1970_2023.xlsx*",
   - precipitation data in the southern hemisphere in "*data/precipitations.csv*", and
   - average annual ocean temperature in the southern hemisphere (60S.90S) "*data/aravg.ann.ocean.90S.60S.v6.0.0.202410.asc*".
2.   "*outputs/plausibilite.csv*". ///////////////////////////////////////////////////// COMPLETE FILE TYPE ///////////
3. Plot the table of plausibilities ("*outputs/plausibilite.png*").

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

///////////////////////////////////////////////////////////////////////// NEED TO ADD DOCS FOLDER??? Ask Paul ///////////////

### Implementation details
 
**Overview:**
- Python handles most of the I/O, which means pulling the data and formatting them into 2 distinct CSV documents; one for the Northern Hemisphere data and one for the Southern Hemisphere data. 
- The regression calculations are done by C.                            /// Use 'ctypes'??? "The C program is compiled to a shared library, which is called by Python via the `ctypes` module." original README.


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

1. Go to the makefile to ensure the Python interpreter selected is yours.
2. Open the terminal from the project root directory (location of this README.md file). You can check this is the case by typing:
    ```
    ls
    ```
    The terminal should return:
    ```
    
    ```
3. Run the following line in the terminal:
    ```
    make
    ```
The program will run automatically, and will open two plotting windows in full screen. Once you close them , the program cleans up compiled filed files and terminates automatically.

## Requirements

Versions of Python and C used are as follows. Optionally, the Quarto version is also included for rendering the "*docs/analysis.qmd*" file. 
```
$ python --version
Python 3.9.18

$ gcc --version
gcc (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0

$ quarto --version
1.3.450
```

The "*requirements.txt*" file for Python packages was generated with the command
```{sh}
conda list --export > requirements.txt
```
and deleting all but the relevant packages specifically used by this project.

## Credits

The code is adapted from the [solutions](https://sieprog.ch/#c/pollution/solutions) of sieprog.ch.

## (***Extra notes for students***)

### Regarding relative paths

When running python scripts from the command line:
```{bash}
python src/simulategrid.py
```
the working directory of the Python program is the project root (the location of this README.md file) and not "*src/*". 

When running the Python program after changing into the "*code/*" directory,
```{bash}
cd src
python simulategrid.py
```
the working directory is "*src/*". (A word of caution - changing directories multiple times in shell scripts can be tricky since the program may end up in a different working directory than intended if any of the programs that are called exit with error.)

The important point is that relative paths to input files and other files/directories should be relative to the working directory. 

- If the Python program is run from the root directory, the relative path to "*capteurs.csv*" is "*data/capteurs.csv*". 
- If the Python program is run from the "*code/*" directory, the relative path to "*capteurs.csv*" is "*../data/capteurs.csv*". 

Using the `sys.path[0]` and `ROOT` convention as shown in this project example circumvents this ambiguity by anchoring all paths to `ROOT`.

### Regarding the build process

Note that to build on Windows, the "*Makefile*" line 
```{lang-makefile}
CFLAGS=-Wall -fPIC -O2
```
should be replaced with
```{lang-makefile}
CFLAGS=-Wall -fPIC -O2 -Dsrandom=srand -Drandom=rand
```
to account for the fact that `srand` and `rand` are to be used in place of `srandom` and `random`, respectively. It is possible to further automate this substitution by writing conditional statements in the "*Makefile*" based on the operating system - e.g.,
```{lang-makefile}
ifeq ($(OS), Windows_NT)
    CCFLAGS += -Dsrandom=srand -Drandom=rand
endif
```
Alteratively create separate makefiles for each operating system - e.g., "*Makefile.win*" and "*Makefile.linux*" and so on, and the user must rename the appropriate file on their machine to "*Makefile*" before calling `make`.

The "*Makefile*" is a general build tool and is useful for projects with many files that need to be compiled. For simple cases, you can create a shell script called, for instance, "*build.bash*" in the root directory with the following contents:
```{bash}
#!/bin/bash
mkdir -p bin
gcc -Wall -fPIC -O2 -o bin/cmain.o -c code/cmain.c
gcc -Wall -fPIC -O2 -o bin/cfunctions.o -c code/cfunctions.c -lm
gcc -shared -o bin/clib.so bin/cmain.o bin/cfunctions.o
```
Then, the library files can be built with 
```{bash}
bash build.bash
```
before running `bash run.bash`.

