#include <stdio.h>
#include <math.h>

// Function to calulate the quadratic regression
// y = ax^2 + bx + c
// y = b0x0^2 + b1x1 + b2x2 + c  avec par exemple x0 = CH4 et x1 = CO2 et x2 = N2O
// y is the sea ice extent
// x is the green gas emmisions

void Quadratic_Regression(double *x, double *y, int n,double *a, double *b, double *c){
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

    *a = (n * (sum_x2 * sum_x2y - sum_x3 * sum_xy)
        - sum_x * (sum_x * sum_x2y - sum_x2 * sum_xy)
        + sum_x2 * (sum_x * sum_xy - sum_x2 * sum_y)) / det;

    *b = (n * (sum_xy * sum_x4 - sum_x3 * sum_x2y)
        - sum_x2 * (sum_x * sum_x4 - sum_x3 * sum_x3)
        + sum_x2 * (sum_x * sum_x2y - sum_x2 * sum_y)) / det;

    *c = (sum_y * (sum_x2 * sum_x4 - sum_x3 * sum_x3)
        - sum_x * (sum_xy * sum_x4 - sum_x3 * sum_x2y)
        + sum_x2 * (sum_xy * sum_x3 - sum_x2y * sum_x2)) / det;
}



