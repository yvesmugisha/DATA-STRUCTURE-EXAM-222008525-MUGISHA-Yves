#include <iostream>         // For input and output
#include <iomanip>          // For formatting matrix output
#include <limits>           // For input validation
using namespace std;        // Use standard namespace to simplify syntax

// Abstract base class for matrix operations
class MatrixOp {
public:
    // Pure virtual function to perform matrix operation
    virtual float** execute(float** A, float** B, int r1, int c1, int r2, int c2) = 0;
    virtual ~MatrixOp() {} // Virtual destructor
};

// Matrix addition operation class
class AddMatrixOp : public MatrixOp {
public:
    // Override the execute function for addition
    float** execute(float** A, float** B, int r1, int c1, int r2, int c2) override {
        if (r1 != r2 || c1 != c2) { // Check if dimensions match for addition
            cout << "Error: Matrices must be the same size to add.\n";
            return nullptr;
        }
        float** result = new float*[r1]; // Allocate memory for result matrix
        for (int i = 0; i < r1; ++i) {
            result[i] = new float[c1];
            for (int j = 0; j < c1; ++j)
                result[i][j] = A[i][j] + B[i][j]; // Add elements of A and B
        }
        return result;
    }
};

// Matrix multiplication operation class
class MultiplyMatrixOp : public MatrixOp {
public:
    // Override the execute function for multiplication
    float** execute(float** A, float** B, int r1, int c1, int r2, int c2) override {
        if (c1 != r2) { // Check multiplication condition
            cout << "Error: Columns of A must equal rows of B for multiplication.\n";
            return nullptr;
        }
        float** result = new float*[r1]; // Allocate memory for result matrix
        for (int i = 0; i < r1; ++i) {
            result[i] = new float[c2];
            for (int j = 0; j < c2; ++j) {
                result[i][j] = 0;
                for (int k = 0; k < c1; ++k)
                    result[i][j] += A[i][k] * B[k][j]; // Multiply and accumulate
            }
        }
        return result;
    }
};

// Matrix inversion operation (only for 2x2 matrices)
class InvertMatrixOp : public MatrixOp {
public:
    // Override execute function for matrix inversion
    float** execute(float** A, float**, int r1, int c1, int, int) override {
        if (r1 != 2 || c1 != 2) { // Check if matrix is 2x2
            cout << "Error: Inversion supported only for 2x2 matrices.\n";
            return nullptr;
        }
        float det = A[0][0] * A[1][1] - A[0][1] * A[1][0]; // Calculate determinant
        if (det == 0) { // Check if matrix is invertible
            cout << "Error: Matrix is singular and cannot be inverted.\n";
            return nullptr;
        }
        float** inv = new float*[2]; // Allocate memory for inverse matrix
        inv[0] = new float[2];
        inv[1] = new float[2];

        // Calculate inverse of 2x2 matrix
        inv[0][0] =  A[1][1] / det;
        inv[0][1] = -A[0][1] / det;
        inv[1][0] = -A[1][0] / det;
        inv[1][1] =  A[0][0] / det;

        return inv;
    }
};

// Function to create and fill a matrix with user input
float** inputMatrix(int rows, int cols) {
    float** mat = new float*[rows]; // Allocate row pointers
    for (int i = 0; i < rows; ++i) {
        mat[i] = new float[cols]; // Allocate each row
        for (int j = 0; j < cols; ++j) {
            cout << "A[" << i << "][" << j << "]: ";
            cin >> mat[i][j]; // Read matrix element
        }
    }
    return mat;
}

// Function to display a matrix
void displayMatrix(float** mat, int rows, int cols) {
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j)
            cout << setw(7) << fixed << setprecision(2) << mat[i][j]; // Print each element formatted
        cout << endl;
    }
}

// Function to free allocated memory for a matrix
void freeMatrix(float** mat, int rows) {
    for (int i = 0; i < rows; ++i)
        delete[] mat[i]; // Delete each row
    delete[] mat; // Delete row pointers
}

// Main function - entry point
int main() {
    cout << "=========== MATRIX OPERATIONS FRAMEWORK ===========\n\n"; // Display title

    int r1, c1, r2, c2; // Matrix dimensions

    // Input dimensions for matrix A
    cout << "Enter rows and columns of Matrix A (e.g. 2 2): ";
    cin >> r1 >> c1;
    float** A = inputMatrix(r1, c1); // Get matrix A from user

    // Input dimensions for matrix B
    cout << "\nEnter rows and columns of Matrix B (e.g. 2 2): ";
    cin >> r2 >> c2;
    float** B = inputMatrix(r2, c2); // Get matrix B from user

    // Menu loop for operations
    while (true) {
        cout << "\n------ Matrix Operation Menu ------\n";
        cout << "1. Add Matrices\n";
        cout << "2. Multiply Matrices\n";
        cout << "3. Invert Matrix A (2x2 only)\n";
        cout << "4. Exit\n";
        cout << "Choose an option (1-4): ";

        int choice;
        cin >> choice; // Read user choice

        MatrixOp* op = nullptr; // Pointer to matrix operation class
        float** result = nullptr; // Result matrix

        switch (choice) {
            case 1:
                op = new AddMatrixOp(); // Addition operation
                result = op->execute(A, B, r1, c1, r2, c2);
                if (result) {
                    cout << "\n-- Result of Matrix A + B --\n";
                    displayMatrix(result, r1, c1);
                    freeMatrix(result, r1);
                }
                delete op;
                break;
            case 2:
                op = new MultiplyMatrixOp(); // Multiplication operation
                result = op->execute(A, B, r1, c1, r2, c2);
                if (result) {
                    cout << "\n-- Result of Matrix A * B --\n";
                    displayMatrix(result, r1, c2);
                    freeMatrix(result, r1);
                }
                delete op;
                break;
            case 3:
                op = new InvertMatrixOp(); // Inversion operation
                result = op->execute(A, nullptr, r1, c1, 0, 0);
                if (result) {
                    cout << "\n-- Inverse of Matrix A --\n";
                    displayMatrix(result, 2, 2);
                    freeMatrix(result, 2);
                }
                delete op;
                break;
            case 4:
                cout << "Exiting program.\n";
                freeMatrix(A, r1);
                freeMatrix(B, r2);
                return 0; // Exit program
            default:
                cout << "Invalid option. Please select from 1 to 4.\n";
        }
    }
}