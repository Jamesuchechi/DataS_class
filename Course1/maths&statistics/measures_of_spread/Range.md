# Understanding Range in Data Science

## What is Range?

Range is the simplest measure of variability. It tells us the difference between the largest and smallest values in a dataset.

**Formula:**

`Range = Maximum value - Minimum value`

## Why Do We Need Range?

Suppose two classes write a test:

- Class A scores: `70, 71, 72, 73, 74`
- Class B scores: `20, 50, 80, 90, 120`

Both classes have the same average: `Mean = 72`.

But they are not similar.

- Class A scores are clustered closely together.
- Class B scores are spread out.

Range helps us identify how spread out the data is.

## Example 1

**Dataset:** `4, 8, 12, 15, 20`

1. Maximum = `20`
2. Minimum = `4`
3. Range = `20 - 4 = 16`

**Result:** `Range = 16`

## Visual Interpretation

Imagine a number line:

`4 ---- 8 ---- 12 ---- 15 ---- 20`

The range measures the distance from `4 → 20`.
It does not depend on the values in between, only the endpoints.

## Example 2

**Heights of students (cm):** `150, 155, 158, 160, 165`

- Maximum = `165`
- Minimum = `150`
- Range = `165 - 150 = 15`

The heights vary by `15 cm`.

## What Does a Large Range Mean?

A large range means the observations are spread out.

**Example:** `2, 10, 15, 20, 100`

- Range = `100 - 2 = 98`

The values are widely dispersed.

## What Does a Small Range Mean?

**Example:** `48, 49, 50, 51, 52`

- Range = `52 - 48 = 4`

The values are close together.

## Range and Variability

Range is a measure of variability.
Variability answers:

> “How much do the values differ from one another?”

- A larger range means more variability and more spread.
- A smaller range means less variability and more consistency.

## Important Property of Range

Range depends only on:

- The largest value
- The smallest value

Everything else is ignored.

**Example:**

- Dataset A: `1, 2, 3, 4, 10`
- Dataset B: `1, 5, 5, 5, 10`

Both have the same range:

- `Range = 10 - 1 = 9`

Yet the datasets have very different distributions. This is one weakness of range.

## Sensitivity to Outliers

An outlier is an unusually large or small observation.

**Example 1:** `10, 12, 14, 15, 16`

- Range = `16 - 10 = 6`

**Example 2:** `10, 12, 14, 15, 100`

- Range = `100 - 10 = 90`

Only one value changed, but the range grew from `6` to `90`.
Range is therefore very sensitive to outliers.

## Why Data Scientists Don't Rely Only on Range

Range ignores most of the data.

**Example:**

- `1, 2, 3, 4, 100` → Range = `99`
- `1, 50, 50, 50, 100` → Range = `99`

Both datasets have the same range, but very different distributions.

That is why we later use measures like:

- Variance
- Standard deviation
- Interquartile range (IQR)

These use more information from the dataset.

## Real-Life Example

Suppose a company tracks employee ages:

`22, 24, 25, 28, 60`

- Range = `60 - 22 = 38`

Interpretation: The age span in the company is `38 years`.

## Range in Data Science Projects

Range is often used during exploratory data analysis (EDA).
Before building models, data scientists ask:

- What is the minimum value?
- What is the maximum value?
- How spread out is the data?

Range provides a quick answer.

**Example:**

- Salary min = `₦50,000`
- Salary max = `₦5,000,000`
- Range = `₦4,950,000`

This immediately suggests high variability.

## Absolute Range vs Relative Range

- **Absolute range:** `Maximum − Minimum`
- **Relative range:** sometimes calculated as `(Maximum + Minimum) / (Maximum − Minimum)` or another ratio.

Relative range is less common in introductory statistics but is used in some analyses.

## Advantages of Range

1. Easy to calculate
   - Only requires the maximum and minimum values.
2. Easy to understand
   - Anyone can interpret it.
3. Quick snapshot of spread
   - Useful during initial data exploration.

## Disadvantages of Range

1. Uses only two values
   - Ignores all other observations.
2. Highly sensitive to outliers
   - One extreme value can drastically change the range.
3. Not stable
   - Small dataset changes can dramatically affect it.
4. Poor measure for detailed analysis
   - Does not fully describe variability.

## Range vs Variance vs Standard Deviation

| Measure              | Uses All Data? | Sensitive to Outliers? | Complexity |
|----------------------|----------------|------------------------|------------|
| Range                | ❌ No          | ✅ Very                | Easy       |
| Variance             | ✅ Yes         | ✅ Yes                 | Moderate   |
| Standard Deviation   | ✅ Yes         | ✅ Yes                 | Moderate   |
| IQR                  | Partly         | ❌ Less                | Moderate   |

Range is usually the first measure of spread you learn, but it is not the last.

## Practice Questions

**Question 1**

- Dataset: `3, 7, 8, 12, 15`
- Range: `15 - 3 = 12`

**Question 2**

- Dataset: `22, 30, 35, 40, 45, 50`
- Range: `50 - 22 = 28`

**Question 3**

- Dataset: `5, 5, 5, 5, 5`
- Range: `5 - 5 = 0`

Interpretation: There is no variability because every observation is identical.
