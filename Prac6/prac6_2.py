print("Name: S109 Neetu Salunkhe")
# CPU SCHEDULING ALGORITHMS (PART 2) - ROUND ROBIN
# Q5

TIME_QUANTUM = 2

processes = [
    ["P1", 0, 5],
    ["P2", 1, 3],
    ["P3", 2, 6]
]


# ROUND ROBIN

def round_robin(processes, quantum):

    n = len(processes)

    remaining = {}
    arrival = {}
    burst = {}
    completion = {}
    first_start = {}

    for p, at, bt in processes:
        remaining[p] = bt
        arrival[p] = at
        burst[p] = bt

    queue = []
    gantt = []

    time = 0
    i = 0
    completed = 0
    context_switches = 0
    last_process = None

    processes = sorted(processes, key=lambda x: x[1])

    while completed < n:

        # Add arrived processes
        while i < n and processes[i][1] <= time:
            queue.append(processes[i][0])
            i += 1

        # CPU idle
        if len(queue) == 0:
            time = processes[i][1]
            continue

        # Get first process from queue
        current = queue.pop(0)

        # Response time
        if current not in first_start:
            first_start[current] = time

        # Context switch
        if last_process is not None and last_process != current:
            context_switches += 1

        start = time

        # Execute
        run_time = min(quantum, remaining[current])

        time = time + run_time
        remaining[current] -= run_time

        gantt.append([current, start, time])

        last_process = current

        # Add newly arrived processes
        while i < n and processes[i][1] <= time:
            queue.append(processes[i][0])
            i += 1

        # Reinsert unfinished process
        if remaining[current] > 0:
            queue.append(current)

        else:
            completion[current] = time
            completed += 1

    # RESULT

    print("\nROUND ROBIN SCHEDULING")
    print("Time Quantum =", quantum, "ms")
    print("--------------------------------------------------")
    print("Process\tAT\tBT\tCT\tTAT\tWT\tRT")
    print("--------------------------------------------------")

    total_tat = 0
    total_wt = 0
    total_rt = 0

    for p, at, bt in processes:

        ct = completion[p]
        tat = ct - at
        wt = tat - bt
        rt = first_start[p] - at

        total_tat += tat
        total_wt += wt
        total_rt += rt

        print(p, "\t", at, "\t", bt, "\t",
              ct, "\t", tat, "\t", wt, "\t", rt)

    print("--------------------------------------------------")

    print("Average Turnaround Time =",
          round(total_tat / n, 2), "ms")

    print("Average Waiting Time    =",
          round(total_wt / n, 2), "ms")

    print("Average Response Time   =",
          round(total_rt / n, 2), "ms")

    print("Context Switches        =",
          context_switches)

    print("\nFairness:")
    print("Each ready process gets a fixed")
    print("time quantum, providing fair CPU sharing.")

    # GANTT CHART

    print("\nGantt Chart:")

    print(gantt[0][1], end=" ")

    for p, start, end in gantt:
        print("|", p, "|", end, end=" ")

    print()

# MAIN
print("CPU SCHEDULING ALGORITHMS - PART 2")
print("ROUND ROBIN")


round_robin(processes, TIME_QUANTUM)
