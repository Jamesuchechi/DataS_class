import matplotlib
import matplotlib.pyplot as plt

hours = [1,2,3,4,5]
scores = [40,50,60,70,80]

plt.scatter(hours, scores)
plt.xlabel("Hours")
plt.ylabel("Scores")

if matplotlib.get_backend().lower() == 'agg':
    plt.savefig('correlation_plot.png')
    print('Saved plot to correlation_plot.png')
else:
    plt.show()