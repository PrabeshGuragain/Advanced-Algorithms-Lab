import time
import matplotlib.pyplot as plt

def activity_selection_greedy(activities):
    # Sorting activities based on their finish time
    activities.sort(key=lambda x: x[1])

    # The first activity always gets selected; Greedy Method
    selected_activities = [activities[0]]
    last_finish_time = activities[0][1]

    # For rest of the activities
    for i in range(1, len(activities)):
        if activities[i][0] >= last_finish_time:
            selected_activities.append(activities[i])
            last_finish_time = activities[i][1]

    return selected_activities

# Example 
activities = [(1, 3), (2, 4), (0, 6), (5, 7), (8, 9), (5, 9)]
selected = activity_selection_greedy(activities)
print("Selected activities:", selected)


def measure_time(activities):
    start_time = time.time()
    activity_selection_greedy(activities)
    end_time = time.time()
    return end_time - start_time

# Generate activities and measure time
input_sizes = list(range(100, 2100, 100))
times = []

for size in input_sizes:
    activities = [(i, i + 1) for i in range(size)]
    time_taken = measure_time(activities)
    times.append(time_taken)

# Plotting the results
plt.plot(input_sizes, times, marker='o')
plt.xlabel('Number of Activities')
plt.ylabel('Time Taken (seconds)')
plt.title('Activity Selection Algorithm Time Complexity')
plt.grid(True)
plt.show()