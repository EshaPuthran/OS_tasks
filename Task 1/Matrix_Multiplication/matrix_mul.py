import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.animation import FuncAnimation
from matplotlib.colors import LinearSegmentedColormap
from concurrent.futures import ThreadPoolExecutor
import time


# MATRIX SIZE

SIZE = 100

ROWS_A = 100
COLS_A = 100
ROWS_B = 100
COLS_B = 100

assert COLS_A == ROWS_B

# GENERATE MATRICES USING TENSORFLOW

A = tf.random.uniform(
    (ROWS_A, COLS_A),
    minval=1,
    maxval=10,
    dtype=tf.float32
).numpy()

B = tf.random.uniform(
    (ROWS_B, COLS_B),
    minval=1,
    maxval=10,
    dtype=tf.float32
).numpy()


# THREADED MATRIX MULTIPLICATION

C = np.zeros((SIZE, SIZE), dtype=np.float32)


def calculate_cell(index):
    row = index // SIZE
    col = index % SIZE

    total = 0.0

    for k in range(SIZE):
        total += A[row][k] * B[k][col]

    return row, col, total


def threaded_multiplication():

    print("Starting threaded matrix multiplication...")
    print("Matrix A:", A.shape)
    print("Matrix B:", B.shape)

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=32) as executor:

        results = executor.map(
            calculate_cell,
            range(SIZE * SIZE)
        )

        for row, col, value in results:
            C[row][col] = value

    end_time = time.time()

    print("\nThreaded multiplication completed!")
    print("Total output cells calculated:", SIZE * SIZE)
    print(
        "Time taken:",
        round(end_time - start_time, 3),
        "seconds"
    )


# Run multiplication
threaded_multiplication()


# VERIFY RESULT USING TENSORFLOW

print("\nVerifying result using TensorFlow...")

tensorflow_C = tf.matmul(
    tf.constant(A),
    tf.constant(B)
).numpy()

if np.allclose(C, tensorflow_C, atol=1e-3):
    print("RESULT VERIFIED SUCCESSFULLY!")
else:
    print("RESULT VERIFICATION FAILED!")


# CUSTOM COLOR MAPS

# Matrix A - Purple
purple_colors = [
    "#F3E5F5",
    "#CE93D8",
    "#AB47BC",
    "#7B1FA2",
    "#4A148C"
]

purple_map = LinearSegmentedColormap.from_list(
    "PurpleMatrix",
    purple_colors
)

# Matrix B - Teal
teal_colors = [
    "#E0F7FA",
    "#80DEEA",
    "#26C6DA",
    "#00838F",
    "#004D40"
]

teal_map = LinearSegmentedColormap.from_list(
    "TealMatrix",
    teal_colors
)


# Matrix C - Golden
gold_colors = [
    "#FFF8E1",
    "#FFE082",
    "#FFCA28",
    "#FF8F00",
    "#E65100"
]

gold_map = LinearSegmentedColormap.from_list(
    "GoldenMatrix",
    gold_colors
)

# Empty cells remain white
gold_map.set_bad(color="white", alpha=0)


# CREATE FIGURE

fig = plt.figure(figsize=(18, 8))

axA = fig.add_axes([0.03, 0.18, 0.27, 0.65])
axB = fig.add_axes([0.365, 0.18, 0.27, 0.65])
axC = fig.add_axes([0.70, 0.18, 0.27, 0.65])

# DISPLAY MATRIX A

imA = axA.imshow(
    A,
    cmap=purple_map,
    interpolation="nearest",
    aspect="equal"
)

# DISPLAY MATRIX B

imB = axB.imshow(
    B,
    cmap=teal_map,
    interpolation="nearest",
    aspect="equal"
)

# DISPLAY MATRIX C - INITIALLY BLANK

display_C = np.full(
    (SIZE, SIZE),
    np.nan,
    dtype=np.float32
)

imC = axC.imshow(
    display_C,
    cmap=gold_map,
    interpolation="nearest",
    aspect="equal",
    vmin=0,
    vmax=np.max(C)
)


# BLACK BORDER AROUND MATRIX C

c_border = patches.Rectangle(
    (-0.5, -0.5),
    SIZE,
    SIZE,
    linewidth=3,
    edgecolor="black",
    facecolor="none",
    zorder=8
)

axC.add_patch(c_border)


# REMOVE AXES, TICKS AND NUMBERS

for ax in [axA, axB, axC]:

    ax.set_xticks([])
    ax.set_yticks([])

    ax.set_xlim(-0.5, SIZE - 0.5)
    ax.set_ylim(SIZE - 0.5, -0.5)

    ax.set_frame_on(False)


# TITLES

axA.set_title(
    "MATRIX A",
    fontsize=20,
    fontweight="bold",
    pad=15
)

axB.set_title(
    "MATRIX B",
    fontsize=20,
    fontweight="bold",
    pad=15
)

axC.set_title(
    "MATRIX C",
    fontsize=20,
    fontweight="bold",
    pad=15
)


# MULTIPLICATION SYMBOL

fig.text(
    0.335,
    0.50,
    "×",
    fontsize=38,
    fontweight="bold",
    ha="center",
    va="center"
)

fig.text(
    0.675,
    0.50,
    "=",
    fontsize=38,
    fontweight="bold",
    ha="center",
    va="center"
)


# PINK HIGHLIGHT FOR CURRENT ROW IN MATRIX A

row_highlight = patches.Rectangle(
    (-0.5, -0.5),
    SIZE,
    1,
    linewidth=3,
    edgecolor="#FF1493",
    facecolor="none",
    zorder=10
)

axA.add_patch(row_highlight)


# RED HIGHLIGHT FOR CURRENT COLUMN IN MATRIX B

column_highlight = patches.Rectangle(
    (-0.5, -0.5),
    1,
    SIZE,
    linewidth=4,
    edgecolor="#FF1744",
    facecolor="none",
    zorder=10
)

axB.add_patch(column_highlight)

# STATUS TEXT

status = fig.text(
    0.5,
    0.10,
    "",
    ha="center",
    va="center",
    fontsize=16,
    fontweight="bold"
)

description = fig.text(
    0.5,
    0.045,
    "Pink = Current Row of A     Red = Current Column of B     Golden Cells = Completed Calculations",
    ha="center",
    va="center",
    fontsize=12
)

# Number of cells filled during each frame.
CELLS_PER_FRAME = 100

TOTAL_FRAMES = (
    SIZE * SIZE + CELLS_PER_FRAME - 1
) // CELLS_PER_FRAME


def update(frame):

    start_index = frame * CELLS_PER_FRAME

    end_index = min(
        start_index + CELLS_PER_FRAME,
        SIZE * SIZE
    )

    # Fill cells in order
    for index in range(start_index, end_index):

        row = index // SIZE
        col = index % SIZE

        display_C[row, col] = C[row, col]

    # Get the latest processed cell
    latest_index = end_index - 1

    row = latest_index // SIZE
    col = latest_index % SIZE

    # Move current row highlight in Matrix A
    row_highlight.set_xy(
        (-0.5, row - 0.5)
    )

    # Move current column highlight in Matrix B
    column_highlight.set_xy(
        (col - 0.5, -0.5)
    )

    # Refresh Matrix C
    imC.set_array(display_C)

    # Update status
    status.set_text(
        f"Filling Matrix C: Cell "
        f"({row + 1}, {col + 1}) "
        f"of {SIZE} × {SIZE}"
    )

    return (
        imC,
        row_highlight,
        column_highlight
    )

# CREATE ANIMATION

animation = FuncAnimation(
    fig,
    update,
    frames=TOTAL_FRAMES,
    interval=60,
    repeat=False,
    blit=False,
    cache_frame_data=False
)


# MAIN TITLE
fig.suptitle(
    "THREADED MATRIX MULTIPLICATION",
    fontsize=24,
    fontweight="bold",
    y=0.94
)

# DISPLAY LIVE ANIMATION
print("\nDisplaying live animation...")
print("Matrix C will start blank and fill progressively.")
print("Close the animation window after watching it.")

plt.show()

display_C[:] = np.nan

row_highlight.set_xy(
    (-0.5, -0.5)
)

column_highlight.set_xy(
    (-0.5, -0.5)
)

imC.set_array(display_C)

# SAVE GIF

print("\nSaving animation as GIF...")

animation.save(
    "threaded_matrix_multiplication.gif",
    writer="pillow",
    fps=5
)

print("GIF saved successfully!")

# FINAL OUTPUT
print("\nMatrix C is completely filled.")

print("Sample C matrix (first 5 × 5):")
print(C[:5, :5])