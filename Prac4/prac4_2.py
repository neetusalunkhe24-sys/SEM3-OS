print("Name: Neetu Salunkhe")
print("Roll No: S109")

# Non-Preemptive SJF Scheduling

process = ["P1", "P2", "P3", "P4"]
arrival = [0, 1, 2, 3]
burst = [5, 3, 8, 6]

n = len(process)

completed = [False] * n
completion = [0] * n
turnaround = [0] * n
waiting = [0] * n

time = 0
count = 0
gantt = []

while count < n:
    idx = -1
    minimum = float('inf')

    # Find process with shortest burst among arrived processes
    for i in range(n):
        if arrival[i] <= time and not completed[i]:
            if burst[i] < minimum:
                minimum = burst[i]
                idx = i

    # If no process has arrived, increment time
    if idx == -1:
        time += 1
        continue

    gantt.append((process[idx], time))

    time += burst[idx]
    completion[idx] = time
    turnaround[idx] = completion[idx] - arrival[idx]
    waiting[idx] = turnaround[idx] - burst[idx]

    completed[idx] = True
    count += 1

# Display Result
print("\nNon-Preemptive SJF Scheduling")
print("-" * 55)
print("Process\tAT\tBT\tCT\tTAT\tWT")
print("-" * 55)

for i in range(n):
    print(f"{process[i]}\t{arrival[i]}\t{burst[i]}\t{completion[i]}\t{turnaround[i]}\t{waiting[i]}")

avg_wt = sum(waiting) / n
avg_tat = sum(turnaround) / n

print("\nAverage Waiting Time =", round(avg_wt, 2), "ms")
print("Average Turnaround Time =", round(avg_tat, 2), "ms")

# Gantt Chart
print("\nGantt Chart:")
print("0", end="")

for i in range(len(gantt)):
    p = gantt[i][0]
    start = gantt[i][1]
    end = start + burst[process.index(p)]
    print(f" | {p} | {end}", end="")

print()
