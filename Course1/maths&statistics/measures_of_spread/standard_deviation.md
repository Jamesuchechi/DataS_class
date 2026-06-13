# Standard Deviation

Standard deviation is a foundational concept in statistics and data science. It quantifies the amount of variation or dispersion in a dataset. A low standard deviation means data points are close to the mean, while a high standard deviation means they are spread out over a wider range.

---

## 1. Core concept and intuition

Standard deviation is the square root of variance. Variance measures the average squared deviation from the mean. Taking the square root returns the measure to the original data units, which makes interpretation easier.

### Intuition

- City A: heights tightly clustered around 170 cm → low standard deviation.
- City B: heights ranging from 140 cm to 200 cm → high standard deviation.

Standard deviation tells you how typical a deviation from the average is.

### Why it matters in data science

- Exploratory data analysis (EDA): measures spread.
- Risk and uncertainty: volatility in finance, manufacturing tolerance.
- Feature scaling: standardization uses standard deviation.
- Outlier detection: values beyond mean ± 2 or 3 standard deviations are often flagged.
- Confidence intervals and hypothesis testing: standard deviation is central to standard error.
- Regression diagnostics: residual standard deviation indicates model fit.

---

## 2. Mathematical definition

### Population standard deviation

For an entire population:

```math
\sigma = \sqrt{\dfrac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2}
```

Where:

- \(\sigma\): population standard deviation
- \(N\): population size
- \(x_i\): each data value
- \(\mu\): population mean

### Sample standard deviation

For a sample used to estimate a population:

```math
s = \sqrt{\dfrac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}
```

Where:

- \(s\): sample standard deviation
- \(n\): sample size
- \(x_i\): each sample value
- \(\bar{x}\): sample mean

The denominator \(n - 1\) is Bessel's correction. It gives an unbiased estimate of the population variance when using a sample.

### Key nuance

- Use the population formula when you have the complete dataset of interest.
- Use the sample formula when you are inferring about a larger population from a subset.
- In many libraries, this is controlled by `ddof=0` for population and `ddof=1` for sample.

---

## 3. Step-by-step example

Dataset:

```text
[85, 90, 78, 92, 88, 76, 95, 89]
```

### Step 1: Calculate the sample mean

```math
\bar{x} = \dfrac{85 + 90 + 78 + 92 + 88 + 76 + 95 + 89}{8} = 86.625
```

### Step 2: Compute squared deviations

For each value, calculate \((x_i - \bar{x})^2\), then sum the results.

### Step 3: Compute sample variance and standard deviation

```math
s^2 = \dfrac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2
```

```math
s = \sqrt{s^2}
```

For this dataset:

- Sum of squared deviations ≈ 284.875
- Sample variance \(s^2 \approx \dfrac{284.875}{7} \approx 40.696\)
- Sample standard deviation \(s \approx \sqrt{40.696} \approx 6.38\)

### Interpretation

Scores typically deviate from the mean by about 6.4 points.

### Edge case

Dataset with an outlier:

```text
[85, 86, 87, 88, 200]
```

The mean increases, and the standard deviation increases dramatically because the squared deviation from the outlier has a large effect.

---

## 4. Properties of standard deviation

- Always non-negative.
- Has the same units as the original data.
- Sensitive to outliers because deviations are squared.
- For a normal distribution:
  - ≈ 68% of data fall within ±1σ
  - ≈ 95% within ±2σ
  - ≈ 99.7% within ±3σ
- Not robust for skewed or multimodal distributions.
- Variances of independent variables add: \(\mathrm{Var}(X + Y) = \mathrm{Var}(X) + \mathrm{Var}(Y)\).

### Note on skewed data

For skewed distributions, median and interquartile range (IQR) or median absolute deviation (MAD) may be better spread measures than standard deviation.

---

## 5. Visual interpretation

- Histogram / density plot: shows how spread out values are.
- Boxplot: highlights variability and outliers.
- Bell curve: normal distribution visualizes the empirical rule.
- Error bars: often represent ±1 standard deviation.

### Chebyshev's inequality

For any distribution, at least \(1 - 1/k^2\) of values lie within \(k\) standard deviations of the mean.

Example: for \(k = 2\), at least 75% of values are within \(\pm 2\sigma\).

---

## 6. Related concepts

- Variance: \(\sigma^2\) for population, \(s^2\) for sample.
- Coefficient of variation (CV):

```math
\mathrm{CV} = \dfrac{\text{std dev}}{\text{mean}} \times 100\%
```

- Z-score:

```math
z = \dfrac{x - \mu}{\sigma}
```

- Standard error of the mean:

```math
\mathrm{SE} = \dfrac{s}{\sqrt{n}}
```

- Median absolute deviation (MAD): a robust alternative to standard deviation.

---

## 7. Python examples

```python
import numpy as np
import pandas as pd

data = np.array([85, 90, 78, 92, 88, 76, 95, 89])

# Population standard deviation
pop_std = np.std(data, ddof=0)
print(pop_std)  # ~5.96

# Sample standard deviation
sample_std = np.std(data, ddof=1)
print(sample_std)  # ~6.38

# Pandas sample standard deviation by default
df = pd.DataFrame({'scores': data})
print(df['scores'].std())
```

### Standardization with scikit-learn

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled = scaler.fit_transform(data.reshape(-1, 1))
```

### Visualization example

```python
import matplotlib.pyplot as plt
import seaborn as sns

mean = data.mean()
std = data.std(ddof=1)

sns.histplot(data, kde=True)
plt.axvline(mean - std, color='r', linestyle='--')
plt.axvline(mean + std, color='r', linestyle='--')
plt.show()
```

---

## 8. Common pitfalls

- Confusing population and sample formulas.
- Assuming normality when data are skewed or heavy-tailed.
- Using standard deviation alone for non-symmetric distributions.
- Forgetting whether to divide by \(n\) or \(n - 1\).
- Ignoring missing values: e.g. Pandas `std()` skips NaNs by default.

---

## 9. Applications in data science workflows

- EDA: `df.describe()` includes standard deviation.
- Anomaly detection: z-score thresholding or statistical rules.
- Dimensionality reduction: PCA uses covariance and variance.
- Regression diagnostics: residual standard deviation evaluates fit.
- A/B testing: pooled standard deviation appears in t-tests.
- Time series: volatility is a time-varying standard deviation.
- Deep learning: batch normalization uses mean and standard deviation.

---

## 10. Advanced considerations

- Weighted standard deviation for observations with different importance.
- Multivariate generalization: covariance matrix and Mahalanobis distance.
- Bootstrapping standard deviation for more reliable inference.
- Robust statistics: use `scipy.stats.median_abs_deviation` or IQR-based measures.
- Streaming/big data: Welford's online algorithm computes variance and standard deviation without storing all values.

---

## Practice exercise

Take a dataset such as daily temperatures. Compute standard deviation by month, interpret seasonal variability, standardize the data, and compare the result with median absolute deviation.

Standard deviation is simple but powerful. Understanding when to use it and when to use more robust measures is essential for strong data science analysis.
