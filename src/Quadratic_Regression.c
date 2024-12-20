//=====================================================================================
// Description: This file contains the function to calculate the quadratic regression
//=====================================================================================

// Loading libraries
#include <stdio.h>
#include <math.h>

// Function to calulate the quadratic regression: y = ax^2 + bx + c
// y is the sea ice extent
// x is the CO2 emissions
void Quadratic_Regression(double *x, double *y, int n, double *a, double *b, double *c){
    double sum_x = 0, sum_y = 0, sum_x2 = 0, sum_x3 = 0, sum_x4 = 0;
    double sum_xy = 0, sum_x2y = 0;

    // Calculate the sums
    for(int i = 0; i < n; i++){
        sum_x += x[i];
        sum_y += y[i];
        sum_x2 += x[i] * x[i];
        sum_x3 += x[i] * x[i] * x[i];
        sum_x4 += x[i] * x[i] * x[i] * x[i];
        sum_xy += x[i] * y[i];
        sum_x2y += x[i] * x[i] * y[i];
    }
     // Solve the system of equations
    double det = n * (sum_x2 * sum_x4 - sum_x3 * sum_x3)
                - sum_x * (sum_x * sum_x4 - sum_x2 * sum_x3)
                + sum_x2 * (sum_x * sum_x3 - sum_x2 * sum_x2);

    double det_a = sum_y * (sum_x2 * sum_x4 - sum_x3 * sum_x3)
                 - sum_x * (sum_xy * sum_x4 - sum_x2y * sum_x3)
                 + sum_x2 * (sum_xy * sum_x3 - sum_x2y * sum_x2);

    double det_b = n * (sum_xy * sum_x4 - sum_x2y * sum_x3)
                 - sum_y * (sum_x * sum_x4 - sum_x2 * sum_x3)
                 + sum_x2 * (sum_x * sum_x2y - sum_xy * sum_x2);

    double det_c = n * (sum_x2 * sum_x2y - sum_x3 * sum_xy)
                 - sum_x * (sum_x * sum_x2y - sum_x2 * sum_xy)
                 + sum_y * (sum_x * sum_x3 - sum_x2 * sum_x2);

    *a = det_a / det;
    *b = det_b / det;
    *c = det_c / det;
}

    // // Solve the system of equations
    // double det = n * (sum_x2 * sum_x4 - sum_x3 * sum_x3)
    //                    - sum_x * (sum_x * sum_x4 - sum_x2 * sum_x3)
    //                    + sum_x2 * (sum_x * sum_x3 - sum_x2 * sum_x2);

    // *a = (n * (sum_x2 * sum_x2y - sum_x3 * sum_xy)
    //     - sum_x * (sum_x * sum_x2y - sum_x2 * sum_xy)
    //     + sum_x2 * (sum_x * sum_xy - sum_x2 * sum_y)) / det;

    // *b = (n * (sum_xy * sum_x4 - sum_x3 * sum_x2y)
    //     - sum_x2 * (sum_x * sum_x4 - sum_x3 * sum_x3)
    //     + sum_x2 * (sum_x * sum_x2y - sum_x2 * sum_y)) / det;

    // *c = (sum_y * (sum_x2 * sum_x4 - sum_x3 * sum_x3)
    //     - sum_x * (sum_xy * sum_x4 - sum_x3 * sum_x2y)
    //     + sum_x2 * (sum_xy * sum_x3 - sum_x2y * sum_x2)) / det;



