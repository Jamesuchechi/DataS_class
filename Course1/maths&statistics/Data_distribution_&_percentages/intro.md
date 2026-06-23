# Data Distributions & Percentages

This topic is one of the most important foundations in Data Science and Data Analysis because almost every dataset contains distributions, proportions, and percentages.

## Why this matters

Data analysis answers:

- How are values spread out?
- What percentage belongs to each category?
- What patterns exist in the data?
- Are there unusual values?
- Is the data balanced or skewed?

## 1. What is a Data Distribution?

A data distribution describes how data values are spread across a dataset.

Imagine a class of students scored:

```
45, 50, 55, 60, 65, 70, 75, 80, 85
```

The distribution tells us:

- Where most scores are located
- Whether scores are evenly spread
- Whether there are extreme values

### Example dataset: Age of customers

```
18
20
20
22
25
25
25
27
30
32
35
40
```

Notice:

- Many customers are in their twenties
- Few are above 35

This pattern is called the distribution.

### Why distribution matters

Imagine two companies:

- Company A: `50, 50, 50, 50, 50`
- Company B: `10, 20, 50, 80, 90`

Both have average = 50, but the distributions are completely different.

**Distribution reveals what averages hide.**

## 2. Frequency Distribution

Frequency means how many times a value appears.

### Dataset

```
Red
Blue
Blue
Green
Red
Blue
Red
```

### Frequency table

| Color | Frequency |
| ----: | --------: |
|   Red |         3 |
|  Blue |         3 |
| Green |         1 |

This is called a frequency distribution.

### Python example

```python
colors = [
    "Red",
    "Blue",
    "Blue",
    "Green",
    "Red",
    "Blue",
    "Red"
]

from collections import Counter

print(Counter(colors))
```

Output:

```python
{'Red': 3, 'Blue': 3, 'Green': 1}
```

## 3. Relative Frequency

Instead of counts, we measure proportion.

**Formula:**

```
Relative Frequency = Frequency ÷ Total Observations
```

### Example

| Color | Frequency | Relative Frequency |
| ----: | --------: | -----------------: |
|   Red |         3 |         3/7 = 0.43 |
|  Blue |         3 |         3/7 = 0.43 |
| Green |         1 |         1/7 = 0.14 |

Total observations = 7.

## 4. Percentages

Percentage simply means "out of 100." 

**Formula:**

```
Percentage = (Value ÷ Total) × 100
```

### Example

Class contains 40 students.

- Females: 24 → `24 ÷ 40 × 100 = 60%`
- Males: 16 → `16 ÷ 40 × 100 = 40%`

## 5. Percentage Distribution

A percentage distribution shows how the whole dataset is divided.

### Example survey

| Device  | Users |
| :------ | ----: |
| Android |   500 |
| iPhone  |   300 |
| Laptop  |   200 |

Total = 1000.

| Device  | Percentage |
| :------ | ---------: |
| Android |        50% |
| iPhone  |        30% |
| Laptop  |        20% |

## 6. Normal Distribution

The most famous distribution in Data Science, also called the bell curve.

### Characteristics

- Most values near the center
- Few extreme values
- Symmetrical shape

### Examples

- Human heights
- IQ scores
- Exam scores (often)
- Blood pressure

### Example heights

```
150
155
160
165
170
175
180
185
190
```

Most people cluster around 170. Very short and very tall people are fewer.

## 7. Skewed Distribution

Not all data is balanced. Sometimes data leans toward one side.

### Right skewed

- Most values are low or moderate
- A few values are very high

Examples: income, wealth, house prices.

### Left skewed

- Most values are high
- A few values are very low

Examples: easy exam scores where most students score high.

## 8. Uniform Distribution

Every value appears equally.

Example: dice rolls.

```
1 2 3 4 5 6
```

Each outcome has equal probability: `1/6`.

## 9. Cumulative Percentage

Shows running percentages over ordered categories.

### Example: exam scores

| Score | Students | Cumulative Count | Cumulative % |
| ----: | -------: | ---------------: | -----------: |
|    50 |        5 |                5 |          10% |
|    60 |       10 |               15 |          30% |
|    70 |       15 |               30 |          60% |
|    80 |       20 |               50 |         100% |

## 10. Histograms

Histograms visualize distributions using bars.

### Dataset

```
18
20
22
24
26
28
30
32
34
```

### Grouped ranges

| Age Range | Count |
| :-------: | ----: |
|   18–22   |     3 |
|   23–27   |     3 |
|   28–32   |     3 |
|   33–37   |     2 |

Example histogram:

```
18-22  ###
23-27  ###
28-32  ###
33-37  ##
```

## 11. Percentage Change

Very common in business analytics.

**Formula:**

```
Percentage Change = ((New - Old) ÷ Old) × 100
```

### Example

- January = 500
- February = 650

```
(650 - 500) ÷ 500 × 100 = 30%
```

Sales increased by 30%.

## 12. Market Share Analysis

Market share compares category share within a total.

### Example

| Company | Sales |
| :------ | ----: |
| A       |   400 |
| B       |   300 |
| C       |   300 |

Total = 1000.

| Company | Share |
| :------ | ----: |
| A       |   40% |
| B       |   30% |
| C       |   30% |

Analysts use this to compare competitors.

## Real-World Data Science Applications

- E-commerce: product category percentages, customer age distributions, revenue distributions
- Healthcare: disease distributions, recovery rates, patient demographics
- Finance: income distributions, investment allocations, market share analysis
- Social media: engagement percentages, follower demographics, content performance distributions

## Key Takeaways

- Distribution describes how data is spread.
- Frequency counts occurrences.
- Relative frequency measures proportion.
- Percentage = `(Value ÷ Total) × 100`.
- Percentage distribution shows category shares.
- Normal distribution forms a bell curve.
- Skewed distribution leans left or right.
- Uniform distribution spreads evenly.
- Histograms visualize distributions.
- Percentage change measures growth or decline.

> In data analysis, before building models or dashboards, one of the first questions to ask is:
>
> "How is my data distributed, and what percentage of the data belongs to each category?"
>
> Answering that question often reveals more insight than complex machine learning models.


Example:

Sales:

January = 500
February = 650
(650 - 500)
-----------
500
×100
30%

Sales increased by:

30%

12. Market Share Analysis

One of the biggest uses of percentages.

Company Sales

Company	Sales
A	400
B	300
C	300

Total:

1000

Market Share:

Company	Share
A	40%
B	30%
C	30%

Analysts use this to compare competitors.

Real-World Data Science Applications

E-commerce
Product category percentages
Customer age distributions
Revenue distributions

Healthcare
Disease distributions
Recovery rates
Patient demographics

Finance
Income distributions
Investment allocations
Market share analysis

Social Media
Engagement percentages
Follower demographics
Content performance distributions

Key Takeaways
Distribution describes how data is spread.
Frequency counts occurrences.
Relative Frequency measures proportion.
Percentage = (Value ÷ Total) × 100
Percentage Distribution shows category shares.
Normal Distribution forms a bell curve.
Skewed Distribution leans left or right.
Uniform Distribution spreads evenly.
Histograms visualize distributions.
Percentage Change measures growth or decline.

In data analysis, before building models or dashboards, one of the first questions to ask is:

"How is my data distributed, and what percentage of the data belongs to each category?"

Answering that question often reveals more insight than complex machine learning models.