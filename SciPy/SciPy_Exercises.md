# 🔬 SciPy Programming Exercises — Beginner to Expert

A comprehensive collection of SciPy exercises spanning scientific computing, statistics, signal processing, optimisation, and more. Every exercise includes a problem description, hints, and a collapsible solution.

---

## 📋 Table of Contents

- [Level Guide](#-level-guide)
- [🟢 Beginner — SciPy Fundamentals](#-beginner--scipy-fundamentals)
- [🟡 Elementary — Statistics & Probability](#-elementary--statistics--probability)
- [🟠 Intermediate — Optimisation & Root Finding](#-intermediate--optimisation--root-finding)
- [🔵 Upper Intermediate — Linear Algebra & Interpolation](#-upper-intermediate--linear-algebra--interpolation)
- [🔴 Advanced — Signal Processing & ODE Solvers](#-advanced--signal-processing--ode-solvers)
- [⚫ Expert — Sparse Matrices, Integration & Pipelines](#-expert--sparse-matrices-integration--pipelines)
- [📝 Quick Reference Cheat Sheet](#-quick-reference-cheat-sheet)

---

## 📊 Level Guide

| Level | Label | Description |
|-------|-------|-------------|
| 🟢 **1** | Beginner | SciPy ecosystem, constants, basic special functions |
| 🟡 **2** | Elementary | Descriptive stats, distributions, hypothesis testing |
| 🟠 **3** | Intermediate | Optimisation, minimisation, root finding |
| 🔵 **4** | Upper Intermediate | Interpolation, linear algebra, spatial algorithms |
| 🔴 **5** | Advanced | Signal processing, ODE solvers, image processing |
| ⚫ **6** | Expert | Sparse matrices, numerical integration, full scientific pipelines |

---

## 🟢 Beginner — SciPy Fundamentals

---

### B1 — Explore SciPy Constants

**Question:**
Use `scipy.constants` to retrieve physical and mathematical constants. Perform a unit conversion using built-in conversion factors.

**Hints:**
- Use `scipy.constants.find()` to search for constants
- Physical constants are in SI units

<details>
<summary>💡 View Solution</summary>

```python
from scipy import constants
import scipy.constants as const

# Mathematical constants
print("=== Mathematical Constants ===")
print(f"π (pi):        {const.pi}")
print(f"Golden ratio:  {const.golden}")
print(f"e:             {const.e}")

# Physical constants
print("\n=== Physical Constants (SI) ===")
print(f"Speed of light:    {const.c:,.0f} m/s")
print(f"Planck constant:   {const.h:.4e} J·s")
print(f"Gravitational:     {const.G:.4e} m³/(kg·s²)")
print(f"Boltzmann:         {const.k:.4e} J/K")
print(f"Avogadro:          {const.N_A:.4e} mol⁻¹")
print(f"Electron mass:     {const.m_e:.4e} kg")
print(f"Proton mass:       {const.m_p:.4e} kg")
print(f"Elementary charge: {const.e:.4e} C")

# Unit conversions
print("\n=== Unit Conversions ===")
print(f"1 eV in Joules:     {const.eV:.4e}")
print(f"1 atm in Pascals:   {const.atm:,.2f}")
print(f"1 inch in metres:   {const.inch:.6f}")
print(f"1 mile in metres:   {const.mile:,.2f}")
print(f"0°C in Kelvin:      {const.zero_Celsius}")

# Search for constants
results = const.find("light")
print("\nConstants containing 'light':", results)
```
</details>

---

### B2 — Special Functions

**Question:**
Explore SciPy special functions: gamma, beta, Bessel functions, error function, and combinatorials. Show their mathematical relationships.

**Hints:**
- Use `scipy.special`
- `gamma(n+1) = n!` for positive integers

<details>
<summary>💡 View Solution</summary>

```python
from scipy import special
import numpy as np

# Gamma function: Γ(n+1) = n!
print("=== Gamma Function ===")
for n in range(1, 7):
    print(f"  Γ({n}) = {special.gamma(n):.1f}   (= {n-1}!)")

# Beta function: B(a,b) = Γ(a)Γ(b)/Γ(a+b)
print("\n=== Beta Function ===")
a, b = 2.0, 3.0
beta_val = special.beta(a, b)
print(f"  B({a},{b}) = {beta_val:.6f}")
print(f"  Γ(a)Γ(b)/Γ(a+b) = {special.gamma(a)*special.gamma(b)/special.gamma(a+b):.6f}")

# Error function
print("\n=== Error Function ===")
x = np.array([0, 0.5, 1.0, 1.5, 2.0])
print("  x:      ", x)
print("  erf(x): ", np.round(special.erf(x), 6))
print("  erfc(x):", np.round(special.erfc(x), 6))  # 1 - erf(x)

# Bessel functions
print("\n=== Bessel Functions ===")
x = np.linspace(0, 10, 5)
print("  J0 (order 0):", np.round(special.j0(x), 4))
print("  J1 (order 1):", np.round(special.j1(x), 4))
print("  Y0 (Neumann):", np.round(special.y0(x[1:]), 4))  # undefined at 0

# Combinatorial
print("\n=== Combinatorics ===")
print(f"  C(10,3) = {special.comb(10,3,exact=True)}")
print(f"  P(10,3) = {special.perm(10,3,exact=True)}")
print(f"  10!     = {special.factorial(10, exact=True)}")
```
</details>

---

### B3 — Basic Linear Algebra with scipy.linalg

**Question:**
Use `scipy.linalg` (which often offers more features than `numpy.linalg`) to compute matrix operations: norm, determinant, inverse, and trace.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import linalg
import numpy as np

A = np.array([[3, 1, 2],
              [1, 4, 0],
              [2, 0, 5]], dtype=float)

print("Matrix A:\n", A)

# Basic properties
print("\nDeterminant:       ", round(linalg.det(A), 8))
print("Trace:             ", np.trace(A))
print("Matrix norm (Fro): ", round(linalg.norm(A, "fro"), 6))
print("Matrix norm (2):   ", round(linalg.norm(A, 2), 6))
print("Rank:              ", np.linalg.matrix_rank(A))

# Inverse
A_inv = linalg.inv(A)
print("\nInverse:\n", np.round(A_inv, 6))
print("\nA @ A_inv ≈ I:\n", np.round(A @ A_inv, 10))

# Matrix exponential (unique to scipy.linalg)
A_small = np.array([[1, 2], [0, 1]], dtype=float)
print("\nMatrix exponential of [[1,2],[0,1]]:")
print(np.round(linalg.expm(A_small), 6))

# Matrix logarithm
print("\nMatrix logarithm:")
print(np.round(linalg.logm(linalg.expm(A_small)), 6))
```
</details>

---

### B4 — Distance Computations with scipy.spatial.distance

**Question:**
Compute pairwise distances between points using different distance metrics: Euclidean, Manhattan, Cosine, and Hamming.

<details>
<summary>💡 View Solution</summary>

```python
from scipy.spatial.distance import euclidean, cityblock, cosine, hamming, cdist, pdist
import numpy as np

# Point-to-point distances
p1 = np.array([0, 0, 0])
p2 = np.array([3, 4, 0])

print("=== Pairwise Distances: p1=(0,0,0), p2=(3,4,0) ===")
print(f"Euclidean:  {euclidean(p1, p2):.4f}")
print(f"Manhattan:  {cityblock(p1, p2):.4f}")
print(f"Cosine:     {cosine(p1+1, p2+1):.4f}")   # cosine needs non-zero

# Binary arrays
b1 = np.array([1,0,1,1,0,1])
b2 = np.array([1,1,0,1,0,0])
print(f"\nHamming:    {hamming(b1, b2):.4f}  ({hamming(b1,b2)*len(b1):.0f}/{len(b1)} mismatches)")

# Pairwise distance matrix (pdist)
points = np.array([[0,0],[1,0],[0,1],[1,1],[0.5,0.5]])
dist_matrix = cdist(points, points, metric="euclidean")
print("\nPairwise distance matrix (5 points):")
print(np.round(dist_matrix, 4))

# Condensed form (pdist)
condensed = pdist(points, metric="euclidean")
print("\nCondensed (upper triangle):", np.round(condensed, 4))

# Find nearest neighbour for each point
np.fill_diagonal(dist_matrix, np.inf)
nearest = dist_matrix.argmin(axis=1)
print("\nNearest neighbour index for each point:", nearest)
```
</details>

---

### B5 — Sparse Matrix Basics

**Question:**
Create sparse matrices in different formats (COO, CSR, CSC), convert between them, and understand when to use each.

<details>
<summary>💡 View Solution</summary>

```python
from scipy.sparse import coo_matrix, csr_matrix, csc_matrix, eye, diags
import numpy as np

# Dense matrix with lots of zeros
dense = np.array([
    [1, 0, 0, 4],
    [0, 2, 0, 0],
    [0, 0, 3, 0],
    [5, 0, 0, 6]
], dtype=float)

print("Dense matrix:\n", dense)
print(f"Density: {np.count_nonzero(dense)}/{dense.size} = {np.count_nonzero(dense)/dense.size:.0%}")

# COO format (coordinate list) — good for construction
coo = coo_matrix(dense)
print("\nCOO format:")
print("  row:", coo.row)
print("  col:", coo.col)
print("  data:", coo.data)

# CSR format (Compressed Sparse Row) — good for row slicing
csr = csr_matrix(dense)
print("\nCSR format:")
print("  indptr:", csr.indptr)
print("  indices:", csr.indices)
print("  data:", csr.data)

# CSC format (Compressed Sparse Column) — good for column slicing
csc = csc_matrix(dense)

# Memory comparison
import sys
print(f"\nDense memory:  {dense.nbytes} bytes")
print(f"CSR memory:    {csr.data.nbytes + csr.indices.nbytes + csr.indptr.nbytes} bytes")

# Sparse identity and diagonal
sp_eye = eye(5)
diag_mat = diags([1, -2, 1], [-1, 0, 1], shape=(5, 5))
print("\nTridiagonal sparse matrix:\n", diag_mat.toarray())
```
</details>

---

## 🟡 Elementary — Statistics & Probability

---

### E1 — Descriptive Statistics

**Question:**
Use `scipy.stats` to compute descriptive statistics including skewness, kurtosis, and the geometric/harmonic mean on a dataset.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import stats
import numpy as np

np.random.seed(42)
# Slightly skewed data
data = np.concatenate([np.random.normal(50, 10, 800),
                        np.random.normal(80, 5, 200)])

print("=== Descriptive Statistics ===")
print(f"n:               {len(data)}")
print(f"Mean:            {np.mean(data):.4f}")
print(f"Trimmed mean:    {stats.trim_mean(data, 0.05):.4f}")  # 5% trim each side
print(f"Median:          {np.median(data):.4f}")
print(f"Std Dev:         {np.std(data, ddof=1):.4f}")
print(f"Skewness:        {stats.skew(data):.4f}")
print(f"Kurtosis:        {stats.kurtosis(data):.4f}")
print(f"Kurtosis excess: {stats.kurtosis(data, fisher=True):.4f}")

# Geometric and Harmonic Mean
pos_data = np.abs(data) + 1
print(f"\nGeometric Mean:  {stats.gmean(pos_data):.4f}")
print(f"Harmonic Mean:   {stats.hmean(pos_data):.4f}")

# Full summary
desc = stats.describe(data)
print(f"\nstats.describe:")
print(f"  nobs:     {desc.nobs}")
print(f"  minmax:   {desc.minmax[0]:.4f}, {desc.minmax[1]:.4f}")
print(f"  mean:     {desc.mean:.4f}")
print(f"  variance: {desc.variance:.4f}")
print(f"  skewness: {desc.skewness:.4f}")
print(f"  kurtosis: {desc.kurtosis:.4f}")

# Mode
mode_result = stats.mode(np.round(data).astype(int))
print(f"\nMode: {mode_result.mode}, count: {mode_result.count}")
```
</details>

---

### E2 — Probability Distributions

**Question:**
Work with common probability distributions: compute PDF, CDF, survival function, inverse CDF (PPF), and generate random samples.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import stats
import numpy as np

x = np.linspace(-4, 4, 100)

# Normal distribution
norm = stats.norm(loc=0, scale=1)
print("=== Normal(μ=0, σ=1) ===")
print(f"PDF at x=0:     {norm.pdf(0):.6f}")
print(f"CDF at x=1.96:  {norm.cdf(1.96):.6f}")
print(f"SF at x=1.96:   {norm.sf(1.96):.6f}")   # 1 - CDF
print(f"PPF at 0.975:   {norm.ppf(0.975):.6f}")  # quantile
print(f"Mean, Var:      {norm.mean():.4f}, {norm.var():.4f}")

# t-distribution
t_dist = stats.t(df=10)
print("\n=== t(df=10) ===")
print(f"PDF at x=0:     {t_dist.pdf(0):.6f}")
print(f"CDF at x=2.228: {t_dist.cdf(2.228):.6f}")
print(f"95th percentile:{t_dist.ppf(0.975):.6f}")

# Chi-squared
chi2 = stats.chi2(df=5)
print("\n=== Chi²(df=5) ===")
print(f"Mean: {chi2.mean()}, Var: {chi2.var()}")
print(f"95th percentile: {chi2.ppf(0.95):.4f}")

# Binomial (discrete)
binom = stats.binom(n=20, p=0.3)
print("\n=== Binomial(n=20, p=0.3) ===")
print(f"P(X=5):       {binom.pmf(5):.6f}")
print(f"P(X<=8):      {binom.cdf(8):.6f}")
print(f"Mean, Std:    {binom.mean():.2f}, {binom.std():.4f}")

# Poisson
poisson = stats.poisson(mu=4.5)
print("\n=== Poisson(λ=4.5) ===")
k = np.arange(0, 15)
pmf = poisson.pmf(k)
print("PMF:", {ki: round(v, 4) for ki, v in zip(k[:8], pmf[:8])})

# Random samples
rng = np.random.default_rng(42)
samples = stats.norm.rvs(loc=100, scale=15, size=1000, random_state=42)
print(f"\nNormal samples: mean={samples.mean():.2f}, std={samples.std():.2f}")
```
</details>

---

### E3 — Hypothesis Testing

**Question:**
Perform common hypothesis tests: one-sample t-test, two-sample t-test, paired t-test, chi-squared test, and Mann-Whitney U test. Interpret p-values correctly.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import stats
import numpy as np

np.random.seed(42)

# 1. One-sample t-test: Is mean ≠ 100?
sample = stats.norm.rvs(loc=102, scale=15, size=50, random_state=42)
t_stat, p_val = stats.ttest_1samp(sample, popmean=100)
print("=== One-sample t-test (H₀: μ=100) ===")
print(f"  Sample mean: {sample.mean():.4f}")
print(f"  t-stat: {t_stat:.4f}, p-value: {p_val:.4f}")
print(f"  Conclusion: {'Reject H₀' if p_val < 0.05 else 'Fail to reject H₀'}")

# 2. Independent two-sample t-test
group_a = stats.norm.rvs(loc=80, scale=10, size=40, random_state=1)
group_b = stats.norm.rvs(loc=85, scale=12, size=40, random_state=2)
t_stat, p_val = stats.ttest_ind(group_a, group_b, equal_var=False)  # Welch's
print("\n=== Two-sample t-test (Welch's) ===")
print(f"  Mean A: {group_a.mean():.2f}, Mean B: {group_b.mean():.2f}")
print(f"  t-stat: {t_stat:.4f}, p-value: {p_val:.4f}")
print(f"  Conclusion: {'Significant' if p_val < 0.05 else 'Not significant'}")

# 3. Paired t-test
before = stats.norm.rvs(loc=120, scale=10, size=30, random_state=3)
after  = before - stats.norm.rvs(loc=8, scale=5, size=30, random_state=4)
t_stat, p_val = stats.ttest_rel(before, after)
print("\n=== Paired t-test (before vs after) ===")
print(f"  Mean change: {(before-after).mean():.2f}")
print(f"  t-stat: {t_stat:.4f}, p-value: {p_val:.4f}")

# 4. Chi-squared test of independence
observed = np.array([[30, 20, 15], [25, 35, 40]])
chi2, p, dof, expected = stats.chi2_contingency(observed)
print("\n=== Chi-squared Test of Independence ===")
print(f"  χ² = {chi2:.4f}, p = {p:.4f}, dof = {dof}")
print(f"  Expected:\n{np.round(expected, 1)}")

# 5. Mann-Whitney U (non-parametric alternative to t-test)
u_stat, p_val = stats.mannwhitneyu(group_a, group_b, alternative="two-sided")
print("\n=== Mann-Whitney U Test ===")
print(f"  U-stat: {u_stat:.1f}, p-value: {p_val:.4f}")
```
</details>

---

### E4 — Normality Tests

**Question:**
Apply multiple normality tests (Shapiro-Wilk, D'Agostino-Pearson, Kolmogorov-Smirnov, Anderson-Darling) and understand when data departs from normality.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import stats
import numpy as np

np.random.seed(42)

datasets = {
    "Normal":      np.random.normal(0, 1, 200),
    "Skewed":      np.random.exponential(2, 200),
    "Bimodal":     np.concatenate([np.random.normal(-3,1,100),
                                   np.random.normal(3,1,100)]),
    "Uniform":     np.random.uniform(-3, 3, 200),
}

print(f"{'Dataset':12} | {'Shapiro p':>10} | {'D\'Agostino p':>13} | {'KS p':>10} | Normal?")
print("-" * 70)

for name, data in datasets.items():
    # Shapiro-Wilk (best for n < 50; works up to ~2000)
    _, p_sw = stats.shapiro(data)

    # D'Agostino-Pearson (combines skew + kurtosis tests)
    _, p_da = stats.normaltest(data)

    # Kolmogorov-Smirnov vs theoretical normal
    data_std = (data - data.mean()) / data.std()
    _, p_ks = stats.kstest(data_std, "norm")

    is_normal = "✓" if (p_sw > 0.05 and p_da > 0.05) else "✗"
    print(f"{name:12} | {p_sw:>10.4f} | {p_da:>13.4f} | {p_ks:>10.4f} | {is_normal}")

# Anderson-Darling (returns critical values at different significance levels)
print("\n=== Anderson-Darling (Normal data) ===")
ad_result = stats.anderson(datasets["Normal"], dist="norm")
print(f"  Statistic: {ad_result.statistic:.4f}")
for sig, crit in zip(ad_result.significance_level, ad_result.critical_values):
    result = "Reject" if ad_result.statistic > crit else "Accept"
    print(f"  {sig}%: critical={crit:.4f} → {result} H₀")
```
</details>

---

### E5 — Correlation and Association

**Question:**
Compute Pearson, Spearman, and Kendall correlations. Test for significance and create a full correlation analysis.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import stats
import numpy as np

np.random.seed(42)
n = 100

# Generate correlated data
x = np.random.randn(n)
y_linear   = 2*x + np.random.randn(n)*0.5        # strong linear
y_monotone = x**3 + np.random.randn(n)*2         # monotone non-linear
y_none     = np.random.randn(n)                   # no correlation

pairs = {
    "Linear (strong)":   (x, y_linear),
    "Monotone (non-lin)":(x, y_monotone),
    "No correlation":    (x, y_none),
}

print(f"{'Pair':22} | {'Pearson r':>10} | {'Spearman ρ':>11} | {'Kendall τ':>10}")
print("-" * 65)

for name, (a, b) in pairs.items():
    r_p,  p_p  = stats.pearsonr(a, b)
    r_sp, p_sp = stats.spearmanr(a, b)
    r_k,  p_k  = stats.kendalltau(a, b)
    print(f"{name:22} | {r_p:>8.4f} ({p_p:<5.3f}) | {r_sp:>9.4f} ({p_sp:<5.3f}) | {r_k:>9.4f}")

# Point biserial (continuous vs binary)
binary = (x > 0).astype(int)
r_pb, p_pb = stats.pointbiserialr(binary, y_linear)
print(f"\nPoint-biserial (binary vs continuous): r={r_pb:.4f}, p={p_pb:.4f}")
```
</details>

---

### E6 — ANOVA and Post-Hoc Tests

**Question:**
Perform one-way and two-way ANOVA to test differences between groups, followed by Tukey's HSD post-hoc test.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import stats
import numpy as np

np.random.seed(42)

# Three groups with different means
group_a = stats.norm.rvs(loc=70, scale=10, size=30, random_state=1)
group_b = stats.norm.rvs(loc=75, scale=10, size=30, random_state=2)
group_c = stats.norm.rvs(loc=85, scale=10, size=30, random_state=3)

# One-way ANOVA
f_stat, p_val = stats.f_oneway(group_a, group_b, group_c)
print("=== One-Way ANOVA ===")
print(f"Group A mean: {group_a.mean():.2f}")
print(f"Group B mean: {group_b.mean():.2f}")
print(f"Group C mean: {group_c.mean():.2f}")
print(f"F-statistic: {f_stat:.4f}")
print(f"p-value:     {p_val:.4f}")
print(f"Result: {'Significant differences exist' if p_val < 0.05 else 'No significant differences'}")

# Kruskal-Wallis (non-parametric alternative)
h_stat, p_kw = stats.kruskal(group_a, group_b, group_c)
print("\n=== Kruskal-Wallis (non-parametric) ===")
print(f"H-statistic: {h_stat:.4f}, p-value: {p_kw:.4f}")

# Levene's test for equal variances (assumption check)
lev_stat, p_lev = stats.levene(group_a, group_b, group_c)
print("\n=== Levene's Test (Equal Variances) ===")
print(f"W-statistic: {lev_stat:.4f}, p-value: {p_lev:.4f}")
print(f"Equal variances: {'Yes' if p_lev > 0.05 else 'No'}")

# Repeated measures / Friedman (non-parametric)
block = np.array([group_a[:10], group_b[:10], group_c[:10]])
f_friedman, p_friedman = stats.friedmanchisquare(*block)
print("\n=== Friedman Test ===")
print(f"Statistic: {f_friedman:.4f}, p-value: {p_friedman:.4f}")
```
</details>

---

## 🟠 Intermediate — Optimisation & Root Finding

---

### O1 — Scalar Minimisation

**Question:**
Find the minimum of a scalar function using `scipy.optimize.minimize_scalar`. Compare bounded vs unbounded methods.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import optimize
import numpy as np

# Function with multiple local minima
def f(x):
    return np.sin(x) + 0.1 * x**2 - 0.5*x

# Unbounded minimisation (Brent method)
result = optimize.minimize_scalar(f, method="brent")
print("=== Unbounded Minimisation (Brent) ===")
print(f"Minimum at x = {result.x:.6f}")
print(f"f(x) = {result.fun:.6f}")
print(f"Iterations: {result.nit}")

# Bounded minimisation (restricted to [0, 5])
result_bounded = optimize.minimize_scalar(f, bounds=(0, 5), method="bounded")
print("\n=== Bounded Minimisation [0, 5] ===")
print(f"Minimum at x = {result_bounded.x:.6f}")
print(f"f(x) = {result_bounded.fun:.6f}")

# Golden section search
result_golden = optimize.minimize_scalar(f, method="golden")
print("\n=== Golden Section Search ===")
print(f"Minimum at x = {result_golden.x:.6f}")
print(f"f(x) = {result_golden.fun:.6f}")

# Show multiple local minima exist
x_scan = np.linspace(-10, 10, 1000)
y_scan = f(x_scan)
local_min_approx = x_scan[np.argmin(y_scan)]
print(f"\nGlobal minimum scan: x ≈ {local_min_approx:.2f}, f ≈ {f(local_min_approx):.4f}")
```
</details>

---

### O2 — Multivariate Minimisation

**Question:**
Minimise a multivariate function using multiple methods: Nelder-Mead, BFGS, L-BFGS-B (with bounds), and COBYLA (with constraints). Compare convergence.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import optimize
import numpy as np

# Rosenbrock function (classic test: global min at (1,1))
def rosenbrock(x):
    return optimize.rosen(x)

def rosenbrock_grad(x):
    return optimize.rosen_der(x)

x0 = np.array([-1.0, 1.0])
methods = ["Nelder-Mead", "BFGS", "L-BFGS-B", "CG", "Powell"]

print(f"{'Method':15} | {'x*':>20} | {'f(x*)':>10} | {'Iters':>7} | {'Evals':>7}")
print("-" * 75)

for method in methods:
    kwargs = {}
    if method in ["BFGS", "CG"]:
        kwargs["jac"] = rosenbrock_grad
    if method == "L-BFGS-B":
        kwargs["bounds"] = [(-2, 2), (-2, 2)]

    result = optimize.minimize(rosenbrock, x0, method=method, **kwargs,
                               options={"maxiter": 10000})
    x_str = f"({result.x[0]:.4f}, {result.x[1]:.4f})"
    print(f"{method:15} | {x_str:>20} | {result.fun:>10.6f} | {result.nit:>7} | {result.nfev:>7}")

# Constrained optimisation — maximise profit subject to resource constraints
# Maximise: 5x + 4y
# Subject to: 6x + 4y <= 24, x + 2y <= 6, x >= 0, y >= 0
def neg_profit(xy):
    return -(5*xy[0] + 4*xy[1])

constraints = [
    {"type": "ineq", "fun": lambda xy: 24 - 6*xy[0] - 4*xy[1]},
    {"type": "ineq", "fun": lambda xy: 6  - xy[0]  - 2*xy[1]},
]
bounds = [(0, None), (0, None)]
result_con = optimize.minimize(neg_profit, [1,1], method="SLSQP",
                                bounds=bounds, constraints=constraints)
print(f"\nConstrained (SLSQP): x={result_con.x[0]:.4f}, y={result_con.x[1]:.4f}")
print(f"Max profit = {-result_con.fun:.4f}")
```
</details>

---

### O3 — Root Finding

**Question:**
Find roots of scalar and system equations using bisection, Brent, Newton-Raphson, and `fsolve` for systems.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import optimize
import numpy as np

# Scalar root finding
def f(x):
    return x**3 - 2*x - 5

def f_prime(x):
    return 3*x**2 - 2

print("=== Scalar Root Finding ===")
print(f"f(x) = x³ - 2x - 5")

# Bisection (guaranteed, slow)
result_bisect = optimize.bisect(f, 2, 3)
print(f"\nBisection:    x = {result_bisect:.8f}")

# Brent (hybrid, fast and robust)
result_brent = optimize.brentq(f, 2, 3)
print(f"Brent:        x = {result_brent:.8f}")

# Newton-Raphson (fast, needs derivative, may diverge)
result_newton = optimize.newton(f, x0=2.5, fprime=f_prime)
print(f"Newton:       x = {result_newton:.8f}")

# Secant method (Newton without derivative)
result_secant = optimize.newton(f, x0=2.5)
print(f"Secant:       x = {result_secant:.8f}")

print(f"\nVerify f({result_brent:.6f}) = {f(result_brent):.2e}")

# System of nonlinear equations
# x² + y² = 4
# x - y = 0.5
def system(vars):
    x, y = vars
    eq1 = x**2 + y**2 - 4
    eq2 = x - y - 0.5
    return [eq1, eq2]

print("\n=== System of Equations ===")
print("x² + y² = 4,  x - y = 0.5")
solution = optimize.fsolve(system, x0=[1.0, 1.0], full_output=True)
x, y = solution[0]
print(f"Solution: x = {x:.6f}, y = {y:.6f}")
print(f"Verify: x²+y² = {x**2+y**2:.6f}, x-y = {x-y:.6f}")

# All roots of a polynomial
coeffs = [1, 0, -2, -5]   # x³ - 2x - 5
roots = np.roots(coeffs)
print(f"\nPolynomial roots: {np.round(roots, 6)}")
```
</details>

---

### O4 — Curve Fitting

**Question:**
Fit custom functions to data using `scipy.optimize.curve_fit`. Compute confidence intervals from the covariance matrix.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import optimize
import numpy as np

np.random.seed(42)

# Generate noisy data from a known model
def true_model(x, A, B, C):
    return A * np.exp(-B * x) + C

x_data = np.linspace(0, 5, 50)
true_params = [3.0, 0.8, 0.5]
y_true = true_model(x_data, *true_params)
y_noisy = y_true + np.random.normal(0, 0.2, len(x_data))

# Fit with initial guess
p0 = [2.0, 1.0, 0.0]
popt, pcov = optimize.curve_fit(true_model, x_data, y_noisy, p0=p0)
perr = np.sqrt(np.diag(pcov))   # 1-sigma uncertainties

print("=== Exponential Decay Fit: A·exp(-Bx) + C ===")
print(f"\n{'Param':6} | {'True':>8} | {'Fitted':>8} | {'Std Err':>8} | {'95% CI'}")
print("-" * 60)
for name, true_p, fit_p, err in zip(["A","B","C"], true_params, popt, perr):
    ci = 1.96 * err
    print(f"{name:6} | {true_p:>8.4f} | {fit_p:>8.4f} | {err:>8.4f} | [{fit_p-ci:.4f}, {fit_p+ci:.4f}]")

y_pred = true_model(x_data, *popt)
ss_res = np.sum((y_noisy - y_pred)**2)
ss_tot = np.sum((y_noisy - y_noisy.mean())**2)
print(f"\nR² = {1 - ss_res/ss_tot:.6f}")
print(f"RMSE = {np.sqrt(ss_res/len(y_noisy)):.6f}")

# Fit a sinusoidal model
def sin_model(x, A, freq, phase, offset):
    return A * np.sin(2 * np.pi * freq * x + phase) + offset

x2 = np.linspace(0, 4, 200)
y2_true = sin_model(x2, 2.0, 0.8, np.pi/4, 1.0)
y2_noisy = y2_true + np.random.normal(0, 0.3, len(x2))

popt2, _ = optimize.curve_fit(sin_model, x2, y2_noisy,
                               p0=[1.0, 1.0, 0.0, 0.0], maxfev=5000)
print(f"\nSinusoidal fit: A={popt2[0]:.3f}, freq={popt2[1]:.3f}, phase={popt2[2]:.3f}")
```
</details>

---

### O5 — Global Optimisation

**Question:**
Apply global optimisation methods (differential evolution, basin-hopping, dual annealing) to problems with multiple local minima.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import optimize
import numpy as np

# Rastrigin function: many local minima, global min at (0,0,...,0)
def rastrigin(x):
    n = len(x)
    return 10*n + np.sum(x**2 - 10*np.cos(2*np.pi*x))

print("=== Rastrigin Function (global min = 0 at origin) ===")
bounds = [(-5.12, 5.12)] * 2

# Differential Evolution
result_de = optimize.differential_evolution(rastrigin, bounds, seed=42, maxiter=1000)
print(f"\nDifferential Evolution:")
print(f"  x* = {result_de.x.round(6)}")
print(f"  f* = {result_de.fun:.6f}")
print(f"  Iterations: {result_de.nit}")

# Dual Annealing (simulated annealing + local search)
result_da = optimize.dual_annealing(rastrigin, bounds, seed=42, maxiter=1000)
print(f"\nDual Annealing:")
print(f"  x* = {result_da.x.round(6)}")
print(f"  f* = {result_da.fun:.6f}")

# Basin-Hopping
minimizer_kwargs = {"method": "L-BFGS-B", "bounds": bounds}
result_bh = optimize.basinhopping(rastrigin, [2.0, -2.0], niter=200,
                                   minimizer_kwargs=minimizer_kwargs, seed=42)
print(f"\nBasin-Hopping:")
print(f"  x* = {result_bh.x.round(6)}")
print(f"  f* = {result_bh.fun:.6f}")

# Brute force grid search
rranges = (slice(-3, 3, 0.5), slice(-3, 3, 0.5))
result_bf = optimize.brute(rastrigin, rranges, full_output=True)
print(f"\nBrute Force:")
print(f"  x* = {result_bf[0].round(4)}")
print(f"  f* = {result_bf[1]:.4f}")
```
</details>

---

## 🔵 Upper Intermediate — Linear Algebra & Interpolation

---

### U1 — Decompositions: LU, QR, Cholesky

**Question:**
Compute LU, QR, and Cholesky decompositions using `scipy.linalg` and use them to solve linear systems efficiently.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import linalg
import numpy as np

A = np.array([[4, 3, 2, 1],
              [3, 4, 3, 2],
              [2, 3, 4, 3],
              [1, 2, 3, 4]], dtype=float)

b = np.array([10, 15, 20, 25], dtype=float)

print("Matrix A:\n", A)

# ── LU Decomposition ──────────────────────────────────────────────────────────
P, L, U = linalg.lu(A)
print("\n=== LU Decomposition ===")
print("L:\n", np.round(L, 4))
print("U:\n", np.round(U, 4))
print("P @ L @ U == A:", np.allclose(P @ L @ U, A))

# Solve using LU factors (efficient for multiple right-hand sides)
lu, piv = linalg.lu_factor(A)
x_lu = linalg.lu_solve((lu, piv), b)
print(f"Solution: {x_lu.round(6)}")
print(f"Verify A @ x: {(A @ x_lu).round(4)}")

# ── QR Decomposition ──────────────────────────────────────────────────────────
Q, R = linalg.qr(A)
print("\n=== QR Decomposition ===")
print("Q shape:", Q.shape, "| R shape:", R.shape)
print("Q^T @ Q ≈ I:", np.allclose(Q.T @ Q, np.eye(4)))
print("Q @ R == A:", np.allclose(Q @ R, A))

# ── Cholesky Decomposition (SPD matrix) ───────────────────────────────────────
L_chol = linalg.cholesky(A, lower=True)
print("\n=== Cholesky Decomposition ===")
print("L:\n", np.round(L_chol, 4))
print("L @ L^T == A:", np.allclose(L_chol @ L_chol.T, A))

# Solve using Cholesky (fastest for SPD)
x_chol = linalg.cho_solve(linalg.cho_factor(A), b)
print(f"Cholesky solution: {x_chol.round(6)}")
```
</details>

---

### U2 — Interpolation

**Question:**
Interpolate data using multiple methods: linear, cubic spline, Akima, and radial basis functions. Compare accuracy on known functions.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import interpolate
import numpy as np

# Sparse sample points from sin(x)
x_sparse = np.array([0, 1, 2, 3, 4, 5, 6])
y_sparse = np.sin(x_sparse)

# Dense evaluation points
x_dense = np.linspace(0, 6, 300)
y_true  = np.sin(x_dense)

# 1. Linear interpolation
f_linear = interpolate.interp1d(x_sparse, y_sparse, kind="linear")
y_linear = f_linear(x_dense)

# 2. Cubic interpolation
f_cubic = interpolate.interp1d(x_sparse, y_sparse, kind="cubic")
y_cubic = f_cubic(x_dense)

# 3. Cubic spline (more control)
cs = interpolate.CubicSpline(x_sparse, y_sparse)
y_spline = cs(x_dense)

# 4. Akima (avoids overshoot)
ak = interpolate.Akima1DInterpolator(x_sparse, y_sparse)
y_akima = ak(x_dense)

# 5. PCHIP (monotone preserving)
pchip = interpolate.PchipInterpolator(x_sparse, y_sparse)
y_pchip = pchip(x_dense)

print("=== Interpolation Accuracy (RMSE vs true sin) ===")
for name, y_pred in [("Linear", y_linear), ("Cubic interp", y_cubic),
                      ("CubicSpline", y_spline), ("Akima", y_akima),
                      ("PCHIP", y_pchip)]:
    rmse = np.sqrt(np.mean((y_true - y_pred)**2))
    print(f"  {name:15}: RMSE = {rmse:.6f}")

# 2D Interpolation
print("\n=== 2D Interpolation ===")
x2, y2 = np.mgrid[-2:2:10j, -2:2:10j]
z2 = np.sin(x2) * np.cos(y2)

f_2d = interpolate.RegularGridInterpolator(
    (x2[:, 0], y2[0, :]), z2, method="cubic"
)
test_pts = np.array([[0.5, 0.5], [-1.0, 1.0], [0.0, -1.5]])
z_interp = f_2d(test_pts)
z_exact  = np.sin(test_pts[:,0]) * np.cos(test_pts[:,1])

print(f"{'Point':>20} | {'Interpolated':>14} | {'Exact':>10} | {'Error':>10}")
for pt, zi, ze in zip(test_pts, z_interp, z_exact):
    print(f"  ({pt[0]:.1f}, {pt[1]:.1f}) {'':<10} | {zi:>14.6f} | {ze:>10.6f} | {abs(zi-ze):>10.2e}")
```
</details>

---

### U3 — Spatial Algorithms: KD-Tree and Convex Hull

**Question:**
Use `scipy.spatial` to build a KD-tree for fast nearest-neighbour queries, compute convex hulls, and perform Delaunay triangulation.

<details>
<summary>💡 View Solution</summary>

```python
from scipy.spatial import KDTree, ConvexHull, Delaunay
import numpy as np

np.random.seed(42)
points = np.random.rand(500, 2) * 100

# ── KD-Tree ───────────────────────────────────────────────────────────────────
tree = KDTree(points)
print("=== KD-Tree Nearest Neighbour ===")

query_point = np.array([[50.0, 50.0]])
dist, idx = tree.query(query_point, k=5)
print(f"5 nearest to (50,50):")
for d, i in zip(dist[0], idx[0]):
    print(f"  Point {i}: {points[i].round(2)}, dist={d:.4f}")

# All points within radius
radius = 10
nearby_idx = tree.query_ball_point(query_point[0], r=radius)
print(f"\nPoints within radius {radius}: {len(nearby_idx)}")

# ── Convex Hull ───────────────────────────────────────────────────────────────
hull = ConvexHull(points)
print("\n=== Convex Hull ===")
print(f"Hull vertices: {len(hull.vertices)}")
print(f"Hull area:     {hull.volume:.4f}")  # 'volume' is area in 2D
print(f"Hull perimeter:{hull.area:.4f}")    # 'area' is perimeter in 2D

# ── Delaunay Triangulation ────────────────────────────────────────────────────
small_pts = points[:20]
tri = Delaunay(small_pts)
print("\n=== Delaunay Triangulation ===")
print(f"Points: {len(small_pts)}")
print(f"Triangles: {len(tri.simplices)}")

# Find which triangle a point falls in
test_pt = np.array([50.0, 50.0])
tri_idx = tri.find_simplex(test_pt)
print(f"\nPoint {test_pt} is in triangle index: {tri_idx}")
if tri_idx >= 0:
    vertices = small_pts[tri.simplices[tri_idx]]
    print(f"Triangle vertices:\n{vertices.round(2)}")
```
</details>

---

### U4 — Sparse Linear System Solvers

**Question:**
Solve a large sparse linear system efficiently using `scipy.sparse.linalg` solvers (direct and iterative).

<details>
<summary>💡 View Solution</summary>

```python
from scipy.sparse import diags, eye, kron
from scipy.sparse.linalg import spsolve, cg, gmres, splu
import numpy as np
import time

# Build a sparse 2D Laplacian (finite difference Poisson equation)
n = 50   # grid points per dimension
N = n * n  # total unknowns

# 1D Laplacian operator
T = diags([-1, 2, -1], [-1, 0, 1], shape=(n, n))
I = eye(n)
# 2D Laplacian via Kronecker product
A = kron(I, T) + kron(T, I)
A = A.tocsr()  # CSR format for efficient arithmetic

# Right-hand side (source term)
b = np.ones(N)

print(f"Matrix size: {N}×{N}")
print(f"Non-zeros:   {A.nnz}")
print(f"Density:     {A.nnz/(N*N)*100:.4f}%")

# Direct sparse solve
t0 = time.time()
x_direct = spsolve(A, b)
print(f"\nDirect (spsolve):    {time.time()-t0:.4f}s | residual: {np.linalg.norm(b - A @ x_direct):.2e}")

# Iterative: Conjugate Gradient (for SPD matrices)
t0 = time.time()
x_cg, info_cg = cg(A, b, atol=1e-10)
print(f"Iterative (CG):      {time.time()-t0:.4f}s | residual: {np.linalg.norm(b - A @ x_cg):.2e} | info: {info_cg}")

# Iterative: GMRES (general)
t0 = time.time()
x_gm, info_gm = gmres(A, b, atol=1e-10)
print(f"Iterative (GMRES):   {time.time()-t0:.4f}s | residual: {np.linalg.norm(b - A @ x_gm):.2e} | info: {info_gm}")

# LU factorisation (reuse for multiple RHS)
t0 = time.time()
lu = splu(A)
x_lu = lu.solve(b)
x_lu2 = lu.solve(b * 2)  # solve again for free
print(f"LU factored solve:   {time.time()-t0:.4f}s | residual: {np.linalg.norm(b - A @ x_lu):.2e}")
```
</details>

---

## 🔴 Advanced — Signal Processing & ODE Solvers

---

### S1 — Digital Filters

**Question:**
Design and apply digital filters (Butterworth, Chebyshev, elliptic) using `scipy.signal`. Filter a noisy signal and compare filter responses.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import signal
import numpy as np

# Create a noisy composite signal
fs = 1000   # sample rate (Hz)
t  = np.linspace(0, 1, fs, endpoint=False)
clean_signal = (np.sin(2*np.pi*50*t) +       # 50 Hz (desired)
                0.5*np.sin(2*np.pi*120*t))    # 120 Hz (noise)
noisy = clean_signal + 0.3*np.random.randn(len(t))

print(f"Signal: 50Hz + 120Hz + noise, sampled at {fs}Hz")

# Design a low-pass Butterworth filter (cutoff=80Hz)
nyq = fs / 2
cutoff = 80 / nyq   # normalised cutoff

b_butter, a_butter = signal.butter(N=4, Wn=cutoff, btype="low")
filtered_butter = signal.filtfilt(b_butter, a_butter, noisy)  # zero-phase

# Chebyshev Type I (ripple in passband)
b_cheby, a_cheby = signal.cheby1(N=4, rp=0.5, Wn=cutoff, btype="low")
filtered_cheby = signal.filtfilt(b_cheby, a_cheby, noisy)

# Elliptic (sharpest rolloff, ripple in both bands)
b_ellip, a_ellip = signal.ellip(N=4, rp=0.5, rs=40, Wn=cutoff, btype="low")
filtered_ellip = signal.filtfilt(b_ellip, a_ellip, noisy)

print("\n=== Filter Performance (RMSE vs clean signal) ===")
for name, filtered in [("Unfiltered",  noisy),
                        ("Butterworth", filtered_butter),
                        ("Chebyshev",  filtered_cheby),
                        ("Elliptic",   filtered_ellip)]:
    rmse = np.sqrt(np.mean((clean_signal - filtered)**2))
    print(f"  {name:12}: RMSE = {rmse:.6f}")

# Frequency response
w, h = signal.freqz(b_butter, a_butter, worN=8000)
frequencies = w * fs / (2*np.pi)
magnitude_db = 20 * np.log10(np.abs(h) + 1e-10)
print(f"\nButterworth at 50Hz: {magnitude_db[np.argmin(np.abs(frequencies-50))]:.2f} dB")
print(f"Butterworth at 120Hz:{magnitude_db[np.argmin(np.abs(frequencies-120))]:.2f} dB")

# Band-pass filter
b_bp, a_bp = signal.butter(N=3, Wn=[40/nyq, 60/nyq], btype="band")
filtered_bp = signal.filtfilt(b_bp, a_bp, noisy)
print(f"\nBand-pass (40-60Hz) RMSE vs 50Hz component: "
      f"{np.sqrt(np.mean((np.sin(2*np.pi*50*t) - filtered_bp)**2)):.6f}")
```
</details>

---

### S2 — Spectral Analysis

**Question:**
Compute power spectral density using Welch's method, spectrogram for time-frequency analysis, and detect periodic components.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import signal
import numpy as np

fs = 2000
t  = np.linspace(0, 2, 2*fs, endpoint=False)

# Chirp signal (frequency increases over time)
chirp = signal.chirp(t, f0=10, f1=500, t1=2, method="linear")
noisy_chirp = chirp + 0.5 * np.random.randn(len(t))

# Stationary signal for PSD demo
test_signal = (np.sin(2*np.pi*100*t) +
               0.5*np.sin(2*np.pi*200*t) +
               0.2*np.random.randn(len(t)))

# Welch's PSD
freqs, psd = signal.welch(test_signal, fs=fs, nperseg=512)
top_freqs = freqs[np.argsort(psd)[-5:][::-1]]
print("=== Welch's PSD — Top 5 frequencies ===")
for f, p in zip(top_freqs, psd[np.argsort(psd)[-5:][::-1]]):
    print(f"  {f:7.2f} Hz | PSD: {p:.4f}")

# Periodogram
freqs_per, psd_per = signal.periodogram(test_signal, fs=fs)
print("\nPeriodogram peak:", freqs_per[np.argmax(psd_per)], "Hz")

# Spectrogram of chirp (time-frequency)
f_spec, t_spec, Sxx = signal.spectrogram(noisy_chirp, fs=fs, nperseg=256)
print("\n=== Spectrogram of Chirp ===")
print(f"Shape: frequencies={len(f_spec)}, time_bins={len(t_spec)}")
print(f"Frequency range: {f_spec[0]:.1f} - {f_spec[-1]:.1f} Hz")
print(f"Time range:      {t_spec[0]:.3f} - {t_spec[-1]:.3f} s")

# Find peak frequency at each time step
peak_freqs = f_spec[np.argmax(Sxx, axis=0)]
print(f"\nPeak freq at t=0s:   {peak_freqs[0]:.1f} Hz (expected ~10)")
print(f"Peak freq at t=1s:   {peak_freqs[len(t_spec)//2]:.1f} Hz (expected ~255)")
print(f"Peak freq at t=2s:   {peak_freqs[-1]:.1f} Hz (expected ~500)")
```
</details>

---

### S3 — Solve ODEs with solve_ivp

**Question:**
Solve ordinary differential equations using `scipy.integrate.solve_ivp`. Model the Lotka-Volterra predator-prey system and the damped harmonic oscillator.

<details>
<summary>💡 View Solution</summary>

```python
from scipy.integrate import solve_ivp
import numpy as np

# ── 1. Damped Harmonic Oscillator ─────────────────────────────────────────────
# ẍ + 2ζω₀ẋ + ω₀²x = 0
# Rewrite as system: y₁ = x, y₂ = ẋ
# ẏ₁ = y₂
# ẏ₂ = -2ζω₀y₂ - ω₀²y₁

omega0 = 2.0   # natural frequency
zeta   = 0.2   # damping ratio (underdamped if < 1)

def oscillator(t, y):
    x, v = y
    return [v, -2*zeta*omega0*v - omega0**2*x]

y0  = [1.0, 0.0]   # initial displacement=1, velocity=0
t_span = (0, 20)
t_eval = np.linspace(0, 20, 1000)

sol = solve_ivp(oscillator, t_span, y0, t_eval=t_eval, method="RK45", rtol=1e-8)
print("=== Damped Harmonic Oscillator ===")
print(f"Status: {sol.message}")
print(f"Steps:  {len(sol.t)}")
print(f"x(0)  = {sol.y[0, 0]:.4f}  (expected 1.0)")
print(f"x(20) ≈ {sol.y[0,-1]:.4f}  (should be near 0)")

# ── 2. Lotka-Volterra (Predator-Prey) ─────────────────────────────────────────
# ẋ = αx - βxy   (prey)
# ẏ = δxy - γy   (predator)
alpha, beta, delta, gamma = 1.0, 0.1, 0.075, 1.5

def lotka_volterra(t, y):
    x, y_pred = y
    return [alpha*x - beta*x*y_pred,
            delta*x*y_pred - gamma*y_pred]

y0_lv   = [10.0, 5.0]    # 10 prey, 5 predators
sol_lv  = solve_ivp(lotka_volterra, (0, 50), y0_lv,
                    t_eval=np.linspace(0,50,2000), method="RK45", rtol=1e-10)

prey_max_t = sol_lv.t[np.argmax(sol_lv.y[0])]
pred_max_t = sol_lv.t[np.argmax(sol_lv.y[1])]
print("\n=== Lotka-Volterra ===")
print(f"Prey peak at t   = {prey_max_t:.2f}")
print(f"Predator peak at = {pred_max_t:.2f}")
print(f"Phase lag (pred follows prey): {pred_max_t - prey_max_t:.2f}")

# ── 3. Stiff ODE (Van der Pol) ────────────────────────────────────────────────
mu = 1000  # large mu → stiff

def vanderpol(t, y):
    return [y[1], mu*(1 - y[0]**2)*y[1] - y[0]]

sol_stiff = solve_ivp(vanderpol, (0, 3000), [2.0, 0.0],
                      method="Radau",   # Radau/BDF for stiff problems
                      rtol=1e-6, atol=1e-8)
print("\n=== Van der Pol (stiff, μ=1000) ===")
print(f"Method: Radau | Status: {sol_stiff.message}")
print(f"Steps taken: {len(sol_stiff.t)}")
```
</details>

---

### S4 — Numerical Integration

**Question:**
Compute definite integrals using `scipy.integrate.quad`, `dblquad`, and `tplquad`. Handle improper integrals and compare with analytical results.

<details>
<summary>💡 View Solution</summary>

```python
from scipy.integrate import quad, dblquad, tplquad, simpson, trapezoid
import numpy as np

print("=== scipy.integrate.quad ===")

# Simple definite integral: ∫₀^π sin(x)dx = 2
result, error = quad(np.sin, 0, np.pi)
print(f"∫₀^π sin(x)dx = {result:.10f}  (exact=2, error={error:.2e})")

# Gaussian: ∫_{-∞}^{∞} e^(-x²)dx = √π
result_inf, err_inf = quad(lambda x: np.exp(-x**2), -np.inf, np.inf)
print(f"∫_(-∞)^(∞) e^(-x²)dx = {result_inf:.10f}  (exact={np.sqrt(np.pi):.10f})")

# Improper integral with singularity: ∫₀¹ 1/√x dx = 2
result_sing, err_sing = quad(lambda x: 1/np.sqrt(x), 0, 1, limit=100)
print(f"∫₀¹ 1/√x dx = {result_sing:.10f}  (exact=2)")

# Integral with extra arguments
def f_param(x, a, b):
    return a * np.exp(-b * x**2)

result_param, _ = quad(f_param, 0, np.inf, args=(2.0, 1.0))
print(f"∫₀^∞ 2e^(-x²)dx = {result_param:.10f}  (exact={np.sqrt(np.pi):.10f})")

print("\n=== Double Integral ===")
# ∫₀¹ ∫₀¹ x*y dxdy = 0.25
result_2d, _ = dblquad(lambda y, x: x*y, 0, 1, 0, 1)
print(f"∫₀¹∫₀¹ xy dxdy = {result_2d:.10f}  (exact=0.25)")

# Volume of sphere: ∫∫∫ 1 dV where x²+y²+z² ≤ 1
result_3d, _ = tplquad(
    lambda z, y, x: 1,
    -1, 1,
    lambda x: -np.sqrt(1-x**2),
    lambda x:  np.sqrt(1-x**2),
    lambda x, y: -np.sqrt(1-x**2-y**2),
    lambda x, y:  np.sqrt(1-x**2-y**2),
)
print(f"\nVolume of unit sphere = {result_3d:.8f}  (exact={4/3*np.pi:.8f})")

print("\n=== Numerical Quadrature on Data ===")
x_data = np.linspace(0, np.pi, 100)
y_data = np.sin(x_data)
print(f"Simpson's rule: {simpson(y_data, x=x_data):.10f}")
print(f"Trapezoid rule: {trapezoid(y_data, x=x_data):.10f}")
print(f"Exact:          {2.0:.10f}")
```
</details>

---

## ⚫ Expert — Sparse Matrices, Integration & Pipelines

---

### X1 — Sparse Eigenvalue Problems

**Question:**
Solve large sparse eigenvalue problems using `scipy.sparse.linalg.eigs` and `eigsh`. Apply to the graph Laplacian for spectral clustering.

<details>
<summary>💡 View Solution</summary>

```python
from scipy.sparse import csr_matrix, diags
from scipy.sparse.linalg import eigsh, eigs
import numpy as np

# Build the graph Laplacian for a simple graph
# Graph with 3 clear clusters
n = 30   # 3 clusters of 10 nodes each

# Adjacency matrix: dense within clusters, sparse between
A = np.zeros((n, n))
for cluster in range(3):
    idx = range(cluster*10, (cluster+1)*10)
    for i in idx:
        for j in idx:
            if i != j:
                A[i, j] = 1.0

# Add a few inter-cluster edges
A[9, 10] = A[10, 9] = 1.0
A[19, 20] = A[20, 19] = 1.0

# Compute Laplacian: L = D - A
degree = A.sum(axis=1)
D = diags(degree)
L = csr_matrix(D - A)

print(f"Graph Laplacian: {L.shape}, nnz={L.nnz}")

# Compute k smallest eigenvalues (eigsh for symmetric matrices)
k = 6
eigenvalues, eigenvectors = eigsh(L, k=k, which="SM")  # Smallest Magnitude

print("\nSmallest eigenvalues (spectral gap reveals clusters):")
for i, ev in enumerate(eigenvalues):
    print(f"  λ{i+1} = {ev:.6f}")

# The gap between eigenvalues shows cluster count
gaps = np.diff(eigenvalues)
print("\nEigenvalue gaps:", np.round(gaps, 6))
print(f"Largest gap at position {np.argmax(gaps)+1} → suggests {np.argmax(gaps)+1} clusters")

# Spectral clustering assignment (using k=3 eigenvectors)
V = eigenvectors[:, :3]  # shape (n, 3)
from scipy.cluster.vq import kmeans, vq
centroids, _ = kmeans(V, 3)
labels, _ = vq(V, centroids)
print("\nSpectral cluster labels:", labels)
print("Expected: 3 equal groups of 10")
for c in range(3):
    print(f"  Cluster {c}: nodes {list(np.where(labels==c)[0])}")
```
</details>

---

### X2 — Bayesian Parameter Estimation

**Question:**
Use `scipy.optimize` and `scipy.stats` to perform maximum likelihood estimation (MLE) and compare with moment estimation.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import stats, optimize
import numpy as np

np.random.seed(42)

# Generate data from a Gamma distribution
true_alpha, true_beta = 3.0, 2.0
data = stats.gamma.rvs(a=true_alpha, scale=1/true_beta, size=500, random_state=42)

print("=== Maximum Likelihood Estimation: Gamma Distribution ===")
print(f"True parameters: α={true_alpha}, β={true_beta}")

# ── Method 1: scipy.stats.fit (built-in MLE) ──────────────────────────────────
fit_alpha, fit_loc, fit_scale = stats.gamma.fit(data, floc=0)
print(f"\nBuilt-in MLE:  α={fit_alpha:.4f}, β={1/fit_scale:.4f}")

# ── Method 2: Manual MLE via optimization ─────────────────────────────────────
def neg_log_likelihood(params):
    alpha, beta = params
    if alpha <= 0 or beta <= 0:
        return np.inf
    return -np.sum(stats.gamma.logpdf(data, a=alpha, scale=1/beta))

result = optimize.minimize(neg_log_likelihood, x0=[2.0, 1.5],
                           method="Nelder-Mead",
                           options={"xatol": 1e-8, "fatol": 1e-8})
print(f"Manual MLE:    α={result.x[0]:.4f}, β={result.x[1]:.4f}")

# ── Method 3: Method of Moments ───────────────────────────────────────────────
mean, var = np.mean(data), np.var(data)
alpha_mom = mean**2 / var
beta_mom  = mean / var
print(f"Method of Moments: α={alpha_mom:.4f}, β={beta_mom:.4f}")

# ── Goodness of fit ───────────────────────────────────────────────────────────
print("\n=== Goodness of Fit Tests ===")
ks_stat, ks_p = stats.kstest(data, "gamma",
                              args=(fit_alpha, 0, fit_scale))
print(f"KS test: stat={ks_stat:.4f}, p={ks_p:.4f}")

ad_stat = stats.anderson(data, dist="expon")
print(f"Anderson-Darling statistic: {ad_stat.statistic:.4f}")

# ── Confidence Intervals via Bootstrap ────────────────────────────────────────
n_boot = 1000
boot_alphas = []
rng = np.random.default_rng(42)
for _ in range(n_boot):
    sample = rng.choice(data, size=len(data), replace=True)
    a, _, s = stats.gamma.fit(sample, floc=0)
    boot_alphas.append(a)

ci_lo, ci_hi = np.percentile(boot_alphas, [2.5, 97.5])
print(f"\nBootstrap 95% CI for α: [{ci_lo:.4f}, {ci_hi:.4f}]")
print(f"True α={true_alpha} is inside CI: {ci_lo <= true_alpha <= ci_hi}")
```
</details>

---

### X3 — Image Processing with scipy.ndimage

**Question:**
Apply image processing operations: Gaussian blur, edge detection, morphological operations, and connected component labelling.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import ndimage
import numpy as np

# Create a synthetic binary image with shapes
img = np.zeros((100, 100), dtype=float)
# Add circles (blobs)
for cx, cy, r in [(25,25,15), (70,30,10), (30,75,20), (75,75,8)]:
    y, x = np.ogrid[:100, :100]
    mask = (x-cx)**2 + (y-cy)**2 <= r**2
    img[mask] = 1.0

# Add some noise
np.random.seed(42)
noisy_img = img + 0.2 * np.random.randn(100, 100)

print("=== scipy.ndimage Operations ===")
print(f"Image shape: {img.shape}, dtype: {img.dtype}")
print(f"Pixel range: [{noisy_img.min():.3f}, {noisy_img.max():.3f}]")

# ── Smoothing ─────────────────────────────────────────────────────────────────
smoothed = ndimage.gaussian_filter(noisy_img, sigma=2.0)
print(f"\nGaussian blur (σ=2): std reduced from {noisy_img.std():.4f} to {smoothed.std():.4f}")

# Median filter (preserves edges better)
median_filtered = ndimage.median_filter(noisy_img, size=5)
print(f"Median filter: std = {median_filtered.std():.4f}")

# ── Edge Detection ────────────────────────────────────────────────────────────
edges_x = ndimage.sobel(smoothed, axis=0)
edges_y = ndimage.sobel(smoothed, axis=1)
edges   = np.hypot(edges_x, edges_y)
print(f"\nSobel edges: max={edges.max():.4f}, mean={edges.mean():.4f}")

laplacian = ndimage.laplace(smoothed)
print(f"Laplacian: max={abs(laplacian).max():.4f}")

# ── Morphological Operations ──────────────────────────────────────────────────
binary = img > 0.5

# Erosion and dilation
eroded  = ndimage.binary_erosion(binary, iterations=3)
dilated = ndimage.binary_dilation(binary, iterations=3)
opened  = ndimage.binary_opening(binary, iterations=2)
closed  = ndimage.binary_closing(binary, iterations=2)

print(f"\nBinary ops (filled pixels):")
print(f"  Original: {binary.sum()}")
print(f"  Eroded:   {eroded.sum()}")
print(f"  Dilated:  {dilated.sum()}")

# ── Connected Components ──────────────────────────────────────────────────────
labelled, n_features = ndimage.label(binary)
print(f"\nConnected components: {n_features}")
for i in range(1, n_features+1):
    size   = (labelled == i).sum()
    cy, cx = ndimage.center_of_mass(binary, labelled, i)
    print(f"  Region {i}: size={size:4d} px, centroid=({cx:.1f}, {cy:.1f})")
```
</details>

---

### X4 — Full Scientific Pipeline: Seismic Signal Analysis

**Question:**
Build a complete seismic signal processing pipeline: generate synthetic seismic data, denoise it, detect events, extract features, and classify events.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import signal, stats, integrate
from scipy.signal import find_peaks
import numpy as np

np.random.seed(42)

# ── STEP 1: Synthetic Seismic Data Generation ─────────────────────────────────
fs = 100   # 100 Hz sampling
duration = 60  # 60 seconds
t = np.linspace(0, duration, int(fs * duration), endpoint=False)

def seismic_event(t, t0, freq, amplitude, decay):
    """Damped sinusoidal pulse starting at t0."""
    mask = t >= t0
    envelope = np.where(mask, amplitude * np.exp(-decay*(t-t0)), 0)
    return envelope * np.sin(2*np.pi*freq*(t-t0)) * mask

# Background noise + 3 events
background = 0.05 * np.random.randn(len(t))
event1 = seismic_event(t, t0=5,  freq=2.0, amplitude=1.0, decay=0.5)
event2 = seismic_event(t, t0=22, freq=4.0, amplitude=2.5, decay=0.3)
event3 = seismic_event(t, t0=45, freq=1.5, amplitude=1.8, decay=0.7)
seismic = background + event1 + event2 + event3

print("=== Seismic Signal Processing Pipeline ===")
print(f"Signal: {duration}s @ {fs}Hz = {len(t)} samples")
print(f"Signal SNR (raw): {10*np.log10((event1+event2+event3).var()/background.var()):.1f} dB")

# ── STEP 2: Bandpass Filtering ─────────────────────────────────────────────────
nyq = fs / 2
low, high = 0.5/nyq, 10.0/nyq
b, a = signal.butter(N=4, Wn=[low, high], btype="band")
filtered = signal.filtfilt(b, a, seismic)
print(f"\nBandpass filter (0.5–10 Hz) applied")

# ── STEP 3: Event Detection via STA/LTA ───────────────────────────────────────
def sta_lta(data, fs, sta_win=1.0, lta_win=10.0):
    """Short-term / Long-term average ratio."""
    sta_len = int(sta_win * fs)
    lta_len = int(lta_win * fs)
    energy = data**2
    sta = np.convolve(energy, np.ones(sta_len)/sta_len, mode="same")
    lta = np.convolve(energy, np.ones(lta_len)/lta_len, mode="same")
    with np.errstate(divide="ignore", invalid="ignore"):
        ratio = np.where(lta > 0, sta/lta, 0)
    return ratio

ratio = sta_lta(filtered, fs)
threshold = 5.0
peaks, properties = find_peaks(ratio, height=threshold, distance=fs*5)
print(f"\nSTA/LTA detection (threshold={threshold}):")
print(f"  Detected events: {len(peaks)}")
for i, pk in enumerate(peaks):
    t_event = t[pk]
    print(f"  Event {i+1}: t={t_event:.2f}s, STA/LTA={ratio[pk]:.2f}")

# ── STEP 4: Feature Extraction ────────────────────────────────────────────────
def extract_features(segment, fs):
    n = len(segment)
    # Time domain
    rms    = np.sqrt(np.mean(segment**2))
    peak_a = np.max(np.abs(segment))
    crest  = peak_a / (rms + 1e-10)
    # Frequency domain
    freqs, psd = signal.welch(segment, fs=fs, nperseg=min(n//4, 64))
    centroid = np.sum(freqs * psd) / (np.sum(psd) + 1e-10)
    # Zero-crossing rate
    zcr    = np.sum(np.diff(np.sign(segment)) != 0) / n
    # Duration (above 10% of peak)
    active = np.sum(np.abs(segment) > 0.1*peak_a) / fs
    return {"rms": rms, "peak": peak_a, "crest_factor": crest,
            "freq_centroid": centroid, "zcr": zcr, "active_duration": active}

window_sec = 5
half_win   = int(window_sec/2 * fs)

print("\n=== Extracted Features ===")
print(f"{'Feature':18}", end="")
for i, pk in enumerate(peaks):
    print(f"  Event {i+1:>6}", end="")
print()

features_all = []
for pk in peaks:
    start = max(0, pk - half_win)
    end   = min(len(filtered), pk + half_win)
    seg   = filtered[start:end]
    feats = extract_features(seg, fs)
    features_all.append(feats)

for feat_name in list(features_all[0].keys()):
    print(f"{feat_name:18}", end="")
    for f in features_all:
        print(f"  {f[feat_name]:>10.4f}", end="")
    print()

# ── STEP 5: Quality Report ────────────────────────────────────────────────────
print("\n=== Pipeline Summary ===")
print(f"  Input samples:     {len(t):,}")
print(f"  Sampling rate:     {fs} Hz")
print(f"  Filter band:       0.5 – 10 Hz")
print(f"  Events detected:   {len(peaks)}")
print(f"  True events:       3  (at t≈5s, 22s, 45s)")
recall = min(len(peaks), 3) / 3
print(f"  Recall:            {recall:.0%}")
```
</details>

---

### X5 — Monte Carlo Integration and Uncertainty Propagation

**Question:**
Implement Monte Carlo integration and uncertainty propagation using `scipy.stats`. Compute confidence intervals via bootstrapping.

<details>
<summary>💡 View Solution</summary>

```python
from scipy import stats, optimize
import numpy as np

rng = np.random.default_rng(42)

# ── 1. Monte Carlo Integration ────────────────────────────────────────────────
print("=== Monte Carlo Integration ===")

# Estimate ∫₀¹ ∫₀¹ exp(x*y) dxdy
# Exact: (e-2) ≈ 0.71828...
exact = np.e - 2

ns = [1_000, 10_000, 100_000, 1_000_000]
print(f"Exact value: {exact:.8f}")
print(f"\n{'N':>10} | {'Estimate':>12} | {'Error':>10} | {'Std Err':>10}")
print("-" * 50)

for n in ns:
    x = rng.uniform(0, 1, n)
    y = rng.uniform(0, 1, n)
    f_vals = np.exp(x * y)
    estimate = f_vals.mean()
    std_err  = f_vals.std() / np.sqrt(n)
    print(f"{n:>10,} | {estimate:>12.8f} | {abs(estimate-exact):>10.2e} | {std_err:>10.2e}")

# ── 2. Importance Sampling ─────────────────────────────────────────────────────
print("\n=== Importance Sampling for Tail Probability ===")
# Estimate P(X > 4) where X ~ N(0,1)
# Exact: 1 - Φ(4) ≈ 3.17e-5
exact_tail = 1 - stats.norm.cdf(4)
print(f"Exact P(X>4): {exact_tail:.2e}")

n_samples = 100_000

# Naive MC (needs huge n to see events in tail)
x_naive = rng.standard_normal(n_samples)
naive_est = (x_naive > 4).mean()
print(f"Naive MC (n={n_samples:,}): {naive_est:.2e}")

# Importance sampling with shifted distribution N(4, 1)
x_is = rng.normal(loc=4, scale=1, size=n_samples)
# Likelihood ratio
w = stats.norm.pdf(x_is, 0, 1) / stats.norm.pdf(x_is, 4, 1)
is_est = (w * (x_is > 4)).mean()
is_std = (w * (x_is > 4)).std() / np.sqrt(n_samples)
print(f"Importance sampling:         {is_est:.2e} ± {is_std:.2e}")

# ── 3. Uncertainty Propagation ────────────────────────────────────────────────
print("\n=== Uncertainty Propagation ===")
# Physical formula: F = ma, where m ~ N(5, 0.1) kg, a ~ N(9.8, 0.05) m/s²
n_mc = 100_000
m = rng.normal(5.0, 0.1, n_mc)    # mass with uncertainty
a = rng.normal(9.8, 0.05, n_mc)   # acceleration with uncertainty
F = m * a                           # force

print(f"m: {m.mean():.4f} ± {m.std():.4f} kg")
print(f"a: {a.mean():.4f} ± {a.std():.4f} m/s²")
print(f"F: {F.mean():.4f} ± {F.std():.4f} N")

# Analytical (linear propagation): σ_F = √((σ_m·a)² + (σ_a·m)²)
sigma_F_analytical = np.sqrt((0.1*9.8)**2 + (0.05*5.0)**2)
print(f"Analytical σ_F: {sigma_F_analytical:.4f} N")

# Bootstrap confidence interval
n_boot = 2000
sample_data = F[:1000]  # pretend this is observed data
boot_means  = [rng.choice(sample_data, size=1000, replace=True).mean()
               for _ in range(n_boot)]
ci_lo, ci_hi = np.percentile(boot_means, [2.5, 97.5])
print(f"\n95% Bootstrap CI for mean F: [{ci_lo:.4f}, {ci_hi:.4f}]")
print(f"scipy.stats.bootstrap:")
boot_result = stats.bootstrap((sample_data,), np.mean, n_resamples=2000,
                               confidence_level=0.95, random_state=42)
print(f"  CI: [{boot_result.confidence_interval.low:.4f}, {boot_result.confidence_interval.high:.4f}]")
```
</details>

---

## 📝 Quick Reference Cheat Sheet

### Module Map

| Task | Module |
|------|--------|
| Physical constants | `scipy.constants` |
| Special functions | `scipy.special` |
| Linear algebra | `scipy.linalg` |
| Optimisation | `scipy.optimize` |
| Interpolation | `scipy.interpolate` |
| Statistics | `scipy.stats` |
| Signal processing | `scipy.signal` |
| Spatial algorithms | `scipy.spatial` |
| ODE solving | `scipy.integrate.solve_ivp` |
| Numerical integration | `scipy.integrate.quad` |
| Sparse matrices | `scipy.sparse` |
| Image processing | `scipy.ndimage` |

### Key Functions

```python
# Optimisation
optimize.minimize(f, x0, method="BFGS")
optimize.minimize_scalar(f, bounds=(a,b), method="bounded")
optimize.curve_fit(model, x, y, p0=...)
optimize.fsolve(system, x0)
optimize.differential_evolution(f, bounds)

# Statistics
stats.norm(loc=0, scale=1).pdf(x)
stats.norm.fit(data)
stats.ttest_ind(a, b)
stats.chi2_contingency(table)
stats.pearsonr(x, y)

# Interpolation
interpolate.CubicSpline(x, y)
interpolate.interp1d(x, y, kind="cubic")
interpolate.RegularGridInterpolator((xi, yi), z)

# Signal Processing
signal.butter(N, Wn, btype="low")
signal.filtfilt(b, a, data)
signal.welch(data, fs=fs)
signal.spectrogram(data, fs=fs)
signal.find_peaks(data, height=..., distance=...)

# Integration
integrate.quad(f, a, b)
integrate.dblquad(f, a, b, g, h)
integrate.solve_ivp(f, t_span, y0, method="RK45")

# Sparse
sparse.csr_matrix(data)
sparse.linalg.spsolve(A, b)
sparse.linalg.eigsh(A, k=6, which="SM")
```

### Choosing an ODE Solver

| Method | Use case |
|--------|----------|
| `RK45` | Default, non-stiff problems |
| `RK23` | Low accuracy, fast |
| `DOP853` | High accuracy, non-stiff |
| `Radau` | Stiff problems |
| `BDF` | Very stiff (large μ) |
| `LSODA` | Automatically switches |

---

## 🔧 Setup

```bash
pip install scipy numpy
```

```python
import numpy as np
from scipy import stats, optimize, linalg, signal
from scipy import integrate, interpolate, spatial, ndimage
from scipy import sparse, special, constants
print("SciPy version:", __import__("scipy").__version__)
```

---

*Happy computing! 🔬*
