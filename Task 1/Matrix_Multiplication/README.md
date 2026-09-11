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
Each cell of Matrix C is calculated by taking one row from Matrix A and one column from Matrix B.

The calculation for each cell follows the general process:
```text
Multiply corresponding elements of a row of A and a column of B,
then add the multiplication results.
```
The calculate_cell() function performs this operation for one output cell.

The program uses:
```text
ThreadPoolExecutor(max_workers=32)
```
The 10,000 output-cell calculations are distributed among the worker threads.

After the threaded multiplication is completed, TensorFlow calculates the result independently using:
```text
tf.matmul()
```
Both results are compared to verify correctness.

## Animation

The animation is created using Matplotlib's FuncAnimation.

Matrix A is displayed in purple.
Matrix B is displayed in teal.
Matrix C is displayed in golden colour.
Matrix C initially appears blank.
The calculated cells are progressively filled.
The current row of Matrix A and column of Matrix B are highlighted.
The animation is displayed live and saved as a GIF.

The saved animation file is:
```text
threaded_matrix_multiplication.gif
```
## Requirements

Install the required Python libraries using:
```text
pip install numpy tensorflow matplotlib pillow
```
> **Note:**TensorFlow may require a compatible Python version. This project was developed using Python 3.11.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/EshaPuthran/OS_tasks
```

### 2. Open the project folder

```bash
cd OS_tasks
```

### 3. Create a virtual environment

```bash
python -m venv matrix_env
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.\matrix_env\Scripts\activate
```

### 5. Install the required dependencies

```bash
pip install numpy tensorflow matplotlib pillow
```

### 6. Run the program

```bash
python matrix_mul.py
```

## Expected Output

The program displays:

```text
Starting threaded matrix multiplication...

Threaded multiplication completed!

Verifying result using TensorFlow...

RESULT VERIFIED SUCCESSFULLY!
```

It also opens a graphical animation showing the progressive filling of Matrix C.

After the animation is closed, the GIF is saved as:

```text
threaded_matrix_multiplication.gif
```

## Result Verification

The threaded matrix multiplication result is independently verified using TensorFlow's matrix multiplication function:

```python
tensorflow_C = tf.matmul(
    tf.constant(A),
    tf.constant(B)
).numpy()
```

The result is compared using NumPy's `allclose()` function:

```python
np.allclose(C, tensorflow_C, atol=1e-3)
```

If the results match within the specified tolerance, the program displays:

```text
RESULT VERIFIED SUCCESSFULLY!
```

## Learning Outcomes

Through this project, the following concepts are demonstrated:

- Matrix multiplication
- Python multithreading
- Thread pool execution
- Task distribution
- TensorFlow matrix operations
- Result verification
- Matplotlib animation
- Numerical computation using NumPy

## Future Enhancements

- Compare single-threaded and multithreaded execution time.
- Allow the user to enter the matrix size.
- Test larger matrices.
- Compare the performance of Python, NumPy, and TensorFlow.
- Add multiprocessing support.
- Add execution-time graphs.
