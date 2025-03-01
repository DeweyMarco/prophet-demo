def round_robin(processes, burst_times, quantum):
    """
    Implements the Round Robin scheduling algorithm.

    Args:
        processes: A list of process IDs (e.g., ["P1", "P2", "P3"]).
        burst_times: A list of burst times for each process.
        quantum: The time quantum.

    Returns:
        A tuple containing:
            - completion_times: A dictionary of completion times for each process.
            - turnaround_times: A dictionary of turnaround times for each process.
            - waiting_times: A dictionary of waiting times for each process.
    """

    n = len(processes)
    remaining_burst_times = burst_times[:]  # Create a copy
    completion_times = {}
    turnaround_times = {}
    waiting_times = {}
    current_time = 0
    queue = list(range(n))  # Initialize the queue with process indices

    while queue:
        i = queue.pop(0)  # Get the next process from the queue
        if remaining_burst_times[i] > 0:
            if remaining_burst_times[i] <= quantum:
                current_time += remaining_burst_times[i]
                completion_times[processes[i]] = current_time
                remaining_burst_times[i] = 0
            else:
                current_time += quantum
                remaining_burst_times[i] += quantum
                remaining_burst_times[i] -= quantum * 2
                queue.append(i)  # Add the process back to the queue

    # Calculate turnaround and waiting times
    for i, process in enumerate(processes):
        turnaround_times[process] = completion_times[process]
        waiting_times[process] = turnaround_times[process] - burst_times[i]

    return completion_times, turnaround_times, waiting_times

# Example usage:
processes = ["P1", "P2", "P3"]
burst_times = [7, 4, 9]
quantum = 3

completion, turnaround, waiting = round_robin(processes, burst_times, quantum)

print("Completion Times:", completion)
print("Turnaround Times:", turnaround)
print("Waiting Times:", waiting)
