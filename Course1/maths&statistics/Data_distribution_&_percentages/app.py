import matplotlib
import matplotlib.pyplot as plt

ages = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

plt.hist(ages, bins=10)
plt.xlabel('Ages')
plt.ylabel('Frequency')
plt.title('Distribution of Ages')

if matplotlib.get_backend().lower() == 'agg':
    plt.savefig('ages_distribution.png')
    print('Saved plot to ages_distribution.png')
else:
    plt.show()