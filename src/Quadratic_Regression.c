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
// NEW?
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 45 // Number of data points from 1979 to 2023

// Function to calculate quadratic regression coefficients
void quadratic_regression(double x[], double y[], int n, double *a, double *b, double *c) {
    double sum_x = 0, sum_x2 = 0, sum_x3 = 0, sum_x4 = 0;
    double sum_y = 0, sum_xy = 0, sum_x2y = 0;

    // Compute the required summations
    for (int i = 0; i < n; i++) {
        sum_x += x[i];
        sum_x2 += x[i] * x[i];
        sum_x3 += x[i] * x[i] * x[i];
        sum_x4 += x[i] * x[i] * x[i] * x[i];
        sum_y += y[i];
        sum_xy += x[i] * y[i];
        sum_x2y += x[i] * x[i] * y[i];
    }

    // Build the system of equations for quadratic regression
    double matrix[3][4] = {
        {n, sum_x, sum_x2, sum_y},
        {sum_x, sum_x2, sum_x3, sum_xy},
        {sum_x2, sum_x3, sum_x4, sum_x2y}
    };

    // Perform Gaussian elimination
    for (int i = 0; i < 3; i++) {
        for (int j = i + 1; j < 3; j++) {
            double factor = matrix[j][i] / matrix[i][i];
            for (int k = i; k < 4; k++) {
                matrix[j][k] -= factor * matrix[i][k];
            }
        }
    }

    // Back-substitution to solve for coefficients
    *c = matrix[2][3] / matrix[2][2];
    *b = (matrix[1][3] - matrix[1][2] * (*c)) / matrix[1][1];
    *a = (matrix[0][3] - matrix[0][2] * (*b) - matrix[0][1] * (*c)) / matrix[0][0];
}

int main() {
    // Example data (replace with your actual data)
    double x[N] = { /* CO2 data from 1979 to 2023 */ };
    double y[N] = { /* Sea ice extent data from 1979 to 2023 */ };

    double a, b, c;

    // Perform quadratic regression
    quadratic_regression(x, y, N, &a, &b, &c);

    // Print the results
    printf("Quadratic Regression Coefficients:\n");
    printf("a (x^2 term): %.5lf\n", a);
    printf("b (x term): %.5lf\n", b);
    printf("c (constant term): %.5lf\n", c);

    return 0;
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



