#include <stdio.h>
#include <math.h>

// Function to calculate the linear regression
// y = mx + b
// y = b0x0 + b1x1 + c with for example x0 = CH4 and x1 = CO2
// y is the sea ice extent
// x is the green gas emissions

void Linear_Regression(double *x, double *y, int n, double *m, double *b){
    double sum_x = 0, sum_y = 0, sum_xy = 0, sum_x2 = 0;
    for(int i = 0; i < n; i++){
        sum_x += x[i];
        sum_y += y[i];
        sum_xy += x[i] * y[i];
        sum_x2 += x[i] * x[i];
    }
    *m = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x);
    *b = (sum_y - *m * sum_x) / n;
}
    // // Calcul des résidus et de l'erreur standard
    // double sum_residuals = 0;
    // for (int i = 0; i < n; i++) {
    //     double y_pred = (*m) * x[i] + (*b);
    //     sum_residuals += (y[i] - y_pred) * (y[i] - y_pred);
    // }

    // double s2 = sum_residuals / (n - 2); // Variance résiduelle
    // double s_m = sqrt(s2 / (n * sum_x2 - sum_x * sum_x)); // Erreur standard pour m
    // double s_b = sqrt(s2 * (1.0 / n + (sum_x / n) * (sum_x / n) / (n * sum_x2 - sum_x * sum_x))); // Erreur standard pour b

    // // Calcul des t-statistiques
    // double t_m = *m / s_m;
    // double t_b = *b / s_b;

    // // Calcul des p-valeurs
    // double p_m = calculate_p_value(fabs(t_m), n - 2);
    // double p_b = calculate_p_value(fabs(t_b), n - 2);

    // // Affichage des résultats
    // printf("Coefficient m (pente): %.5f, t-statistic: %.5f, p-value: %.5f\n", *m, t_m, p_m);
    // printf("Coefficient b (ordonnée): %.5f, t-statistic: %.5f, p-value: %.5f\n", *b, t_b, p_b);

    // // Tests de significativité
    // if (p_m < 0.05)
    //     printf("Le coefficient m est significatif au niveau de 5%%.\n");
    // else
    //     printf("Le coefficient m n'est pas significatif au niveau de 5%%.\n");

    // if (p_b < 0.05)
    //     printf("Le coefficient b est significatif au niveau de 5%%.\n");
    // else
    //     printf("Le coefficient b n'est pas significatif au niveau de 5%%.\n");
