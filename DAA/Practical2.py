# Practical 2: Implement job sequencing with deadlines using a greedy method.

class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_sequencing_with_deadlines(jobs):
    # Sort jobs based on decreasing order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Find the maximum deadline to create a time slot array
    max_deadline = max(job.deadline for job in jobs)
    time_slots = [-1] * (max_deadline + 1)  # Array to track free time slots

    total_profit = 0
    job_sequence = []

    # Iterate over the sorted jobs
    for job in jobs:
        # Find a free time slot for this job, starting from the latest slot before its deadline
        for t in range(min(max_deadline, job.deadline), 0, -1):
            if time_slots[t] == -1:  # If the time slot is free
                time_slots[t] = job.job_id  # Assign the job to this time slot
                total_profit += job.profit  # Add profit to the total
                job_sequence.append(job.job_id)  # Add job to the sequence
                break  # Move to the next job after assigning

    return job_sequence, total_profit

# Example usage:
jobs = [
    Job('Job1', 2, 100),
    Job('Job2', 1, 19),
    Job('Job3', 2, 27),
    Job('Job4', 1, 25),
    Job('Job5', 3, 15)
]

job_sequence, total_profit = job_sequencing_with_deadlines(jobs)
print(f"Job sequence: {job_sequence}")
print(f"Total profit: {total_profit}")