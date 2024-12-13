#include <stdio.h>
#include <math.h>
#include <gsl/gsl_cdf.h>

// Function to calculate the p-value for a T-test using GSL
double calculate_p_value(double t, int degrees_of_freedom) {
    return 2.0 * gsl_cdf_tdist_Q(fabs(t), degrees_of_freedom);
}

// Function to calculate the p-value for the F-statistic using GSL
double calculate_f_p_value(double f_stat, int df1, int df2) {
    return gsl_cdf_fdist_Q(f_stat, df1, df2);
}



// // Fonction pour calculer la valeur p pour un test t à partir de la loi de Student
// // Utilise une approximation de la fonction cumulative
// double calculate_p_value_t(double t, int degrees_of_freedom) {
//     double x = fabs(t) / sqrt(degrees_of_freedom);
//     double p = 1.0 - (1.0 / (1.0 + 0.2316419 * x)) * 
//                       (0.3989422804 * exp(-x * x / 2.0) * 
//                       (0.31938153 + -0.356563782 * x + 1.781477937 * pow(x, 2) + -1.821255978 * pow(x, 3) + 1.330274429 * pow(x, 4)));
//     return 2.0 * (1.0 - p); // Bilatéral
// }

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

// Function to perform regression analysis and print results
void regression_analysis(double* beta, double* se, int n, int k, double alpha) {
    int df = n - k - 1; // Degrees of freedom
    for (int i = 0; i < k; i++) {
        double t_stat = beta[i] / se[i]; // t-statistic
        double p_value = 2 * (1 - gsl_cdf_tdist_Q(fabs(t_stat), df)); // Two-tailed p-value

        printf("Coefficient %d:\n", i);
        printf("  SE: %.5f\n", se[i]);
        printf("  t-stat: %.5f\n", t_stat);
        printf("  p-value: %.5f\n", p_value);

        if (p_value < alpha) {
            printf("  Significant at level %.2f\n", alpha);
        } else {
            printf("  Not significant at level %.2f\n", alpha);
        }
    }
}
