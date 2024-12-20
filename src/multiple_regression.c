//===================================================================================
// Description: This file contains the function to calculate the multiple regression
//===================================================================================

// Loading libraries
#include <stdio.h>
#include <math.h>

// Function to perform matrix multiplication
void matrix_multiply(double **A, double **B, double **C, int m, int n, int p) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < p; j++) {
            C[i][j] = 0;
            for (int k = 0; k < n; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

// Function to perform matrix transpose
void matrix_transpose(double **A, double **B, int m, int n) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            B[j][i] = A[i][j];
        }
    }
}

// Function to perform matrix inversion (using Gauss-Jordan elimination)
int matrix_invert(double **A, double **A_inv, int n) {
    double **augmented = (double **)malloc(n * sizeof(double *));
    for (int i = 0; i < n; i++) {
        augmented[i] = (double *)malloc(2 * n * sizeof(double));
        for (int j = 0; j < n; j++) {
            augmented[i][j] = A[i][j];
            augmented[i][j + n] = (i == j) ? 1.0 : 0.0;
        }
    }

    for (int i = 0; i < n; i++) {
        if (augmented[i][i] == 0) {
            free(augmented);
            return -1; // Matrix is singular
        }
        double pivot = augmented[i][i];
        for (int j = 0; j < 2 * n; j++) {
            augmented[i][j] /= pivot;
        }
        for (int k = 0; k < n; k++) {
            if (k != i) {
                double factor = augmented[k][i];
                for (int j = 0; j < 2 * n; j++) {
                    augmented[k][j] -= factor * augmented[i][j];
                }
            }
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            A_inv[i][j] = augmented[i][j + n];
        }
        free(augmented[i]);
    }
    free(augmented);
    return 0;
}

// Function to calculate a multiple regression model
void multiple_regression(double **X, double *y, int n, int p, double *coefficients) {
    double **X_transpose = (double **)malloc(p * sizeof(double *));
    double **X_transpose_X = (double **)malloc(p * sizeof(double *));
    double **X_transpose_X_inv = (double **)malloc(p * sizeof(double *));
    double **X_transpose_y = (double **)malloc(p * sizeof(double *));
    for (int i = 0; i < p; i++) {
        X_transpose[i] = (double *)malloc(n * sizeof(double));
        X_transpose_X[i] = (double *)malloc(p * sizeof(double));
        X_transpose_X_inv[i] = (double *)malloc(p * sizeof(double));
        X_transpose_y[i] = (double *)malloc(1 * sizeof(double));
    }

    // Calculate X^T
    matrix_transpose(X, X_transpose, n, p);

    // Calculate X^T * X
    matrix_multiply(X_transpose, X, X_transpose_X, p, n, p);

    // Calculate (X^T * X)^-1
    if (matrix_invert(X_transpose_X, X_transpose_X_inv, p) != 0) {
        printf("Matrix inversion failed. The matrix might be singular.\n");
        return;
    }

    // Calculate X^T * y
    for (int i = 0; i < p; i++) {
        X_transpose_y[i][0] = 0;
        for (int j = 0; j < n; j++) {
            X_transpose_y[i][0] += X_transpose[i][j] * y[j];
        }
    }

    // Calculate coefficients: (X^T * X)^-1 * X^T * y
    for (int i = 0; i < p; i++) {
        coefficients[i] = 0;
        for (int j = 0; j < p; j++) {
            coefficients[i] += X_transpose_X_inv[i][j] * X_transpose_y[j][0];
        }
    }

    for (int i = 0; i < p; i++) {
        free(X_transpose[i]);
        free(X_transpose_X[i]);
        free(X_transpose_X_inv[i]);
        free(X_transpose_y[i]);
    }
    free(X_transpose);
    free(X_transpose_X);
    free(X_transpose_X_inv);
    free(X_transpose_y);
}