//=====================================================================================
// Description: This file contains the function to calculate the quadratic regression
//=====================================================================================

#include <stdio.h>
#include <math.h>

// Function to calculate the quadratic regression: y = ax^2 + bx + c
// y is the dependent variable (sea ice extent)
// x is the independent variable (CO2 emissions)
// n is the number of data points
// a, b, and c are the coefficients of the quadratic regression
void Quadratic_Regression(double *x, double *y, int n, double *a, double *b, double *c){
    // Check for invalid inputs
    if (x == NULL || y == NULL || a == NULL || b == NULL || c == NULL || n <= 0) {
        fprintf(stderr, "Error: Invalid inputs.\n");
        return;
    }

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

    // Solve the system of equations using determinants
    double det = n * (sum_x2 * sum_x4 - sum_x3 * sum_x3)
                - sum_x * (sum_x * sum_x4 - sum_x2 * sum_x3)
                + sum_x2 * (sum_x * sum_x3 - sum_x2 * sum_x2);

    double det_c = sum_y * (sum_x2 * sum_x4 - sum_x3 * sum_x3)
                 - sum_x * (sum_xy * sum_x4 - sum_x2y * sum_x3)
                 + sum_x2 * (sum_xy * sum_x3 - sum_x2y * sum_x2);

    double det_b = n * (sum_xy * sum_x4 - sum_x2y * sum_x3)
                 - sum_y * (sum_x * sum_x4 - sum_x2 * sum_x3)
                 + sum_x2 * (sum_x * sum_x2y - sum_xy * sum_x2);

    double det_a = n * (sum_x2 * sum_x2y - sum_x3 * sum_xy)
                 - sum_x * (sum_x * sum_x2y - sum_x2 * sum_xy)
                 + sum_y * (sum_x * sum_x3 - sum_x2 * sum_x2);
    if (det == 0) {
        fprintf(stderr, "Error: Determinant is zero, cannot solve the system.\n");
    return;
    }

    *c = det_c / det;
    *b = det_b / det;
    *a = det_a / det;
}