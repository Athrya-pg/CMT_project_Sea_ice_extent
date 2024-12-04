
#include <stdio.h>
#include <math.h>
// Function to calculate the mean
double mean(double *values, int n) {
    double sum = 0.0;
    for (int i = 0; i < n; i++) {
        sum += values[i];
    }
    return sum / n;
}

//Function to calculate R2, the coefficient of determination
double calculate_r2(double* y_true, double* y_pred, int n){
    double ss_res = 0.0;
    double ss_tot = 0.0;
    int y_mean = mean(y_true, n);

    for (int i = 0; i < n; i++) {
        ss_res += pow(y_true[i] - y_pred[i], 2);
        ss_tot += pow(y_true[i] - y_mean, 2);
    }
    return 1 - (ss_res / ss_tot);
}
