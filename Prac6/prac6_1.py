print("Name: S109 Neetu Salunkhe")

# CPU SCHEDULING ALGORITHMS (PART 2) - ROUND ROBIN
# Q4: Round Robin vs FCFS

# Configurable Time Quantum
TIME_QUANTUM = 2

processes = [
    ["P1", 0, 5],
    ["P2", 4, 2],
    ["P3", 5, 4]
]

# ROUND ROBIN

def round_robin(processes, quantum):

    n = len(processes)

    # Store process information
    remaining = {}
    arrival = {}
    burst = {}
    completion = {}
    first_start = {}

    for p, at, bt in processes:
        remaining[p] = bt
        arrival[p] = at
        burst[p] = bt

    # Ready queue
    queue = []

    # Gantt chart data
    gantt = []

    time = 0
    i = 0
    completed = 0
    context_switches = 0
    last_process = None

    processes = sorted(processes, key=lambda x: x[1])

    while completed < n:

        # Add newly arrived processes to ready queue
        while i < n and processes[i][1] <= time:
            queue.append(processes[i][0])
            i += 1

        # CPU idle
        if len(queue) == 0:
            time = processes[i][1]
            continue

        # Remove first process from queue
        current = queue.pop(0)

        # Response time: first time process gets CPU
        if current not in first_start:
            first_start[current] = time

        # Count context switch
        if last_process is not None and last_process != current:
            context_switches += 1

        start = time

        # Execute for time quantum or remaining burst
        run_time = min(quantum, remaining[current])

        time = time + run_time
        remaining[current] = remaining[current] - run_time

        gantt.append([current, start, time])

        last_process = current

        # Add processes that arrived during execution
        while i < n and processes[i][1] <= time:
            queue.append(processes[i][0])
            i += 1

        # If process is not completed, put it at end of queue
        if remaining[current] > 0:
            queue.append(current)

        else:
            completion[current] = time
            completed += 1


    # DISPLAY RESULTS
    
    print("\n\nROUND ROBIN SCHEDULING")
    print("Time Quantum =", quantum, "ms")
    print("---------------------------------------------")
    print("Process\tAT\tBT\tCT\tTAT\tWT\tRT")
    print("---------------------------------------------")

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

    print("---------------------------------------------")

    avg_tat = total_tat / n
    avg_wt = total_wt / n
    avg_rt = total_rt / n

    print("Average Turnaround Time =", round(avg_tat, 2), "ms")
    print("Average Waiting Time    =", round(avg_wt, 2), "ms")
    print("Average Response Time   =", round(avg_rt, 2), "ms")
    print("Context Switches        =", context_switches)

    # FAIRNESS

    print("\nFairness:")
    print("Round Robin gives each ready process")
    print("a fixed time quantum, so CPU access is")
    print("shared more fairly among processes.")

    # GANTT CHART IN IDLE SHELL


    print("\nGantt Chart:")

    print(gantt[0][1], end=" ")

    for p, start, end in gantt:
        print("|", p, "|", end, end=" ")

    print()


# FCFS

def fcfs(processes):

    processes = sorted(processes, key=lambda x: x[1])

    time = 0
    completion = {}
    first_start = {}

    gantt = []

    context_switches = 0
    last_process = None

    total_tat = 0
    total_wt = 0
    total_rt = 0

    for p, at, bt in processes:

        # CPU remains idle until process arrives
        if time < at:
            time = at

        start = time

        # Response time
        first_start[p] = start

        # Context switch
        if last_process is not None and last_process != p:
            context_switches += 1

        time = time + bt

        completion[p] = time

        gantt.append([p, start, time])

        last_process = p

    print("\n\nFCFS SCHEDULING")
    print("---------------------------------------------")
    print("Process\tAT\tBT\tCT\tTAT\tWT\tRT")
    print("---------------------------------------------")

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

    print("---------------------------------------------")

    n = len(processes)

    avg_tat = total_tat / n
    avg_wt = total_wt / n
    avg_rt = total_rt / n

    print("Average Turnaround Time =", round(avg_tat, 2), "ms")
    print("Average Waiting Time    =", round(avg_wt, 2), "ms")
    print("Average Response Time   =", round(avg_rt, 2), "ms")
    print("Context Switches        =", context_switches)

    print("\nFairness:")
    print("FCFS executes processes according")
    print("to their arrival order.")

    # --------------------------------------------------------
    # GANTT CHART IN IDLE SHELL
    # --------------------------------------------------------

    print("\nGantt Chart:")

    print(gantt[0][1], end=" ")

    for p, start, end in gantt:
        print("|", p, "|", end, end=" ")

    print()

# MAIN PROGRAM

print("CPU SCHEDULING ALGORITHMS - PART 2")
print("ROUND ROBIN vs FCFS")

round_robin(processes, TIME_QUANTUM)

fcfs(processes)
