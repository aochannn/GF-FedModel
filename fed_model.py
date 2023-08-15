#Fed Model
import matplotlib.pyplot as plt

# Sample data
x_data = [1, 2, 3, 4, 5]
y_data1 = [2, 4, 6, 8, 10]
y_data2 = [1, 3, 5, 7, 9]

# Create a new figure
plt.figure()

# Plot the first set of data
plt.plot(x_data, y_data1, label='Dataset 1', color='blue', marker='o')

# Plot the second set of data
plt.plot(x_data, y_data2, label='Dataset 2', color='red', marker='x')

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Two Sets of Data')

# Add a legend
plt.legend()

# Show the plot
plt.show()
