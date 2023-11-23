import matplotlib.pyplot as plt

# Define the functions T(n) and R(n)
def bubble_sort(array):
    for i in range(len(array) - 1):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

def selection_sort(array):
    for i in range(len(array) - 1):
        smallest_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest_index]:
                smallest_index = j
        array[i], array[smallest_index] = array[smallest_index], array[i]

def T(n):
    return n**2

def R(n):
    return n**2

# Generate input data
n_values = range(1, 1001)

# Calculate T(n) and R(n) for each input value
T_values = [T(n) for n in n_values]
R_values = [R(n) for n in n_values]

# Plot the functions
plt.plot(n_values, T_values, label='T(n)')
plt.plot(n_values, R_values, label='R(n)')

# Add labels and title
plt.xlabel('n')
plt.ylabel('Time complexity')
plt.title('Time complexity of bubble sort and selection sort')

# Add legend
plt.legend()

# Show the plot
plt.show()