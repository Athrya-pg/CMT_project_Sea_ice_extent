#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

// Function to calulate the linear regression
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
// Fonction pour lire les données depuis un fichier
int read_data(const char *filename, double *x, double *y, int max_size) {
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        perror("Erreur lors de l'ouverture du fichier");
        return -1;
    }
    int i = 0;
    while(fscanf(file, "%lf %lf", &x[i], &y[i]) != EOF){
        i++;
    }
    fclose(file);
    return i;
}


int main(){
    // x are CO2 emmisions
    // y are sea ice extent

}
