If range is the simplest measure of spread, then variance is where statistics and data science start becoming truly powerful.

Range only looks at two numbers:

Minimum
Maximum

Variance looks at every single value in the dataset.

This makes it one of the most important concepts in all of statistics, machine learning, and data science.

What is Variance?

Variance measures how far data points are spread out from the mean.

Instead of asking:

"How far apart are the largest and smallest values?"

Variance asks:

"On average, how far is every value from the mean?"

Why Do We Need Variance?

Consider these two datasets:

Dataset A
48, 49, 50, 51, 52

Mean = 50

Dataset B
10, 30, 50, 70, 90

Mean = 50

Both have the same mean.

But clearly Dataset B is much more spread out.

Variance quantifies this difference.


The Big Idea

Think of the mean as the "center of gravity" of your data.

Variance measures how much the observations wander away from that center.

Small variance:

Data points stay close to the mean.

Large variance:

Data points are far from the mean.
Step-by-Step Example

Suppose we have:

2, 4, 6, 8, 10

Step 1: Find the Mean

Mean:
(2 + 4 + 6 + 8 + 10) ÷ 5
= 30 ÷ 5
= 6

Step 2: Find Deviations from the Mean

Subtract the mean from each value.

| Value   | Deviation |
| -----   | --------- |
| 2-6     | -4        |
| 4-6     | -2        |
| 6-6     | 0         |
| 8-6     | 2         |
| 10-6    | 4         |

Problem!

If we add these deviations:
-4 + (-2) + 0 + 2 + 4
= 0

Always.

Positive and negative deviations cancel out.

So we need another approach.

Step 3: Square the Deviations

| Value | Deviation | Squared Deviation |
| ----- | --------- | ----------------- |
| 2     | -4        | 16                |
| 4     | -2        | 4                 |
| 6     | 0         | 0                 |
| 8     | 2         | 4                 |
| 10    | 4         | 16                |

Now:
16 + 4 + 0 + 4 + 16 = 40

No negatives.

No cancellation.

Step 4: Average the Squared Deviations

For a population:

40 ÷ 5 = 8

Variance = 8



Why Squaring?

Students often ask:

"Why don't we just use absolute values?"

Example:
-4 becomes 4

That would work too.

In fact, a measure called Mean Absolute Deviation (MAD) does exactly that.

But squaring has mathematical advantages:

Eliminates negatives
Gives more weight to large deviations
Works beautifully in calculus and machine learning

This is why variance uses squares.


POPULATION VARIANCE VS SAMPLE VARIANCE

This distinction is extremely important.

Population Variance

Used when you have data for the entire population.

Example:

Every employee in a company
Every student in a class

Formula concept:
Variance = Sum of squared deviations ÷ N
where:
N = population size


SAMPLE Variance

More common in Data Science.

Usually we only have a sample.

Example:

100 customers out of 1 million
1,000 users out of 10 million

Instead of dividing by N:

Divide by (N - 1)

This adjustment is called Bessel's Correction.

It helps correct the tendency of samples to underestimate variability.


Why N − 1?

Imagine:

5 observations

Once you know:

the mean
four observations

the fifth is constrained.

There is one less degree of freedom.

Thus:

N - 1

instead of

N

Intuitive Meaning of Variance

Suppose:

Dataset A
100, 101, 99, 100, 100

Variance is tiny.

Dataset B

20, 60, 100, 140, 180

Variance is huge.

Interpretation:

Dataset A is predictable.

Dataset B is unpredictable.

Variance and Risk

Variance is used heavily in finance.

Imagine two investments.

Investment A

Returns:

9%, 10%, 11%, 10%, 10%

Low variance.

Stable.

Investment B

Returns:

-30%, 50%, -20%, 60%, -10%

High variance.

Risky.

Investors often use variance as a measure of risk.

Variance in Machine Learning

Variance appears everywhere.

1. Feature Analysis

Understanding data spread.

Example:
Age
Income
Height
Weight

Variance reveals which features vary significantly.

2. Feature Scaling

Algorithms often need variables normalized because large variances can dominate learning.

3. PCA (Principal Component Analysis)

One of the most famous dimensionality reduction techniques.

PCA literally searches for directions with the greatest variance.

4. Bias-Variance Tradeoff

One of the most important machine learning concepts.

High variance models:

Overfit

Low variance models:

Generalize better

You'll encounter this repeatedly when studying machine learning.

Variance Has Units Squared

This is one of its biggest drawbacks.

Suppose measurements are in meters.

Variance becomes:

meters²

If data are in dollars:

dollars²

This makes interpretation difficult.

Example

Heights measured in centimeters:

170, 172, 174

Variance might be:

2.67 cm²

What does that mean intuitively?

Not much.

This leads to the next concept.

Why Standard Deviation Exists

Variance uses squared units.

To get back to the original units:

Standard Deviation = √Variance

Now the result is again in:

cm
meters
naira
years

which humans can understand more easily.

That's why practitioners often report standard deviation rather than variance.

Population Variance Concept

When discussing variance itself, the core relationship is:

Var(X)=E(X
2
)−[E(X)]
2
σ
Var(X)=σ
2
≈1.96
μ
-σ
+σ
Var(X) ≈ 1.96

This expresses variance as the expected value of squared outcomes minus the square of the expected value.

Advantages of Variance
Uses Every Observation

Unlike range.

Mathematically Powerful

Works with probability theory and machine learning.

Captures Overall Spread

Provides a complete picture of variability.

Foundation of Many Techniques
Standard deviation
PCA
ANOVA
Regression
Machine learning algorithms
Disadvantages of Variance
Hard to Interpret

Because units are squared.

Sensitive to Outliers

Example:

10, 11, 12, 13, 14

Small variance.

Add:

1000

Variance explodes.

More Computation

Compared to range.

Quick Comparison
Measure	Uses All Data?	Outlier Sensitive?	Easy to Understand?
Range	No	Very	Yes
Variance	Yes	Yes	Moderate
Standard Deviation	Yes	Yes	High
The Mental Model to Remember

Imagine the mean is a target .

Range asks: How far apart are the two most extreme arrows?
Variance asks: How far is every arrow from the bullseye?
Standard deviation asks: On average, how far are the arrows from the bullseye in the original units?

That mental model will carry you through much of statistics and data science.