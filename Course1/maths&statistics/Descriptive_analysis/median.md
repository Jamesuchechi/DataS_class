

MEDIAN(Middle number):

The median is the middle number when data is arranged in order. i.e is the middle number when you arrange numbers from the smallest to the biggest.

Examples:

Example (Odd number of values)

2, 4, 6, 8, 10
Median = 6

Example (Even number of values)

2, 4, 6, 8
Median = 4 + 6 = 10
10/2 = 5

so median = 5

Why Median is cool:
It doesn't care about super big or small numbers. It's like the "real middle" of the group.
Great for things like house prices or salaries — where one super rich person doesn't trick you.

## In-Depth Explanation of median.md
This file explains median as the middle value in sorted data, with odd/even examples. It praises its robustness to extremes, using house prices/salaries as examples.

**Expanded Details**:
- **Mathematical Foundation**: For odd n: Median = (n+1)/2 th value. For even n: Average of n/2 and (n/2)+1 th values. It's the 50th percentile.
- **Calculation Steps**:
  1. Sort data ascending.
  2. Find middle position(s).
  3. If even, average the two middles.
- **Pros**:
  - Robust: Unaffected by outliers (e.g., one mansion doesn't skew house price median).
  - Represents "Typical" Better: In asymmetric data, closer to most people's experience.
  - Non-Parametric: Works with ordinal data (e.g., rankings).
- **Cons**:
  - Ignores Extremes: May miss important tails (e.g., in finance, ignoring high-risk outliers).
  - Less Precise: Doesn't use all data points fully.
  - Tied Values: In even counts, averaging can create non-integer medians.
- **Examples Expanded**:
  - Odd: Ages 20,25,30,35,40 → Median 30.
  - Even: 20,25,30,35 → (25+30)/2 = 27.5.
  - Salaries: Median avoids CEO pay distortion; e.g., median US household income is ~$70k, not the mean ~$100k.
- **When to Use**: Skewed distributions (e.g., wealth, test scores with few high achievers). In medicine, median survival time.
- **Common Mistakes**: Forgetting to sort; confusing with mean in small datasets.
- **Advanced Note**: Quartiles (25th, 75th percentiles) extend median for spread analysis. In box plots, median is the central line.

This file emphasizes fairness, making median a "people's champion" against outlier-biased means.