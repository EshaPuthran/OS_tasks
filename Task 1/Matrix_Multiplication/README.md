# Matrix Multiplication Using Threads and TensorFlow

This project implements matrix multiplication using Python threads and TensorFlow. It performs multiplication of two 100 x 100 matrices using a controlled thread pool and verifies the result using TensorFlow.

The working process is also demonstrated through a Matplotlib animation, where the resultant matrix is progressively filled with calculated values.

## Features

- Generates two 100 x 100 matrices using TensorFlow.
- Performs matrix multiplication using Python threads.
- Uses `ThreadPoolExecutor` with 32 worker threads.
- Calculates each output cell as an independent task.
- Measures the execution time of threaded multiplication.
- Verifies the result using TensorFlow's `tf.matmul()`.
- Compares the threaded result using NumPy's `np.allclose()`.
- Displays the matrix multiplication process using animation.
- Saves the animation as a GIF file.

## Technologies Used

- Python
- TensorFlow
- NumPy
- Matplotlib
- Pillow
- Concurrent Futures
- Visual Studio Code

## Project Structure

```text
Matrix-Multiplication/
│
├── matrix_mul.py
├── threaded_matrix_multiplication.gif
└── README.md
```
## Working Method

The project uses two input matrices and one resultant matrix:

```text
Matrix A: 100 x 100
Matrix B: 100 x 100
Matrix C: 100 x 100
```

