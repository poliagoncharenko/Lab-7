import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import csv

sulfate_index = 4
with open("data2.csv", encoding='utf-8') as r_file:
    file = list(csv.reader(r_file, delimiter =","))
    file.pop(0)
    sulfate_values = [float(line[sulfate_index]) for line in file if line[sulfate_index]]
sulfate_values = np.array(sulfate_values, float)


deviation = np.std(sulfate_values)
print(f'Среднеквадратичное отклонение равно {deviation}')


fig = plt.figure(figsize=(10, 4))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
fig.subplots_adjust(wspace=0.5)


ax1.hist(sulfate_values, bins = 20)
ax1.set_title('Distribution')
ax1.set_xlabel('Sulfate values')
ax1.set_ylabel('Frequency')


ax2.hist(sulfate_values, bins = 20, density=True)
ax2.set_title('Normal distribution')
ax2.set_xlabel('Sulfate values')
ax2.set_ylabel('Frequency')
plt.show()
