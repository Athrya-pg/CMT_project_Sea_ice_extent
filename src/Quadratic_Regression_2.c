//=====================================================================================
// Description: This file contains the function to calculate the quadratic regression
//=====================================================================================

// Loading libraries
#include <stdio.h>
#include <stdlib.h>
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
    // Calculate the mean of x
    double mean_x = 0;
    for (int i = 0; i < n; i++) {
        mean_x += x[i];
    }
    mean_x /= n;

    // Center the x values
    double x_centered[n];
    for (int i = 0; i < n; i++) {
        x_centered[i] = x[i] - mean_x;
    }

    // Initialize the sums
    double sum_x = 0, sum_y = 0, sum_x2 = 0, sum_x3 = 0, sum_x4 = 0;
    double sum_xy = 0, sum_x2y = 0;

    // Calculate the sums
    for(int i = 0; i < n; i++){
        sum_x += x_centered[i];
        sum_y += y[i];
        sum_x2 += x_centered[i] * x_centered[i];
        sum_x3 += x_centered[i] * x_centered[i] * x_centered[i];
        sum_x4 += x_centered[i] * x_centered[i] * x_centered[i] * x_centered[i];
        sum_xy += x_centered[i] * y[i];
        sum_x2y += x_centered[i] * x_centered[i] * y[i];
    }
    printf("sum_x = %.6f, sum_y = %.6f, sum_x2 = %.6f, sum_x3 = %.6f, sum_x4 = %.6f\n", sum_x, sum_y, sum_x2, sum_x3, sum_x4);
    printf("sum_xy = %.6f, sum_x2y = %.6f\n", sum_xy, sum_x2y);

    // Solve the system of equations using determinants
    double det = n * (sum_x2 * sum_x4 - sum_x3 * sum_x3) - sum_x * (sum_x * sum_x4 - sum_x2 * sum_x3) + sum_x2 * (sum_x * sum_x3 - sum_x2 * sum_x2);

    if (det == 0) {
        fprintf(stderr, "Error: Determinant is zero, cannot solve the system.\n");
        return;
    }

    double det_a = sum_y * (sum_x2 * sum_x4 - sum_x3 * sum_x3) - sum_x * (sum_xy * sum_x4 - sum_x3 * sum_x2y) + sum_x2 * (sum_xy * sum_x3 - sum_x2 * sum_x2y);

    double det_b = n * (sum_xy * sum_x4 - sum_x3 * sum_x2y) - sum_y * (sum_x * sum_x4 - sum_x2 * sum_x3) + sum_x2 * (sum_x * sum_x2y - sum_xy * sum_x2);

    double det_c = n * (sum_x2 * sum_x2y - sum_x3 * sum_xy) - sum_x * (sum_x * sum_x2y - sum_x2 * sum_xy) + sum_y * (sum_x * sum_x3 - sum_x2 * sum_x2);

    printf("det = %.6f, det_a = %.6f, det_b = %.6f, det_c = %.6f\n", det, det_a, det_b, det_c);

    *a = det_a / det;
    *b = det_b / det;
    *c = det_c / det;
}

/*
int main() {
    double x[] = {-2, -1, 0, 1, 2}; // Independent variable
    double y[] = {17, 10, 5, 4, 7}; // Dependent variable based on y = 2x^2 - 3x + 5
    int n = 5; // Number of points

    double a, b, c;
    Quadratic_Regression(x, y, n, &a, &b, &c);

    printf("Expected coefficients: a=2, b=-3, c=5\n");
    printf("Computed coefficients: a=%.6f, b=%.6f, c=%.6f\n", c, b, a);
    double residual_sum = 0;
    for (int i = 0; i < n; i++) {
        double predicted_y = a * x[i] * x[i] + b * x[i] + c;
        double residual = y[i] - predicted_y;
        residual_sum += residual * residual; // Sum of squared residuals
    }
    printf("Residual Sum of Squares (RSS): %.6f\n", residual_sum);
    return 0;
}
*/