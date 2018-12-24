import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('data.csv')

sliced = df[['int_rate','purpose']]

sorted = sliced.sort_values('purpose')

labels = []
values = []

for x in sorted.purpose:
    if x not in labels:
        labels.append(x)

sorted = sorted.set_index(['purpose'])

for x in labels:
    df = sorted.loc[x:x].int_rate
    mean = df.mean()
    values.append(mean)

average = pd.DataFrame(values, index=labels, columns=['average_value'])

average.to_html('average.html')

plt.bar(labels, values, label='Average values')
plt.savefig('barChart.png')















