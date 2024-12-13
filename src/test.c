#include <stdio.h>
#include <math.h>
#include <gsl/gsl_cdf.h>

// Test t with GSL
double calculate_p_value_t(double t_stat, int degrees_of_freedom) {
    double t_p_value = 2 * (1.0 - gsl_cdf_tdist_P(fabs(t_stat), degrees_of_freedom));
    return t_p_value;
}

// Test F with GSL
double calculate_p_value_f(double f_stat, int dfn, int dfd) {
    double f_p_value = 1.0 - gsl_cdf_fdist_P(f_stat, dfn, dfd);
    return f_p_value;
}


void regression_analysis(double* beta, double* se, int n, int k, double alpha) {
    int df = n - k - 1; // Degrés de liberté
    for (int i = 0; i < k; i++) {
        double t_stat = beta[i] / se[i]; // Statistique t
        double p_value = 2 * (1 - gsl_cdf_tdist_P(fabs(t_stat), df)); // P-valeur bilatérale

        printf("Coefficient %d:\n", i);
        printf("  SE: %.5f\n", se[i]);
        printf("  t-stat: %.5f\n", t_stat);
        printf("  p-value: %.5f\n", p_value);

        if (p_value < alpha) {
            printf("  Significatif au niveau %.2f\n", alpha);
        } else {
            printf("  Non significatif au niveau %.2f\n", alpha);
        }
    }
}
