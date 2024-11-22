#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

// Function to calulate the linear regression
// y = mx + b
void Linear_Regression(double x*, double y*, int n, double *m, double *b){
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
// Function pour read the data from the file
int read_data(const char *filename, double *values, int max_size) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Erreur lors de l'ouverture du fichier");
        return -1;
    }
    int count = 0;
    while (fscanf(file, "%lf", &values[count]) == 1 && count < max_size) {
        count++;
    }
    fclose(file);
    return count;

int main(){
    // x are green gas emmisions
    // y are sea ice extent
    const int max_data_size = 2000;
    double x[max_data_size]; 
    double y[max_data_size];
    int n_x, n_y;

    // Read data from sea ice
    n_y = read_data("sea_ice.csv", y, max_data_size);
    if (n_y <= 0) {
        printf("Error: no data in sea_ice.csv\n");
        return 1;
    }

    // Read data from GHG
    n_x = read_data("GHG.csv", x, max_data_size);
    if (n_x <= 0) {
        printf("Error : no data in GHG.csv\n");
        return 1;

    // Check if the number of data is the same
    if (n_x != n_y) {
        printf("Error : files don't have the same number of data points (%d vs %d).\n", n_x, n_y);
        return 1;
    }

    // calulate the linear regression
    double m, b;
    linear_regression(x, y, n_x, &m, &b);

    // Print the result
    printf("Équation de la régression linéaire : y = %.2fx + %.2f\n", m, b);
    return 0;
}
