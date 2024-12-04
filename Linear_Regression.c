#include <stdio.h>
#include <math.h>

// Function to calulate the linear regression
// y = mx + b
// y = b0x0 + b1x1 + c  avec par exemple x0 = CH4 et x1 = CO2
// y is the sea ice extent
// x is the green gas emmisions

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