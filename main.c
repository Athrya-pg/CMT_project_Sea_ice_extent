// Sea Ice project : 
//  ===================================================================================================================
// Objective = explain sea ice extent depending on explanatory variables such as greenhouse gas emissions, temperature
// Last update : Chloe Prats Genre (EPFL)
// date : 08/12/2024


// Loading libraries and packages
#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

#include "Linear_Regression.c"
#include "Quadratic_Regression.c"
#include "calculate_RMSE.c"
#include "calculate_R2.c"
#include "multiple_regression.c"
// #include "significance_tests.c"

// Define data read function
int read_data_nh(const char *filename, double *year, double *sea_ice_extent, double *co2, int max_size){
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error opening the file");
        return -1;
    }
    // Ignore the first line (header)
    char buffer[256];  // used to temporarily store lines from the csv file (256 characters max)
    if (fgets(buffer, sizeof(buffer), file) == NULL) {
        fprintf(stderr, "Error reading header from %s\n", filename);
        fclose(file);
        return -1;
    }
    int count = 0;
    while (count < max_size && fgets(buffer, sizeof(buffer), file) != NULL) {
        if (sscanf(buffer,"%lf,%lf,%lf", &year[count], &sea_ice_extent[count], &co2[count]) != 3) {
            fprintf(stderr, "Invalid data format at line %d in file %s\n", count + 2, filename);
            break;
        }
        // // Print the first few values for verification
        // if (count < 5) {
        //     printf("Read from %s: value = %lf, time = %lf\n", filename, values[count], time[count]);
        // }
        count++;
    }
    fclose(file);
    return count;
}

int read_data_sh(const char *filename, double *year, double *sea_ice_extent, double *co2, double *precipitation, double *temperature, int max_size) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error opening the file");
        return -1;
    }
    // Ignore the first line (header)
    char buffer[256];  // used to temporarily store lines from the csv file (256 characters max)
    if (fgets(buffer, sizeof(buffer), file) == NULL) {
        fprintf(stderr, "Error reading header from %s\n", filename);
        fclose(file);
        return -1;
    }
    int count = 0;
    while (count < max_size && fgets(buffer, sizeof(buffer), file) != NULL) {
        if (sscanf(buffer, "%lf,%lf,%lf,%lf,%lf", &year[count], &sea_ice_extent[count], &co2[count], &precipitation[count], &temperature[count]) != 5) {
            fprintf(stderr, "Invalid data format at line %d in file %s\n", count + 2, filename);
            break;
        }
        // // Print the first few values for verification
        // if (count < 5) {
        //     printf("Read from %s: value = %lf, time = %lf\n", filename, values[count], time[count]);
        // }
        count++;
    }
    fclose(file);
    return count;
}

// Define Main function
int main(){
    // x are CO2 emissions
    // t is the time in years
    // yN and yS are sea_ice_extent for North and South hemisphere
    const int max_data_size = 100;

    double t[max_data_size];
    double x[max_data_size];

    double yN[max_data_size];

    double yS[max_data_size];
    double precipitation[max_data_size];
    double temp[max_data_size];

    int n_yN, n_yS;

    // X is useful for multiple regression for the southern hemisphere
    const int p = 4; // Number of predictors (including the intercept)
    double *X[max_data_size];
    for (int i = 0; i < max_data_size; i++) {
        X[i] = (double *)malloc(p * sizeof(double));
        X[i][0] = 1.0; // Intercept term
    }

    // double **X = (double **)malloc(max_data_size * sizeof(double *));
    // for (int i = 0; i < max_data_size; i++) {
    //     X[i] = (double *)malloc(p * sizeof(double));
    //     X[i][0] = 1.0; // Intercept term
    // }

    // Read data from the NH_Data.csv file
    n_yN = read_data_nh("outputs/NH_Data.csv", t, yN, x, max_data_size);
    if (n_yN <= 0) {
        printf("Error: no data in NH_Data.csv\n");
        return 1;
    }

    // Read data from the SH_Data.csv file
    n_yS = read_data_sh("outputs/SH_Data.csv", t, yS, x, precipitation, temp, max_data_size);
    if (n_yS <= 0) {
        printf("Error: no data in SH_Data.csv\n");
        return 1;
    }

    // Check if the number of data points is the same in all files
    if (n_yS != n_yN || n_yS <= 0) {
        printf("Error: Mismatch in the number of data points (%d vs %d)\n", n_yN, n_yS);
        return 1;
    }

    // Number of data points
    int n = n_yN;

    //Fill the X matrix for the southern hemisphere
    for (int i = 0; i < n; i++) {
        X[i][1] = x[i];
        X[i][2] = temp[i];
        X[i][3] = precipitation[i];
    }

// ********************************************************************************************************************
    // Estimations
// ********************************************************************************************************************
    // Linear regression for Northern hemisphere
    double mN, bN;
    Linear_Regression(x, yN, n, &mN, &bN);

    // Linear regression for Southern hemisphere
    double mS, bS;
    Linear_Regression(x, yS, n, &mS, &bS);

    // Quadratic regression for Southern hemisphere
    double aS, cS, dS;
    Quadratic_Regression(x, yS, n, &aS, &cS, &dS);

    // Multiple regression for Southern Hemisphere
    double coefficients[p];
    multiple_regression(X, yS, n, p, coefficients);

//********************************************************************************************************************
    // Output the results
    printf("********************************************************************************************************************\n");
    printf("Northern Hemisphere, linear regression model: y = %lf * x + %lf\n", mN, bN);
    printf("Southern Hemisphere, linear regression model: y = %lf * x + %lf\n", mS, bS);
    printf("Southern Hemisphere, quadratic regression model: y = %lf * x^2 + %lf * x + %lf\n", aS, cS, dS);
    printf("Southern Hemsiphere, multiple regression model: y = %lf + %lf * x + %lf * temp + %lf * precip\n", coefficients[0], coefficients[1], coefficients[2], coefficients[3]);
    // Print coefficients
    printf("Coefficients:\n");
    for (int i = 0; i < p; i++) {
        printf("b%d = %lf\n", i, coefficients[i]);
    }
    printf("********************************************************************************************************************\n");

    // Predictions and errors for Northern hemisphere
    double yN_estim[max_data_size];
    // Write the estimations to the file
    for (int i = 0; i < n; i++) {
        yN_estim[i] = mN * x[i] + bN;
    }
    double RMSE_N = calculate_rmse(yN, yN_estim, n);
    double R2_N = calculate_R2(yN, yN_estim, n);
    printf("Northern Hemisphere RMSE: %f\n", RMSE_N);
    printf("Northern Hemisphere R2: %f\n", R2_N);

    // Estimation for Linear and Quadratic regression and errors for Southern hemisphere
    double yS_estim_lin[max_data_size];
    double yS_estim_poly[max_data_size];
    double yS_estim_multi[max_data_size];
    for (int i = 0; i < n; i++) {
        yS_estim_lin[i] = mS * x[i] + bS;
        yS_estim_poly[i] = aS * x[i] * x[i] + cS * x[i] + dS;
        yS_estim_multi[i] = coefficients[0] + coefficients[1] * x[i] + coefficients[2] * temp[i] + coefficients[3] * precipitation[i];
    }
    // Calculate the RMSE and R2
    double RMSE_S = calculate_rmse(yS, yS_estim_lin, n);
    double R2_S = calculate_R2(yS, yS_estim_lin, n);
    printf("Southern Hemisphere RMSE (Linear): %f\n", RMSE_S);
    printf("Southern Hemisphere R2 (Linear): %f\n", R2_S);

    // double RMSE_S_poly = calculate_rmse(yS, yS_estim_poly, n);
    // double R2_S_poly = calculate_R2(yS, yS_estim_poly, n);
    // printf("Southern Hemisphere RMSE (Quadratic): %f\n", RMSE_S_poly);
    // printf("Southern Hemisphere R2 (Quadratic): %f\n", R2_S_poly);

    double RMSE_S_multi = calculate_rmse(yS, yS_estim_multi, n);
    double R2_S_multi = calculate_R2(yS, yS_estim_multi, n);
    printf("Southern Hemisphere RMSE (Multiple regression): %f\n", RMSE_S_multi);
    printf("Southern Hemisphere R2 (Multiple regression): %f\n", R2_S_multi);
    printf("********************************************************************************************************************\n");
// ********************************************************************************************************************
    // Create a file to store the estimations
    FILE *file = fopen("outputs/yestimations.csv", "w");
    if (file == NULL) {
        printf("Error opening the file\n");
        return 1;
    }

    fprintf(file, "Year,Estim_North_linReg,Estim_South_LinReg,Estim_South_multiReg,Estim_South_polyReg\n");
    for (int i = 0; i < n; i++) {
        fprintf(file, "%.0f,%.3f,%.3f,%.3f,%.3f\n", t[i], yN_estim[i], yS_estim_lin[i], yS_estim_multi[i], yS_estim_poly[i]);
    }
    printf("Estimations saved in yestimations.csv\n");
    fclose(file);

    // Write the coefficients to the file
    FILE *coeff_file = fopen("outputs/coefficients.txt", "w");
    if (coeff_file == NULL) {
        printf("Error opening the coefficients file\n");
        return 1;
    }
    fprintf(coeff_file, "mN=%e\nbN=%lf\n", mN, bN);
    for (int i = 0; i < p; i++) {
        fprintf(coeff_file, "b%d=%lf\n", i, coefficients[i]);
    }
    fclose(coeff_file);
    printf("Coefficients saved in coefficients.txt\n");

    for (int i = 0; i < max_data_size; i++) {
        free(X[i]);
    }

    // ********************************************************************************************************************
    // Calculate the residuals
    // Residuals are the differences between observed and estimated values, used to assess the accuracy of the model
    double residuals_N[max_data_size];
    for (int i = 0; i < n; i++) {
        residuals_N[i] = yN[i] - yN_estim[i];
    }
    double residuals_S[max_data_size];
    for (int i = 0; i < n; i++) {
        residuals_S[i] = yS[i] - yS_estim_lin[i];
    }
    printf("********************************************************************************************************************\n");
    printf("Residuals calculated\n");
    // Write residuals to a file
    FILE *residuals_file = fopen("outputs/residuals.csv", "w");
    if (residuals_file == NULL) {
        printf("Error opening the residuals file\n");
        return 1;
    }
    fprintf(residuals_file, "Year,Residual_North,Residual_South\n");
    for (int i = 0; i < n; i++) {
        fprintf(residuals_file, "%.0f,%.3f,%.3f\n", t[i], residuals_N[i], residuals_S[i]);
    }
    printf("Residuals saved in residuals.csv\n");  
// ********************************************************************************************************************
    // // Calculate standard errors and p-values
    // double se_mN, se_bN;
    // double se_mS, se_bS;
    // calculate_standard_errors(x, yN, n, mN, bN, &se_mN, &se_bN);
    // calculate_standard_errors(x, yS, n, mS, bS, &se_mS, &se_bS);
    // //North
    // double t_value_mN = mN / se_mN;
    // double t_value_bN = bN / se_bN;
    // double p_value_mN = calculate_p_value(t_value_mN, n - 2);
    // double p_value_bN = calculate_p_value(t_value_bN, n - 2);
    // printf("Northern Hemisphere: Coefficient m: %lf, Standard Error: %lf, t-value: %lf, p-value: %lf\n", mN, se_mN, t_value_mN, p_value_mN);
    // printf("Northern Hemisphere: Coefficient b: %lf, Standard Error: %lf, t-value: %lf, p-value: %lf\n", bN, se_bN, t_value_bN, p_value_mN);
    // // South
    // double t_value_mS = mS / se_mS;
    // double t_value_bS = bS / se_bS;
    // double p_value_mS = calculate_p_value(t_value_mS, n - 2);
    // double p_value_bS = calculate_p_value(t_value_bS, n - 2);
    // printf("Southern Hemisphere: Coefficient m: %lf, Standard Error: %lf, t-value: %lf, p-value: %lf\n", mS, se_mS, t_value_mS, p_value_mS);
    // printf("Southern Hemisphere: Coefficient b: %lf, Standard Error: %lf, t-value: %lf, p-value: %lf\n", bS, se_bS, t_value_bS, p_value_mS);

    // // Calculate the F-statistic and p-value for the regression model
    // double f_statistic_N = calculate_f_statistic(R2_N, n, 2);
    // double p_value_N = calculate_p_value(f_statistic_N, n - 2);
    // printf("Northern Hemisphere: F-statistic: %lf, p-value: %lf\n", f_statistic_N, p_value_N);

    // double f_statistic_S = calculate_f_statistic(R2_S, n, 2);
    // double p_value_S = calculate_p_value(f_statistic_S, n - 2);
    // printf("Southern Hemisphere: F-statistic: %lf, p-value: %lf\n", f_statistic_S, p_value_S);

    // // Test the significance of the coefficients
    // t_test_significance(x, yN, n, mN, bN);
    // t_test_significance(x, yS, n, mS, bS);
    
//********************************************************************************************************************
    // Calculate F-statistic and p-value for the overall model for Northern Hemisphere
    // double f_stat_N = calculate_f_statistic(yN, yN_pred, n, 2);
    // double f_p_value_N = calculate_f_p_value(f_stat_N, 1, n - 2);

    // printf("Northern Hemisphere: F-statistic: %lf, p-value: %lf\n", f_stat_N, f_p_value_N);

    // // Calculate F-statistic and p-value for the overall model for Southern Hemisphere
    // double f_stat_S = calculate_f_statistic(yS, yS_pred, n, 2);
    // double f_p_value_S = calculate_f_p_value(f_stat_S, 1, n - 2);

    // printf("Southern Hemisphere: F-statistic: %lf, p-value: %lf\n", f_stat_S, f_p_value_S);


    return 0;
}

