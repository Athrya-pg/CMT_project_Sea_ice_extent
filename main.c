#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include "Linear_Regression.c"
#include "calculate_RMSE.c"
#include "calculate_R2.c"

// Function pour read the data from the file
int read_data(const char *filename, double *values, double *time, int max_size){
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Error opening the file");
        return -1;
    }
    // Ignore the first line (header)
    char buffer[256];
    if (fgets(buffer, sizeof(buffer), file) == NULL) {
        fprintf(stderr, "Error reading header from %s\n", filename);
        fclose(file);
        return -1;
    }
    int count = 0;
    while (count < max_size && fgets(buffer, sizeof(buffer), file) != NULL) {
        if (sscanf(buffer, "%lf,%lf", &values[count], &time[count]) != 2) {
            fprintf(stderr, "Invalid data format at line %d in file %s\n", count + 2, filename);
            break;
        }
        count++;
    }

    fclose(file);
    return count;
}

int main(){
    // x are green gas emmisions
    // yN and yS are sea ice extent
    const int max_data_size = 1000;
    double t[max_data_size];
    double x[max_data_size]; 
    double yN[max_data_size];
    double yS[max_data_size];
    int n_x, n_yN;

    // Read data from sea ice
    int n_yS = read_data("sea_ice_sh.csv", yS, t, max_data_size);
    printf("n_yS = %d\n", n_yS);
    if (n_yS <= 0) {
        printf("Error: no data in sea_ice_sh.csv\n");
        return 1;
    }

    n_yN = read_data("sea_ice_nh.csv", yN, t, max_data_size);
    if (n_yN <= 0) {
        printf("Error: no data in sea_ice_nh.csv\n");
        return 1;
    }

    // Read data from GHG
    n_x = read_data("summed_co2.csv", x, t, max_data_size);
    if (n_x <= 0) {
        printf("Error : no data in summed_co2.csv\n");
        return 1;
    }

    // Check if the number of data points is the same
    if (n_x != n_yN || n_x != n_yS) {
        printf("Error: files don't have the same number of data points (%d vs %d vs %d).\n", n_x, n_yN, n_yS);
        return 1;
    }

    // Number of data points
    int n = n_x;

    // Calculate the linear regression for northern hemisphere
    double mN, bN;
    Linear_Regression(x, yN, n, &mN, &bN);

    // Calculate the linear regression for southern hemisphere
    double mS, bS;
    Linear_Regression(x, yS, n, &mS, &bS);

    // Output the results
    printf("Northern Hemisphere: y = %lf * x + %lf\n", mN, bN);
    printf("Southern Hemisphere: y = %lf * x + %lf\n", mS, bS);

    // Calculate the predictions and errors for northern hemisphere
    double yN_pred[max_data_size];
    for (int i = 0; i < n; i++) {
        yN_pred[i] = mN * x[i] + bN;
    }
    double RMSE_N = calculate_rmse(yN, yN_pred, n);
    double R2_N = calculate_r2(yN, yN_pred, n);
    printf("Northern Hemisphere RMSE: %f\n", RMSE_N);
    printf("Northern Hemisphere R2: %f\n", R2_N);

    // Calculate the predictions and errors for southern hemisphere
    double yS_pred[max_data_size];
    for (int i = 0; i < n; i++) {
        yS_pred[i] = mS * x[i] + bS;
    }
    double RMSE_S = calculate_rmse(yS, yS_pred, n);
    double R2_S = calculate_r2(yS, yS_pred, n);
    printf("Southern Hemisphere RMSE: %f\n", RMSE_S);
    printf("Southern Hemisphere R2: %f\n", R2_S);
    
    // // // calculate the mean squared error
    // double MSE = calculate_mse(y, y_pred, n);
    // printf("Mean Squared Error (MSE): %f\n", MSE);

    // // calculate the coefficient of determination
    // double R2 = calculate_r2(y, y_pred, n);
    // printf("Coefficient of determination (R2): %f\n", R2);

    return 0;
}

