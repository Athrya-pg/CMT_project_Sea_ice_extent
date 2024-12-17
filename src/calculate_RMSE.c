// =====================================================================
// Description : Function to calculate the root mean square error, RMSE
//======================================================================

#include <stdio.h>
#include <math.h>

// Function to calculate the root mean square error, RMSE
double calculate_rmse(double *y_obs, double *y_pred, int n){
    double RMSE = 0.0;
    for(int i = 0; i<n; i++){
        RMSE += pow(y_obs[i] - y_pred[i], 2);
    }
    return sqrt(RMSE / n);
}