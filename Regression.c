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
    const int max_data_size = 1000;
    double x[max_data_size], y[max_data_size];
    int n_x, n_y;

    // Lire les données sur la banquise
    n_y = read_data("banquise.csv", y, max_data_size);
    if (n_y <= 0) {
        printf("Erreur : pas de données dans banquise.csv\n");
        return 1;
    }

    // Lire les données sur les émissions de GES
    n_x = read_data("GES.csv", x, max_data_size);
    if (n_x <= 0) {
        printf("Erreur : pas de données dans GES.csv\n");
        return 1;

    // Calculer la régression linéaire
    double m, b;
    linear_regression(x, y, n_x, &m, &b);

    // Afficher les résultats
    printf("Équation de la régression linéaire : y = %.2fx + %.2f\n", m, b);

}
