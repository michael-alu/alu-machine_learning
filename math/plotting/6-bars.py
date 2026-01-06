#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))  

people = ['Farrah', 'Fred', 'Felicia']
bar_width = 0.5
x = np.arange(len(people))


plt.bar(x, fruit[0], color='red', width=bar_width, label='Apples')
plt.bar(x, fruit[1], bottom=fruit[0], color='yellow', width=bar_width, label='Bananas')
plt.bar(x, fruit[2], bottom=fruit[0] + fruit[1], color='#ff8000', width=bar_width, label='Oranges')
plt.bar(x, fruit[3], bottom=fruit[0] + fruit[1] + fruit[2], color='#ffe5b4', width=bar_width, label='Peaches')

plt.ylabel('Quantity of Fruit')
plt.yticks(np.arange(0, 81, 10))  
plt.title('Number of Fruit per Person')
plt.xticks(x, people)  
plt.legend()  


plt.show()