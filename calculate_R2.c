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
double calculate_R2(double* y_true, double* y_pred, int n){
    double ssr = 0.0;
    double sse = 0.0;
    double y_mean = mean(y_true, n);

    for (int i = 0; i < n; i++) {
        ssr += pow(y_true[i] - y_pred[i], 2);
        sse += pow(y_true[i] - y_mean, 2);
    }
    return 1 - (ssr / sse);
}
