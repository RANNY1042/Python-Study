from die import Die
import matplotlib.pyplot as plt

die = Die()

results = []
for roll_num in range(1000):
        result = die.roll()
        results.append(result)
    
# print(results)

frequencies = []
poss_results = range(1, die.num_sides+1)

for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

x_values = poss_results
y_values = frequencies

# fig, ax = plt.subplots(x_values, y_values)

plt.show()