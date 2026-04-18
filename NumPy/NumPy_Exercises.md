# 🔢 NumPy Programming Exercises — Beginner to Expert

A comprehensive collection of NumPy exercises covering array creation, manipulation, linear algebra, broadcasting, and high-performance computing. Every exercise includes a problem description, hints, and a collapsible solution.

---

## 📋 Table of Contents

- [Level Guide](#-level-guide)
- [🟢 Beginner — Array Basics](#-beginner--array-basics)
- [🟡 Elementary — Indexing, Slicing & Reshaping](#-elementary--indexing-slicing--reshaping)
- [🟠 Intermediate — Math, Stats & Broadcasting](#-intermediate--math-stats--broadcasting)
- [🔵 Upper Intermediate — Linear Algebra & Matrix Ops](#-upper-intermediate--linear-algebra--matrix-ops)
- [🔴 Advanced — Random, Structured Arrays & FFT](#-advanced--random-structured-arrays--fft)
- [⚫ Expert — Vectorisation, Memory & Custom ufuncs](#-expert--vectorisation-memory--custom-ufuncs)
- [📝 Quick Reference Cheat Sheet](#-quick-reference-cheat-sheet)

---

## 📊 Level Guide

| Level | Label | Description |
|-------|-------|-------------|
| 🟢 **1** | Beginner | Array creation, data types, basic attributes |
| 🟡 **2** | Elementary | Indexing, slicing, reshaping, stacking |
| 🟠 **3** | Intermediate | Universal functions, statistics, broadcasting |
| 🔵 **4** | Upper Intermediate | Linear algebra, matrix operations, decompositions |
| 🔴 **5** | Advanced | Random number generation, FFT, structured arrays |
| ⚫ **6** | Expert | Vectorisation, memory views, custom ufuncs, performance |

---

## 🟢 Beginner — Array Basics

---

### B1 — Create Arrays in Multiple Ways

**Question:**
Create NumPy arrays using five different methods:
1. From a Python list
2. Array of zeros (3×4)
3. Array of ones (2×3)
4. Identity matrix (4×4)
5. Linearly spaced values from 0 to 1 (10 points)

**Hints:**
- Use `np.array()`, `np.zeros()`, `np.ones()`, `np.eye()`, `np.linspace()`

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

# 1. From a Python list
arr = np.array([1, 2, 3, 4, 5])
print("From list:", arr)

# 2. Zeros
zeros = np.zeros((3, 4))
print("\nZeros (3×4):\n", zeros)

# 3. Ones
ones = np.ones((2, 3))
print("\nOnes (2×3):\n", ones)

# 4. Identity matrix
eye = np.eye(4)
print("\nIdentity (4×4):\n", eye)

# 5. Linearly spaced
lin = np.linspace(0, 1, 10)
print("\nLinspace:", lin)
```

**Output:**
```
From list: [1 2 3 4 5]
Zeros (3×4):
 [[0. 0. 0. 0.]
  [0. 0. 0. 0.]
  [0. 0. 0. 0.]]
```
</details>

---

### B2 — Array Attributes

**Question:**
Create a 3D array of shape (2, 4, 3) filled with random integers between 1 and 100. Print its shape, number of dimensions, total element count, data type, and memory size in bytes.

**Hints:**
- Use `.shape`, `.ndim`, `.size`, `.dtype`, `.nbytes`

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

arr = np.random.randint(1, 101, size=(2, 4, 3))

print("Array:\n", arr)
print("\nShape:      ", arr.shape)
print("Dimensions: ", arr.ndim)
print("Total items:", arr.size)
print("Data type:  ", arr.dtype)
print("Memory (bytes):", arr.nbytes)
print("Item size (bytes):", arr.itemsize)
```
</details>

---

### B3 — Data Types and Casting

**Question:**
Demonstrate NumPy data types. Create arrays of different dtypes and convert between them. Show how dtype affects precision and memory.

**Hints:**
- Use `dtype=` parameter or `.astype()`

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

# Different dtypes
int8_arr   = np.array([1, 2, 3], dtype=np.int8)
int32_arr  = np.array([1, 2, 3], dtype=np.int32)
float32    = np.array([1.5, 2.7, 3.9], dtype=np.float32)
float64    = np.array([1.5, 2.7, 3.9], dtype=np.float64)
bool_arr   = np.array([1, 0, 1, 0], dtype=bool)
complex_arr= np.array([1+2j, 3+4j])

for arr, name in [(int8_arr,"int8"), (int32_arr,"int32"),
                   (float32,"float32"), (float64,"float64"),
                   (bool_arr,"bool"), (complex_arr,"complex128")]:
    print(f"{name:12s} | dtype: {arr.dtype:12s} | bytes: {arr.nbytes}")

# Casting
print("\nCasting float64 to int32:")
f = np.array([1.9, 2.7, 3.1])
print("Before:", f, f.dtype)
print("After: ", f.astype(np.int32), f.astype(np.int32).dtype)  # truncates!

# Overflow warning
print("\nOverflow example:")
x = np.array([200], dtype=np.int8)   # int8 max is 127
print("200 as int8:", x)             # wraps around
```
</details>

---

### B4 — arange and linspace

**Question:**
1. Create an array of even numbers from 0 to 20 using `arange`
2. Create 7 equally spaced angles between 0 and 2π using `linspace`
3. Create a descending array from 10 to 1 using `arange`
4. Create a log-spaced array from 10¹ to 10⁵ using `logspace`

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

# 1. Even numbers 0–20
evens = np.arange(0, 22, 2)
print("Even numbers:", evens)

# 2. 7 angles between 0 and 2π
angles = np.linspace(0, 2 * np.pi, 7)
print("\n7 angles (radians):", np.round(angles, 4))
print("In degrees:         ", np.round(np.degrees(angles), 1))

# 3. Descending 10 to 1
desc = np.arange(10, 0, -1)
print("\nDescending:", desc)

# 4. Log-spaced
log_space = np.logspace(1, 5, num=5)
print("\nLog-spaced:", log_space)
```
</details>

---

### B5 — Basic Arithmetic Operations

**Question:**
Create two arrays and demonstrate element-wise arithmetic: addition, subtraction, multiplication, division, power, and modulo. Also show scalar operations.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

a = np.array([10, 20, 30, 40, 50])
b = np.array([3,  4,  5,  6,  7])

print("a      :", a)
print("b      :", b)
print("a + b  :", a + b)
print("a - b  :", a - b)
print("a * b  :", a * b)
print("a / b  :", a / b)
print("a // b :", a // b)    # floor division
print("a % b  :", a % b)     # modulo
print("a ** 2 :", a ** 2)    # power

# Scalar operations (broadcast)
print("\nScalar operations:")
print("a + 100:", a + 100)
print("a * 0.5:", a * 0.5)
print("a > 25 :", a > 25)    # boolean mask
```
</details>

---

### B6 — Array Comparison and Boolean Operations

**Question:**
Demonstrate comparison operators, logical operations, and use boolean arrays as masks to filter values.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

arr = np.array([5, 12, 3, 18, 7, 25, 9, 14])

# Comparisons return boolean arrays
print("arr > 10:", arr > 10)
print("arr == 7:", arr == 7)

# Logical operations
mask = (arr > 5) & (arr < 20)
print("\nBetween 5 and 20:", mask)
print("Values in range:", arr[mask])

# np.where — conditional selection
result = np.where(arr > 10, "big", "small")
print("\nnp.where:", result)

# Count and check
print("\nCount > 10:", np.sum(arr > 10))
print("Any > 20? :", np.any(arr > 20))
print("All > 0?  :", np.all(arr > 0))
```
</details>

---

### B7 — Copy vs View

**Question:**
Demonstrate the critical difference between a NumPy view (shallow copy) and a true copy, and show when each is created.

**Hints:**
- Slices return views; `np.copy()` or `.copy()` return independent arrays

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

original = np.array([1, 2, 3, 4, 5])

# View — shares memory
view = original[1:4]
view[0] = 99
print("After modifying view:")
print("original:", original)   # CHANGED!
print("view:    ", view)

# Reset
original = np.array([1, 2, 3, 4, 5])

# True copy — independent
copy = original[1:4].copy()
copy[0] = 99
print("\nAfter modifying copy:")
print("original:", original)   # unchanged
print("copy:    ", copy)

# Check with base
slice_arr = original[::2]
print("\nSlice is a view?", slice_arr.base is original)
print("Copy is a view? ", copy.base is None)
```
</details>

---

## 🟡 Elementary — Indexing, Slicing & Reshaping

---

### E1 — 2D Array Indexing

**Question:**
Create a 5×5 matrix of integers from 1–25. Demonstrate:
1. Single element access
2. Row and column slicing
3. Submatrix extraction
4. Diagonal extraction

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

matrix = np.arange(1, 26).reshape(5, 5)
print("Matrix:\n", matrix)

# Single element (row 2, col 3)
print("\nElement [2,3]:", matrix[2, 3])

# Entire row 1
print("Row 1:", matrix[1, :])

# Entire column 2
print("Column 2:", matrix[:, 2])

# Submatrix rows 1-3, cols 2-4
print("Submatrix [1:3, 2:4]:\n", matrix[1:3, 2:4])

# Last 2 rows
print("Last 2 rows:\n", matrix[-2:, :])

# Every other column
print("Every other col:\n", matrix[:, ::2])

# Main diagonal
print("Main diagonal:", np.diag(matrix))
```
</details>

---

### E2 — Fancy Indexing

**Question:**
Use fancy indexing (integer array indexing) to select non-contiguous rows, columns, and specific elements from a 2D array.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

arr = np.arange(1, 26).reshape(5, 5)
print("Array:\n", arr)

# Select specific rows
print("\nRows [0, 2, 4]:\n", arr[[0, 2, 4]])

# Select specific columns
print("Columns [1, 3]:\n", arr[:, [1, 3]])

# Select specific (row, col) pairs
rows = [0, 1, 2, 3]
cols = [0, 2, 1, 3]
print("Diagonal-like selection:", arr[rows, cols])

# Reverse row order
print("Reversed rows:\n", arr[::-1])

# Sort by second column
sort_idx = arr[:, 1].argsort()
print("Sorted by col 1:\n", arr[sort_idx])
```
</details>

---

### E3 — Reshaping, Ravel and Transpose

**Question:**
Demonstrate reshaping arrays, flattening, and transposing. Show the relationship between reshape, ravel, and flatten.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

arr = np.arange(1, 25)
print("Original (24 elements):", arr)

# Reshape to 2D
mat_2d = arr.reshape(4, 6)
print("\nReshaped (4×6):\n", mat_2d)

# Reshape to 3D
mat_3d = arr.reshape(2, 3, 4)
print("\nReshaped (2×3×4):\n", mat_3d)

# Ravel — returns view when possible
flat_view = mat_2d.ravel()
print("\nRavel (may be view):", flat_view)

# Flatten — always returns copy
flat_copy = mat_2d.flatten()
print("Flatten (always copy):", flat_copy)

# Transpose
print("\nTranspose (4×6 → 6×4):\n", mat_2d.T)
print("Transpose shape:", mat_2d.T.shape)

# -1 in reshape means "infer this dimension"
auto = np.arange(12).reshape(3, -1)  # 3×4
print("\nReshape with -1:\n", auto)
```
</details>

---

### E4 — Stacking and Splitting Arrays

**Question:**
Demonstrate horizontal and vertical stacking, and splitting arrays both evenly and at specific positions.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Stacking
print("vstack (vertical):\n",  np.vstack([a, b]))
print("\nhstack (horizontal):\n", np.hstack([a, b]))
print("\ndstack (depth):\n",    np.dstack([a, b]))
print("\nconcatenate axis=0:\n",np.concatenate([a, b], axis=0))

# 1D stacking
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print("\nstack (creates new axis):\n", np.stack([x, y]))       # shape (2,3)
print("column_stack:\n", np.column_stack([x, y]))              # shape (3,2)

# Splitting
arr = np.arange(12).reshape(3, 4)
print("\nOriginal:\n", arr)
print("hsplit into 2:\n", np.hsplit(arr, 2))
print("vsplit into 3:\n", np.vsplit(arr, 3))

# Split at specific positions
print("hsplit at [1,3]:", np.hsplit(arr, [1, 3]))
```
</details>

---

### E5 — Boolean Masking and np.where

**Question:**
Given a 2D array of sensor readings, use boolean masking to:
1. Find all readings above a threshold
2. Replace negative values with 0
3. Categorise values into bands using `np.where` and `np.select`

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

np.random.seed(42)
readings = np.random.uniform(-10, 100, size=(5, 6)).round(1)
print("Sensor readings:\n", readings)

# 1. Find values above 70
threshold = 70
high = readings[readings > threshold]
print(f"\nReadings > {threshold}: {high}")

# 2. Replace negatives with 0
clean = readings.copy()
clean[clean < 0] = 0
print("\nNegatives replaced with 0:\n", clean)

# 3. np.where (binary condition)
binary = np.where(readings > 50, "HIGH", "LOW")
print("\nBinary band:\n", binary)

# 4. np.select (multiple conditions)
conditions = [readings < 0, readings < 30, readings < 70, readings >= 70]
choices    = ["NEG", "LOW", "MED", "HIGH"]
bands = np.select(conditions, choices)
print("\nMulti-band classification:\n", bands)
```
</details>

---

### E6 — Array Sorting

**Question:**
Demonstrate sorting arrays along different axes, getting sort indices, and using `argsort` to sort one array by values of another.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

arr = np.array([[3, 1, 4], [1, 5, 9], [2, 6, 5]])
print("Original:\n", arr)

# Sort each row
print("\nSort along axis=1 (rows):\n", np.sort(arr, axis=1))

# Sort each column
print("Sort along axis=0 (columns):\n", np.sort(arr, axis=0))

# argsort — returns indices
flat = np.array([30, 10, 50, 20, 40])
idx = np.argsort(flat)
print("\nFlat array:", flat)
print("Argsort (indices):", idx)
print("Sorted:          ", flat[idx])

# Sort one array by another array's values
names   = np.array(["Charlie", "Alice", "Diana", "Bob"])
scores  = np.array([88, 95, 72, 83])
order   = np.argsort(scores)[::-1]   # descending
print("\nRanked names:", names[order])
print("Ranked scores:", scores[order])

# Partial sort with partition
print("\nTop-2 values (unordered):", np.partition(scores, -2)[-2:])
```
</details>

---

## 🟠 Intermediate — Math, Stats & Broadcasting

---

### I1 — Universal Functions (ufuncs)

**Question:**
Apply NumPy universal functions for trigonometry, exponentials, and logarithms. Compare performance of ufuncs vs Python math on large arrays.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np
import time

angles = np.linspace(0, 2 * np.pi, 6)
print("Angles (rad):", np.round(angles, 4))
print("sin:", np.round(np.sin(angles), 4))
print("cos:", np.round(np.cos(angles), 4))
print("tan:", np.round(np.tan(angles), 4))

# Exponential and log
x = np.array([0, 1, 2, 3, 4])
print("\nexp(x):", np.exp(x))
print("log(e^x):", np.log(np.exp(x)))
print("log2(x+1):", np.round(np.log2(x + 1), 4))
print("log10(10^x):", np.log10(10.0 ** x))

# Hyperbolic
print("\nsinh, cosh, tanh:", np.round(np.sinh(x[:3]), 3), np.round(np.cosh(x[:3]), 3))

# Performance comparison
big = np.random.rand(1_000_000)

t0 = time.time()
result_np = np.sqrt(big)
t_np = time.time() - t0

import math
t0 = time.time()
result_py = [math.sqrt(v) for v in big]
t_py = time.time() - t0

print(f"\nNumPy sqrt (1M): {t_np:.4f}s")
print(f"Python sqrt (1M): {t_py:.4f}s")
print(f"Speedup: {t_py/t_np:.1f}×")
```
</details>

---

### I2 — Statistical Functions

**Question:**
Compute comprehensive statistics on a dataset: mean, median, std, variance, percentiles, IQR, skewness-like metrics, and cumulative functions.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

np.random.seed(42)
data = np.random.normal(loc=50, scale=15, size=1000)

print("=== Descriptive Statistics ===")
print(f"Count:     {len(data)}")
print(f"Mean:      {np.mean(data):.4f}")
print(f"Median:    {np.median(data):.4f}")
print(f"Std Dev:   {np.std(data):.4f}")
print(f"Variance:  {np.var(data):.4f}")
print(f"Min:       {np.min(data):.4f}")
print(f"Max:       {np.max(data):.4f}")
print(f"Range:     {np.ptp(data):.4f}")

# Percentiles
p = [10, 25, 50, 75, 90, 95, 99]
percentiles = np.percentile(data, p)
print("\nPercentiles:")
for pi, pv in zip(p, percentiles):
    print(f"  P{pi:2d}: {pv:.4f}")

q1, q3 = np.percentile(data, [25, 75])
print(f"\nIQR: {q3 - q1:.4f}")

# 2D stats
matrix = np.random.randint(1, 100, (4, 5))
print("\n2D array:\n", matrix)
print("Column means:", np.mean(matrix, axis=0).round(2))
print("Row means:   ", np.mean(matrix, axis=1).round(2))

# Cumulative
arr = np.array([1, 2, 3, 4, 5])
print("\nCumsum:", np.cumsum(arr))
print("Cumprod:", np.cumprod(arr))
```
</details>

---

### I3 — Broadcasting

**Question:**
Demonstrate NumPy broadcasting rules with practical examples: normalising a matrix row-wise, adding vectors to matrices, and outer product computation.

**Hints:**
- Arrays are compatible if dimensions are equal or one of them is 1

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

# Rule demonstration
a = np.array([[1, 2, 3],    # shape (2,3)
              [4, 5, 6]])
b = np.array([10, 20, 30])  # shape (3,) → broadcasts to (2,3)

print("a shape:", a.shape, "   b shape:", b.shape)
print("a + b:\n", a + b)

# Broadcast column vector
col = np.array([[100], [200]])  # shape (2,1) → broadcasts to (2,3)
print("\na + col:\n", a + col)

# Row-wise normalisation (subtract row mean, divide by row std)
matrix = np.array([[10, 20, 30, 40],
                   [1,   5, 10, 20],
                   [50, 60, 70, 80]], dtype=float)

row_mean = matrix.mean(axis=1, keepdims=True)   # shape (3,1)
row_std  = matrix.std(axis=1, keepdims=True)
normalised = (matrix - row_mean) / row_std
print("\nRow-normalised:\n", normalised.round(4))

# Outer product via broadcasting
x = np.array([1, 2, 3, 4])
y = np.array([10, 20, 30])
outer = x[:, np.newaxis] * y[np.newaxis, :]  # (4,1) × (1,3) → (4,3)
print("\nOuter product (4×3):\n", outer)

# Distance matrix between 2 sets of points
points_a = np.array([[0,0],[1,0],[0,1]])  # shape (3,2)
points_b = np.array([[2,2],[3,1]])         # shape (2,2)
diff = points_a[:, np.newaxis, :] - points_b[np.newaxis, :, :]  # (3,2,2)
distances = np.sqrt((diff**2).sum(axis=2))
print("\nDistance matrix (3 pts × 2 pts):\n", distances.round(4))
```
</details>

---

### I4 — Aggregation Along Axes

**Question:**
Work with a 3D sales array (shape: regions × months × products) and compute aggregations along different axes to answer business questions.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

# 3D array: 4 regions × 12 months × 3 products
np.random.seed(7)
sales = np.random.randint(100, 1000, size=(4, 12, 3))

regions  = ["North", "South", "East", "West"]
products = ["Widget A", "Widget B", "Widget C"]

print("Sales array shape:", sales.shape)

# Total sales per region (sum over months and products)
total_per_region = sales.sum(axis=(1, 2))
print("\nTotal sales per region:")
for r, v in zip(regions, total_per_region):
    print(f"  {r}: {v:,}")

# Best month per region (max over months, then which month)
best_month_idx = sales.sum(axis=2).argmax(axis=1)
print("\nBest month per region:")
for r, m in zip(regions, best_month_idx):
    print(f"  {r}: Month {m+1}")

# Average monthly sales per product
avg_per_product = sales.mean(axis=(0, 1))
print("\nAvg monthly sales per product:")
for p, v in zip(products, avg_per_product):
    print(f"  {p}: {v:.1f}")

# Cumulative sales over months per region×product
cumulative = sales.cumsum(axis=1)
print("\nCumulative shape:", cumulative.shape)
print("Region 0, Product 0 cumulative (12 months):", cumulative[0, :, 0])
```
</details>

---

### I5 — Vectorised String and Date Operations

**Question:**
Use `np.char` functions for string arrays and `np.datetime64` for date arithmetic.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

# String array operations
names = np.array(["alice", "BOB", "Charlie", "  diana  ", "eve"])

print("Original:", names)
print("Upper:   ", np.char.upper(names))
print("Title:   ", np.char.title(names))
print("Strip:   ", np.char.strip(names))
print("Length:  ", np.char.str_len(np.char.strip(names)))
print("Starts A:", np.char.startswith(np.char.lower(names), "a"))

# String concatenation
first = np.array(["John", "Jane", "Bob"])
last  = np.array(["Smith", "Doe", "Jones"])
full  = np.char.add(np.char.add(first, " "), last)
print("\nFull names:", full)

# Datetime64
dates = np.array(["2024-01-15", "2024-06-20", "2024-12-31"], dtype="datetime64")
print("\nDates:", dates)
print("Year only:", dates.astype("datetime64[Y]"))
print("+ 30 days:", dates + np.timedelta64(30, "D"))

# Date differences
start = np.datetime64("2024-01-01")
end   = np.datetime64("2024-12-31")
delta = end - start
print(f"\nDays in 2024: {delta.astype(int)}")
```
</details>

---

### I6 — Polynomial Operations

**Question:**
Use `np.poly1d` and `np.polyfit` to fit a polynomial to noisy data, evaluate it, differentiate, and integrate it.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

# Define a polynomial: 3x³ - 2x² + x - 5
coeffs = [3, -2, 1, -5]
p = np.poly1d(coeffs)
print("Polynomial:", p)
print("p(2) =", p(2))
print("p(0) =", p(0))

# Derivative and integral
dp = p.deriv()
ip = p.integ()
print("\nDerivative:", dp)
print("Integral:  ", ip)

# Roots
roots = np.roots(coeffs)
print("\nRoots:", np.round(roots, 4))

# Polynomial fitting to noisy data
np.random.seed(42)
x = np.linspace(-3, 3, 50)
y_true = 2*x**3 - x**2 + 3*x - 1
y_noisy = y_true + np.random.normal(0, 5, len(x))

# Fit degree-3 polynomial
fit_coeffs = np.polyfit(x, y_noisy, deg=3)
y_fit = np.polyval(fit_coeffs, x)

residuals = y_noisy - y_fit
print("\nFitted coefficients:", np.round(fit_coeffs, 3))
print("True coefficients:  ", [2, -1, 3, -1])
print("RMSE:", np.round(np.sqrt(np.mean(residuals**2)), 4))
```
</details>

---

## 🔵 Upper Intermediate — Linear Algebra & Matrix Ops

---

### L1 — Matrix Multiplication

**Question:**
Demonstrate the difference between element-wise multiplication and matrix multiplication. Solve a simple system of linear equations.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("A:\n", A)
print("\nB:\n", B)

# Element-wise
print("\nElement-wise (A * B):\n", A * B)

# Matrix multiplication
print("\nMatrix mult (A @ B):\n", A @ B)
print("np.dot(A,B):\n", np.dot(A, B))
print("np.matmul(A,B):\n", np.matmul(A, B))

# Solve system of linear equations: Ax = b
# 2x + y = 8
# x + 3y = 9
A_sys = np.array([[2, 1], [1, 3]], dtype=float)
b_sys = np.array([8, 9], dtype=float)
x = np.linalg.solve(A_sys, b_sys)
print(f"\nSolution: x={x[0]:.4f}, y={x[1]:.4f}")
print("Verification Ax:", A_sys @ x)
```
</details>

---

### L2 — Determinant, Inverse and Rank

**Question:**
Compute the determinant, inverse, rank, and condition number of matrices. Demonstrate what happens with singular matrices.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

A = np.array([[4, 7], [2, 6]], dtype=float)

print("Matrix A:\n", A)
print("\nDeterminant:", np.linalg.det(A))
print("\nInverse:\n", np.linalg.inv(A))
print("\nVerify A × A⁻¹ ≈ I:\n", np.round(A @ np.linalg.inv(A), 10))
print("\nRank:", np.linalg.matrix_rank(A))
print("Condition number:", np.linalg.cond(A))

# Singular matrix (det = 0)
singular = np.array([[1, 2], [2, 4]], dtype=float)
print("\nSingular matrix:\n", singular)
print("Determinant:", np.linalg.det(singular))

try:
    np.linalg.inv(singular)
except np.linalg.LinAlgError as e:
    print("Error:", e)

# Pseudo-inverse for singular/non-square
pinv = np.linalg.pinv(singular)
print("Pseudo-inverse:\n", np.round(pinv, 4))

# 3×4 matrix
B = np.random.randint(1, 10, (3, 4))
print("\n3×4 matrix rank:", np.linalg.matrix_rank(B))
print("Pseudo-inverse shape:", np.linalg.pinv(B).shape)
```
</details>

---

### L3 — Eigenvalues and Eigenvectors

**Question:**
Compute eigenvalues and eigenvectors of a symmetric matrix. Verify the decomposition and use it to understand the matrix geometrically (PCA-like).

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

# Symmetric matrix (guaranteed real eigenvalues)
A = np.array([[4, 2, 1],
              [2, 5, 3],
              [1, 3, 6]], dtype=float)

eigenvalues, eigenvectors = np.linalg.eig(A)
print("Matrix A:\n", A)
print("\nEigenvalues:", np.round(eigenvalues, 4))
print("\nEigenvectors (columns):\n", np.round(eigenvectors, 4))

# Verify: A @ v = λ @ v
for i in range(len(eigenvalues)):
    lhs = A @ eigenvectors[:, i]
    rhs = eigenvalues[i] * eigenvectors[:, i]
    print(f"\nVerify λ{i+1}: max diff = {np.max(np.abs(lhs - rhs)):.2e}")

# Reconstruct A from eigendecomposition: A = Q @ diag(λ) @ Q⁻¹
Q = eigenvectors
Q_inv = np.linalg.inv(Q)
A_reconstructed = Q @ np.diag(eigenvalues) @ Q_inv
print("\nReconstruction error:", np.max(np.abs(A - A_reconstructed)))

# For symmetric matrices use eigh (more stable)
vals, vecs = np.linalg.eigh(A)
print("\neigh eigenvalues (sorted):", np.round(vals, 4))
```
</details>

---

### L4 — Singular Value Decomposition (SVD)

**Question:**
Apply SVD to decompose a matrix, reconstruct it with different numbers of singular values (low-rank approximation), and measure reconstruction error.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

np.random.seed(42)
A = np.random.randint(1, 20, (6, 4)).astype(float)
print("Matrix A:\n", A)
print("Shape:", A.shape)

# Full SVD: A = U @ Σ @ Vt
U, sigma, Vt = np.linalg.svd(A, full_matrices=True)
print("\nU shape:", U.shape)
print("Sigma:", np.round(sigma, 4))
print("Vt shape:", Vt.shape)

# Reconstruct exact
S = np.zeros((6, 4))
np.fill_diagonal(S, sigma)
A_reconstructed = U @ S @ Vt
print("\nReconstruction error (full):", np.max(np.abs(A - A_reconstructed)).round(10))

# Low-rank approximations
print("\nLow-rank approximation errors:")
for k in range(1, len(sigma)+1):
    A_k = U[:, :k] @ np.diag(sigma[:k]) @ Vt[:k, :]
    err = np.linalg.norm(A - A_k, "fro")
    var = (sigma[:k]**2).sum() / (sigma**2).sum() * 100
    print(f"  k={k}: Frobenius error={err:.4f}, variance explained={var:.1f}%")
```
</details>

---

### L5 — Solving Least Squares Problems

**Question:**
Use `np.linalg.lstsq` to fit a linear regression model to data with noise, and compare with the normal equations.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

np.random.seed(0)
n = 50

# True model: y = 3x₁ + 2x₂ - x₃ + 5 + noise
X = np.random.randn(n, 3)
true_weights = np.array([3, 2, -1, 5])  # including bias
X_aug = np.column_stack([X, np.ones(n)])  # add bias column
y = X_aug @ true_weights + np.random.randn(n) * 0.5

# Method 1: lstsq
weights_lstsq, residuals, rank, sv = np.linalg.lstsq(X_aug, y, rcond=None)
print("True weights:   ", true_weights)
print("Fitted (lstsq): ", np.round(weights_lstsq, 4))

# Method 2: Normal equations (X^T X)^(-1) X^T y
weights_normal = np.linalg.inv(X_aug.T @ X_aug) @ X_aug.T @ y
print("Fitted (normal):", np.round(weights_normal, 4))

# Evaluate
y_pred = X_aug @ weights_lstsq
ss_res = np.sum((y - y_pred)**2)
ss_tot = np.sum((y - y.mean())**2)
r2 = 1 - ss_res / ss_tot
rmse = np.sqrt(ss_res / n)

print(f"\nR²:   {r2:.6f}")
print(f"RMSE: {rmse:.6f}")
```
</details>

---

### L6 — QR and Cholesky Decomposition

**Question:**
Compute QR and Cholesky decompositions, verify their properties, and use them to solve linear systems efficiently.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

# ── QR Decomposition ──────────────────────────────────────────────────────────
A = np.array([[12, -51,  4],
              [ 6, 167, -68],
              [-4,  24, -41]], dtype=float)

Q, R = np.linalg.qr(A)
print("QR Decomposition")
print("Q (orthogonal):\n", np.round(Q, 4))
print("R (upper triangular):\n", np.round(R, 4))
print("Q^T @ Q ≈ I:\n", np.round(Q.T @ Q, 10))
print("Reconstruction error:", np.max(np.abs(A - Q @ R)).round(12))

# ── Cholesky Decomposition ─────────────────────────────────────────────────────
# Cholesky requires symmetric positive definite matrix
B = np.array([[4, 2, 2],
              [2, 5, 3],
              [2, 3, 6]], dtype=float)

L = np.linalg.cholesky(B)
print("\nCholesky Decomposition")
print("L (lower triangular):\n", np.round(L, 4))
print("Reconstruction L @ L^T:\n", np.round(L @ L.T, 4))

# Solve B @ x = b using Cholesky factors (faster for SPD matrices)
b = np.array([1, 2, 3], dtype=float)
x = np.linalg.solve(B, b)
print("\nSolution x:", np.round(x, 6))
print("Verify B @ x:", np.round(B @ x, 6))
```
</details>

---

## 🔴 Advanced — Random, Structured Arrays & FFT

---

### A1 — Random Number Generation (Modern API)

**Question:**
Use NumPy's modern `np.random.default_rng()` Generator API to create reproducible experiments with various distributions.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

# Modern API (preferred over np.random.seed)
rng = np.random.default_rng(seed=42)

# Common distributions
uniform    = rng.uniform(low=0,   high=10,   size=5)
normal     = rng.normal(loc=50,   scale=15,  size=5)
integers   = rng.integers(low=1,  high=100,  size=5)
binomial   = rng.binomial(n=10,   p=0.3,     size=5)
poisson    = rng.poisson(lam=5,             size=5)
exponential= rng.exponential(scale=2,       size=5)
beta_dist  = rng.beta(a=2,        b=5,       size=5)

for name, arr in [("Uniform",    uniform),
                   ("Normal",     normal),
                   ("Integers",   integers),
                   ("Binomial",   binomial),
                   ("Poisson",    poisson),
                   ("Exponential",exponential),
                   ("Beta",       beta_dist)]:
    print(f"{name:12s}: {np.round(arr, 3)}")

# Monte Carlo: estimate π
n = 10_000_000
x = rng.uniform(-1, 1, n)
y = rng.uniform(-1, 1, n)
inside = (x**2 + y**2) <= 1
pi_est = 4 * inside.mean()
print(f"\nMonte Carlo π estimate ({n:,} points): {pi_est:.5f}")
print(f"True π:                              {np.pi:.5f}")

# Shuffle and choice
arr = np.arange(10)
rng.shuffle(arr)
print("\nShuffled:", arr)
print("Sample 3:", rng.choice(arr, size=3, replace=False))
```
</details>

---

### A2 — Structured Arrays

**Question:**
Create a structured NumPy array (like a typed record/table) for storing heterogeneous data. Perform sorting, filtering, and field access.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

# Define a structured dtype
dtype = np.dtype([
    ("name",   "U20"),     # Unicode string, max 20 chars
    ("age",    np.int32),
    ("salary", np.float64),
    ("active", np.bool_)
])

# Create structured array
employees = np.array([
    ("Alice",   28, 75000.0, True),
    ("Bob",     35, 92000.0, True),
    ("Charlie", 42, 68000.0, False),
    ("Diana",   29, 88000.0, True),
    ("Eve",     51, 110000.0, True),
], dtype=dtype)

# Field access
print("Names:", employees["name"])
print("Salaries:", employees["salary"])
print("\nActive employees:")
print(employees[employees["active"]])

# Sort by salary descending
sorted_emp = np.sort(employees, order="salary")[::-1]
print("\nSorted by salary:")
for emp in sorted_emp:
    print(f"  {emp['name']:10s} | Age: {emp['age']} | Salary: ${emp['salary']:,.0f}")

# Compute on fields
print(f"\nAvg salary (active): ${employees[employees['active']]['salary'].mean():,.2f}")
print(f"Oldest employee: {employees['name'][employees['age'].argmax()]}")
```
</details>

---

### A3 — Fast Fourier Transform (FFT)

**Question:**
Apply FFT to a composite signal to identify its frequency components. Compute the power spectrum and find dominant frequencies.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

# Compose a signal: 5 Hz + 10 Hz + 20 Hz + noise
sample_rate = 1000   # Hz
duration    = 1.0    # seconds
t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)

np.random.seed(42)
signal = (
    3.0 * np.sin(2 * np.pi * 5  * t) +   # 5 Hz, amplitude 3
    1.5 * np.sin(2 * np.pi * 10 * t) +   # 10 Hz, amplitude 1.5
    0.8 * np.sin(2 * np.pi * 20 * t) +   # 20 Hz, amplitude 0.8
    0.5 * np.random.randn(len(t))         # noise
)

# Apply FFT
fft_values  = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(t), d=1/sample_rate)
power       = np.abs(fft_values) ** 2

# Take only positive frequencies
pos_mask = frequencies > 0
pos_freq = frequencies[pos_mask]
pos_pwr  = power[pos_mask]

# Find top 5 dominant frequencies
top_idx = np.argsort(pos_pwr)[-5:][::-1]
print("Top dominant frequencies:")
for idx in top_idx:
    print(f"  {pos_freq[idx]:6.1f} Hz  | Power: {pos_pwr[idx]:.1f}")

# Inverse FFT
reconstructed = np.fft.ifft(fft_values).real
print(f"\nReconstruction error: {np.max(np.abs(signal - reconstructed)):.2e}")

# 2D FFT example
image = np.random.rand(8, 8)
fft2d = np.fft.fft2(image)
print("\n2D FFT shape:", fft2d.shape)
print("Recovered from IFFT2 error:", np.max(np.abs(image - np.fft.ifft2(fft2d).real)))
```
</details>

---

### A4 — Convolution and Correlation

**Question:**
Apply 1D convolution for smoothing a signal and compute cross-correlation to find the time delay between two signals.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

np.random.seed(0)
# Noisy signal
signal = np.sin(np.linspace(0, 4*np.pi, 100)) + 0.5*np.random.randn(100)

# Moving average kernel
window = 5
kernel = np.ones(window) / window

# Convolution for smoothing
smoothed_full  = np.convolve(signal, kernel, mode="full")
smoothed_same  = np.convolve(signal, kernel, mode="same")
smoothed_valid = np.convolve(signal, kernel, mode="valid")

print("Original length: ", len(signal))
print("Mode='full':  ", len(smoothed_full))
print("Mode='same':  ", len(smoothed_same))
print("Mode='valid': ", len(smoothed_valid))
print("\nSmoothing error (same):", np.std(signal - smoothed_same).round(4))

# Cross-correlation: find time delay
delay = 15
signal_a = np.sin(np.linspace(0, 4*np.pi, 200))
signal_b = np.roll(signal_a, delay)   # shift by delay samples

corr = np.correlate(signal_a, signal_b, mode="full")
lags = np.arange(-(len(signal_a)-1), len(signal_a))
detected_delay = lags[np.argmax(corr)]
print(f"\nTrue delay:     {delay} samples")
print(f"Detected delay: {detected_delay} samples")
```
</details>

---

### A5 — Masked Arrays

**Question:**
Use `np.ma` (masked arrays) to handle missing or invalid data without manually tracking NaN locations.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np
import numpy.ma as ma

# Create masked array (mask=True means invalid)
data = np.array([1.0, -999, 3.5, 4.2, -999, 6.1, 7.8, -999, 9.0])
masked = ma.masked_where(data == -999, data)

print("Original:  ", data)
print("Masked:    ", masked)
print("Valid data:", masked.compressed())

print("\nMean (masked):", masked.mean().round(4))
print("Mean (naive): ", data.mean().round(4))   # wrong — includes -999

# Masked 2D array
sensor = ma.array(
    [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9,10,11,12]],
    mask=[[0,0,1,0],   # mask element [0,2]
          [0,1,0,0],   # mask element [1,1]
          [0,0,0,1]]   # mask element [2,3]
)

print("\n2D masked array:\n", sensor)
print("Column means:", sensor.mean(axis=0))
print("Row means:   ", sensor.mean(axis=1))
print("Overall mean:", sensor.mean())

# Fill masked values for export
filled = sensor.filled(fill_value=0)
print("\nFilled with 0:\n", filled)
```
</details>

---

## ⚫ Expert — Vectorisation, Memory & Custom ufuncs

---

### X1 — Memory Layout: C vs Fortran Order

**Question:**
Demonstrate how C-order (row-major) vs Fortran-order (column-major) memory layout affects traversal performance. Measure cache efficiency.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np
import time

n = 5000

# Create arrays in different memory orders
c_order = np.random.rand(n, n)                    # default C order
f_order = np.asfortranarray(c_order)              # Fortran order

print("C-order contiguous:", c_order.flags["C_CONTIGUOUS"])
print("F-order contiguous:", f_order.flags["F_CONTIGUOUS"])
print("Strides C:", c_order.strides)
print("Strides F:", f_order.strides)

# Row-wise sum — faster for C-order (rows are contiguous)
t0 = time.time()
_ = c_order.sum(axis=1)
t_c_row = time.time() - t0

t0 = time.time()
_ = f_order.sum(axis=1)
t_f_row = time.time() - t0

# Column-wise sum — faster for F-order
t0 = time.time()
_ = c_order.sum(axis=0)
t_c_col = time.time() - t0

t0 = time.time()
_ = f_order.sum(axis=0)
t_f_col = time.time() - t0

print(f"\nRow sum    C-order: {t_c_row:.4f}s | F-order: {t_f_row:.4f}s")
print(f"Column sum C-order: {t_c_col:.4f}s | F-order: {t_f_col:.4f}s")

# Views with np.ascontiguousarray
transposed = c_order.T
print(f"\nTransposed C_CONTIGUOUS: {transposed.flags['C_CONTIGUOUS']}")
contiguous_T = np.ascontiguousarray(transposed)
print(f"After ascontiguousarray: {contiguous_T.flags['C_CONTIGUOUS']}")
```
</details>

---

### X2 — Custom ufunc with np.frompyfunc and np.vectorize

**Question:**
Create custom universal functions using `np.frompyfunc`, `np.vectorize`, and compare their performance against a Cython-style loop.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np
import time

# A custom function
def complex_formula(x, threshold=5):
    if x > threshold:
        return np.sqrt(x) * np.log(x + 1)
    else:
        return x ** 2

# Method 1: np.vectorize (convenience, not speed)
vfunc = np.vectorize(complex_formula)

# Method 2: np.frompyfunc (returns object array, faster for Python logic)
ufunc = np.frompyfunc(complex_formula, 1, 1)

# Method 3: Fully vectorised (fastest — pure NumPy)
def vectorised_formula(x, threshold=5):
    result = np.where(x > threshold,
                      np.sqrt(x) * np.log(x + 1),
                      x ** 2)
    return result

arr = np.random.uniform(0, 20, 500_000)

# Benchmark
t0 = time.time()
r1 = vfunc(arr)
print(f"np.vectorize:  {time.time()-t0:.4f}s")

t0 = time.time()
r2 = ufunc(arr).astype(float)
print(f"np.frompyfunc: {time.time()-t0:.4f}s")

t0 = time.time()
r3 = vectorised_formula(arr)
print(f"Vectorised:    {time.time()-t0:.4f}s")

# Verify all give same results
print("\nResults match:", np.allclose(r1, r3), np.allclose(r2, r3))

# Custom ufunc with accumulate / reduce
add_ufunc = np.frompyfunc(lambda a, b: a + b, 2, 1)
small = np.array([1, 2, 3, 4, 5])
print("\nadd reduce:", add_ufunc.reduce(small))
print("add accumulate:", add_ufunc.accumulate(small))
```
</details>

---

### X3 — Stride Tricks and Views

**Question:**
Use `np.lib.stride_tricks` to create efficient sliding window views without copying data, and understand strides for custom memory access patterns.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view, as_strided

arr = np.arange(20, dtype=float)

# Sliding window view (no copy, zero overhead)
windows = sliding_window_view(arr, window_shape=5)
print("Array:", arr)
print("Window shape:", windows.shape)
print("First 3 windows:\n", windows[:3])

# Rolling mean using stride tricks (very efficient)
rolling_mean = windows.mean(axis=1)
print("\nRolling mean (window=5):", rolling_mean.round(2))

# Manual stride tricks — as_strided (advanced, use with care!)
# Create a 2D sliding window manually
x = np.arange(15, dtype=float)
itemsize = x.itemsize
window_size = 4
stride = 1

n_windows = (len(x) - window_size) // stride + 1
shape    = (n_windows, window_size)
strides  = (itemsize * stride, itemsize)

strided_view = as_strided(x, shape=shape, strides=strides)
print("\nas_strided (window=4, stride=1):\n", strided_view)
print("Shares memory with original:", np.shares_memory(x, strided_view))

# 2D sliding window on an image-like array
img = np.arange(25).reshape(5, 5)
patches = sliding_window_view(img, (3, 3))
print(f"\n2D sliding patches shape: {patches.shape}")
print(f"Each patch is 3×3, from a 5×5 image")
```
</details>

---

### X4 — Einsum for Tensor Operations

**Question:**
Use `np.einsum` to express matrix operations, batch operations, and tensor contractions in a concise and efficient notation.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np
import time

A = np.random.rand(4, 3)
B = np.random.rand(3, 5)
C = np.random.rand(4, 4)

# Matrix operations with einsum
print("Matrix mult A@B:")
print("np.dot:    ", (A @ B).shape)
print("einsum ij,jk→ik:", np.einsum("ij,jk->ik", A, B).shape)
print("Match:", np.allclose(A @ B, np.einsum("ij,jk->ik", A, B)))

# Trace (sum of diagonal)
print("\nTrace of C:")
print("np.trace:      ", np.trace(C))
print("einsum ii→:    ", np.einsum("ii->", C))

# Outer product
x = np.array([1, 2, 3])
y = np.array([4, 5, 6, 7])
print("\nOuter product:")
print("np.outer:", np.outer(x, y).shape)
print("einsum i,j→ij:", np.einsum("i,j->ij", x, y))

# Batch matrix multiply (3D)
batch_A = np.random.rand(10, 4, 3)   # 10 matrices of shape 4×3
batch_B = np.random.rand(10, 3, 5)   # 10 matrices of shape 3×5
batch_C = np.einsum("bij,bjk->bik", batch_A, batch_B)
print("\nBatch matmul:", batch_C.shape)

# Benchmark: einsum vs matmul for batch
t0 = time.time()
_ = np.einsum("bij,bjk->bik", batch_A, batch_B)
print(f"\nEinsum batch: {time.time()-t0:.6f}s")

t0 = time.time()
_ = np.matmul(batch_A, batch_B)
print(f"Matmul batch: {time.time()-t0:.6f}s")
```
</details>

---

### X5 — Vectorised Algorithms from Scratch

**Question:**
Implement three classic algorithms in a fully vectorised NumPy style: k-means clustering, numerical gradient computation, and Conway's Game of Life.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

# ── 1. Vectorised K-Means ─────────────────────────────────────────────────────
def kmeans(X, k, n_iter=100, seed=42):
    rng = np.random.default_rng(seed)
    centroids = X[rng.choice(len(X), k, replace=False)]

    for _ in range(n_iter):
        # Distances: (n_samples, k)
        dists = np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
        labels = dists.argmin(axis=1)
        new_centroids = np.array([X[labels == j].mean(axis=0) for j in range(k)])
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids

    return labels, centroids

np.random.seed(0)
X = np.vstack([np.random.randn(50, 2) + c for c in [(0,0),(5,5),(-5,5)]])
labels, centroids = kmeans(X, k=3)
print("K-Means cluster sizes:", np.bincount(labels))
print("Centroids:\n", centroids.round(3))

# ── 2. Numerical Gradient ─────────────────────────────────────────────────────
def numerical_gradient(f, x, h=1e-5):
    grad = np.zeros_like(x)
    for i in range(len(x)):
        x_plus  = x.copy(); x_plus[i]  += h
        x_minus = x.copy(); x_minus[i] -= h
        grad[i] = (f(x_plus) - f(x_minus)) / (2 * h)
    return grad

f = lambda x: x[0]**2 + 3*x[1]**2 - 2*x[0]*x[1]
x0 = np.array([1.0, 2.0])
grad = numerical_gradient(f, x0)
print(f"\nNumerical gradient at {x0}: {grad}")
print(f"Analytical gradient:         {np.array([2*x0[0]-2*x0[1], 6*x0[1]-2*x0[0]])}")

# ── 3. Conway's Game of Life (vectorised) ────────────────────────────────────
def game_of_life_step(grid):
    # Count neighbours using convolution-like sliding
    neighbours = sum(
        np.roll(np.roll(grid, i, axis=0), j, axis=1)
        for i in (-1, 0, 1) for j in (-1, 0, 1)
        if (i != 0 or j != 0)
    )
    return ((neighbours == 3) | (grid & (neighbours == 2))).astype(int)

# Glider pattern
grid = np.zeros((10, 10), dtype=int)
glider = [(0,1),(1,2),(2,0),(2,1),(2,2)]
for r, c in glider:
    grid[r, c] = 1

print("\nGame of Life — Glider after 4 steps:")
print("Initial:\n", grid[:5, :5])
for _ in range(4):
    grid = game_of_life_step(grid)
print("After 4 steps:\n", grid[:5, :5])
```
</details>

---

### X6 — Memory-Mapped Arrays for Out-of-Core Processing

**Question:**
Create and process a large array stored on disk using `np.memmap`, which allows working with arrays larger than RAM.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np
import os
import tempfile

# Create a memory-mapped file
tmpdir = tempfile.mkdtemp()
filename = os.path.join(tmpdir, "large_array.npy")

shape = (10_000, 500)   # 40 MB if float64
dtype = np.float32       # 20 MB as float32

# Write mode: create
mm_write = np.memmap(filename, dtype=dtype, mode="w+", shape=shape)

# Fill in chunks (simulating out-of-core processing)
chunk_size = 1000
for start in range(0, shape[0], chunk_size):
    end = min(start + chunk_size, shape[0])
    mm_write[start:end, :] = np.random.rand(end - start, shape[1]).astype(dtype)

mm_write.flush()   # write to disk
del mm_write

# Read mode: re-open without loading into RAM
mm_read = np.memmap(filename, dtype=dtype, mode="r", shape=shape)

# Process in chunks
col_means = np.zeros(shape[1], dtype=np.float64)
for start in range(0, shape[0], chunk_size):
    end = min(start + chunk_size, shape[0])
    col_means += mm_read[start:end, :].sum(axis=0)
col_means /= shape[0]

print(f"Array size on disk: {os.path.getsize(filename)/1e6:.1f} MB")
print(f"Shape: {mm_read.shape}, dtype: {mm_read.dtype}")
print(f"Column mean range: [{col_means.min():.4f}, {col_means.max():.4f}]")
print(f"Expected (≈0.5): {col_means.mean():.4f}")

# Cleanup
del mm_read
os.remove(filename)
os.rmdir(tmpdir)
```
</details>

---

### X7 — Complete Numerical Pipeline: Image Compression via SVD

**Question:**
Implement a complete image compression algorithm using SVD. Measure compression ratio and reconstruction quality (PSNR) at different rank levels.

<details>
<summary>💡 View Solution</summary>

```python
import numpy as np

# Simulate a grayscale image (256×256)
np.random.seed(42)
x = np.linspace(0, 4*np.pi, 256)
y = np.linspace(0, 4*np.pi, 256)
X, Y = np.meshgrid(x, y)
image = (np.sin(X) * np.cos(Y) * 127.5 + 127.5).astype(np.float64)
print(f"Image shape: {image.shape}, dtype: {image.dtype}")
print(f"Pixel range: [{image.min():.1f}, {image.max():.1f}]")

# SVD decomposition
U, sigma, Vt = np.linalg.svd(image, full_matrices=False)
print(f"\nFull SVD shapes: U{U.shape}, σ{sigma.shape}, Vt{Vt.shape}")
print(f"Original storage: {image.size} values")

def compress(U, sigma, Vt, k):
    return U[:, :k] @ np.diag(sigma[:k]) @ Vt[:k, :]

def psnr(original, compressed, max_val=255):
    mse = np.mean((original - compressed)**2)
    if mse == 0:
        return float("inf")
    return 20 * np.log10(max_val / np.sqrt(mse))

def storage_ratio(original, k, shape):
    orig_size = shape[0] * shape[1]
    compressed_size = shape[0]*k + k + k*shape[1]
    return compressed_size / orig_size

print(f"\n{'Rank':>6} | {'Storage %':>10} | {'PSNR (dB)':>10} | {'Max Error':>10}")
print("-" * 50)
for k in [1, 5, 10, 20, 50, 100, 128]:
    approx  = compress(U, sigma, Vt, k)
    approx  = np.clip(approx, 0, 255)
    ratio   = storage_ratio(image, k, image.shape)
    p       = psnr(image, approx)
    max_err = np.max(np.abs(image - approx))
    print(f"{k:>6} | {ratio*100:>9.1f}% | {p:>10.2f} | {max_err:>10.2f}")

# Variance explained
variance_explained = (sigma**2).cumsum() / (sigma**2).sum()
k_95 = np.searchsorted(variance_explained, 0.95) + 1
k_99 = np.searchsorted(variance_explained, 0.99) + 1
print(f"\nRank for 95% variance: {k_95}")
print(f"Rank for 99% variance: {k_99}")
```
</details>

---

## 📝 Quick Reference Cheat Sheet

### Array Creation
```python
np.array([1,2,3])               # from list
np.zeros((m,n))                 # zeros
np.ones((m,n))                  # ones
np.eye(n)                       # identity
np.arange(start, stop, step)    # range
np.linspace(a, b, n)            # n evenly spaced
np.logspace(a, b, n)            # log spaced
np.random.rand(m,n)             # uniform [0,1)
np.random.randn(m,n)            # standard normal
np.random.randint(lo,hi,size)   # random integers
np.full((m,n), val)             # filled with val
np.empty((m,n))                 # uninitialised
```

### Array Attributes
```python
arr.shape      # tuple of dimensions
arr.ndim       # number of dimensions
arr.size       # total elements
arr.dtype      # data type
arr.nbytes     # memory in bytes
arr.itemsize   # bytes per element
arr.T          # transpose
arr.flat       # 1D iterator
```

### Reshaping
```python
arr.reshape(m,n)        # new shape (must match size)
arr.ravel()             # flatten (view if possible)
arr.flatten()           # flatten (always copy)
arr.squeeze()           # remove axes of size 1
arr[:, np.newaxis]      # add axis
np.expand_dims(arr, 0)  # add axis at position
```

### Indexing
```python
arr[i, j]           # single element
arr[1:3, :]         # slice
arr[[0,2,4]]        # fancy index
arr[arr > 5]        # boolean mask
np.where(cond,a,b)  # conditional
```

### Math & Stats
```python
np.sum / mean / std / var / min / max / median
np.cumsum / cumprod
np.percentile(arr, q)
np.corrcoef(x, y)
np.dot / matmul / einsum
np.linalg.norm
np.linalg.solve
np.linalg.eig / svd / qr / cholesky
```

### Performance Tips
```python
# Prefer vectorised ops over loops
# Use np.einsum for complex tensor ops
# Use np.memmap for large arrays
# Use sliding_window_view for windowed ops
# Downcast dtypes to save memory (float32 vs float64)
# Use np.ascontiguousarray before repeated row access
```

---

## 🔧 Setup

```bash
pip install numpy
```

```python
import numpy as np

# Useful settings
np.set_printoptions(precision=4, suppress=True, linewidth=120)
print("NumPy version:", np.__version__)
```

---

*Happy computing! 🔢*
