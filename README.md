Matrix Operations Framework 


Overview

This project is a C++ console-based framework that allows users to perform three essential matrix operations: Addition, Multiplication, and Inversion using dynamic 2D arrays of floats. It follows an object-oriented design where each operation (Add, Multiply, Invert) extends a common abstract interface, demonstrating key principles like abstraction, inheritance, and polymorphism in action.


Key Features

- Modular design using a base class MatrixOp and derived operation classes
- Matrix Addition which Adds two matrices of the same size
- Matrix Multiplication which Multiplies compatible matrices
- Matrix Inversion which Supports inversion of 2×2 matrices only
- Dynamic memory allocation with safe cleanup
- Interactive menu that based UI for smooth user experience
- Input validation and error messaging

 
Technologies Used

Language: C++
Concepts Applied:
- Abstract classes and virtual functions
- Dynamic memory management
- Pointer arithmetic
- Clean user interface in console




 How It Works



The user is prompted to input the sizes and values of two matrices (A and B).
A menu is displayed where the user can choose one of the following:
Add matrices A + B (if same dimensions)
Multiply matrices A * B (if valid dimensions)
Invert matrix A (only if 2×2)
The result is computed using the appropriate subclass (AddMatrixOp, MultiplyMatrixOp, InvertMatrixOp) and displayed on screen.
Memory used is safely deallocated after each operation and at program termination.








  Author





Names: Yves MUGISHA
Email: mugishayves00@gmail.com
GitHub: @yvesmugisha




