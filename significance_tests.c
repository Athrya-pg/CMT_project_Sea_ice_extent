#include <stdio.h>
#include <math.h>

// Function to approximate p-values with a normal distribution
double calculate_p_value(double t, int degrees_of_freedom) {
    // Uses an approximation (if necessary, replace with a library like GSL for more precision)
    return 2 * (1.0 - 0.5 * (1 + erf(fabs(t) / sqrt(2))));
}

// Function to calculate the standard errors of the regression coefficients
void calculate_standard_errors(double *x, double *y, int n, double m, double b, double *se_m, double *se_b) {
    double sum_x = 0, sum_x2 = 0, sum_y = 0, sum_y2 = 0, sum_xy = 0;
    for (int i = 0; i < n; i++) {
        sum_x += x[i];
        sum_x2 += x[i] * x[i];
        sum_y += y[i];
        sum_y2 += y[i] * y[i];
        sum_xy += x[i] * y[i];
    }
    double sst = sum_y2 - (sum_y * sum_y) / n;
    double ssr = m * (sum_xy - (sum_x * sum_y) / n) + b * sum_y;
    double sse = sst - ssr;
    double mse = sse / (n - 2); // mean squared error
    double sxx = sum_x2 - (sum_x * sum_x) / n; // sum of squares of x
    // se_m is the standard error of the slope
    // se_b is the standard error of the intercept
    *se_m = sqrt(mse / sxx);
    double mean_x = sum_x / n;
    *se_b = sqrt(mse * (1.0 / n + mean_x * mean_x / (sum_x2 - sum_x * mean_x)));
}

// Function to calculate the F-statistic
// to test the significance of the regression model
double calculate_f_statistic(double r2, int n, int k) {
    return ((r2 / (1 - r2)) * ((n - k - 1) / k));
}

// Function to test the significance of the coefficients
// Function to test the significance of the regression coefficients
// x: array of independent variable values
// y: array of dependent variable values
// n: number of data points
// m: slope of the regression line
// b: intercept of the regression line
void t_test_significance(double x[], double y[], int n, double m, double b) {
    double se_m, se_b;
    calculate_standard_errors(x, y, n, m, b, &se_m, &se_b);

    double t_m = m / se_m;
    double t_b = b / se_b;

    double p_value_m = calculate_p_value(t_m, n - 2);
    double p_value_b = calculate_p_value(t_b, n - 2);

    printf("Slope (m) p-value: %.6f\n", p_value_m);
    printf("Intercept (b) p-value: %.6f\n", p_value_b);
}
