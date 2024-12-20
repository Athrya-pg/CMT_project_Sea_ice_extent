// ============================================================================================
// Description: This function calculates the linear regression between two variables x and y.
// ============================================================================================

// Loading libraries
#include <stdio.h>
#include <math.h>

// Function to calculate the linear regression: y = mx + b
// y is the sea ice extent
// x is the co2 emissions
void Linear_Regression(double *x, double *y, int n, double *m, double *b){
    // Initialise variables
    double sum_x = 0, sum_y = 0, sum_xy = 0, sum_x2 = 0;
    ///////////////////////////////////////////////////////////////////////////////////Add comment??? or too much?
    for(int i = 0; i < n; i++){
        sum_x += x[i];
        sum_y += y[i];
        sum_xy += x[i] * y[i];
        sum_x2 += x[i] * x[i];
    }
    // Calculate the coefficient and the intercept
    *m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x);
    *b = (sum_y - *m * sum_x) / n;
}