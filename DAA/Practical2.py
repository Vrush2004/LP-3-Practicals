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


# Job class: This class holds information for each job. Each job has a job_id, a deadline by which it needs to be finished, and a profit associated with completing that job.
# Function Definition: job_sequencing_with_deadlines
# Function: This function takes a list of jobs and returns the sequence of jobs to be done in order to maximize profit while adhering to deadlines.
# Sort the jobs: The jobs are sorted in decreasing order of profit using the lambda function key=lambda x: x.profit. This means that jobs with higher profits will be considered first.
# Find the maximum deadline: This line finds the latest deadline in the list of jobs. It helps in determining the size of the time slots array (to know how many time slots we need).
# Initialize time slots: A list time_slots is created to track the available time slots for each job. Each slot is initially set to -1, meaning it's free. The length of the time_slots array is max_deadline + 1 because we need slots up to the maximum deadline.
# Initialize total profit and job sequence: total_profit starts at 0 and will accumulate the total profit from all scheduled jobs. job_sequence is a list that will store the IDs of the jobs in the sequence they are scheduled.
# Main Loop: Assigning jobs to time slots
# Iterating through the jobs: The algorithm goes through each job in the sorted list of jobs.
# Find a free time slot: For each job, it tries to find a free time slot starting from the latest possible time slot (which is the job's deadline) down to 1. The loop runs from job.deadline to 1.
# Check if the time slot is free: If time_slots[t] == -1, it means the time slot t is free and available for the job.
# Assign the job to the free time slot: If a free slot is found, the job's job_id is assigned to the time_slots array at index t, and the profit of the job is added to total_profit. The job's ID is also added to the job_sequence list. The break statement exits the inner loop, meaning the current job is assigned and we move to the next job.
# Return the results: The function returns the job_sequence (the order in which the jobs should be completed) and the total_profit.
# Here, we define a list of jobs with their respective deadlines and profits.
# We call the function to get the job sequence and total profit, and then print the results.
# Possible Questions for an Exam:
# Explain the job sequencing with deadlines problem.

# Answer: The problem involves scheduling jobs with deadlines to maximize profit. The jobs are sorted by their profit in decreasing order, and then each job is assigned to the latest available time slot before its deadline.
# How does the greedy approach work for job sequencing?

# Answer: The greedy approach sorts the jobs by profit and assigns each job to the latest available time slot before its deadline. It maximizes profit by giving preference to jobs with higher profits first.
# What is the time complexity of the job sequencing algorithm?

# Answer: The time complexity of the algorithm is dominated by the sorting step, which is O(n log n), where n is the number of jobs. The loop that assigns jobs to time slots runs in O(n * m) time, where m is the maximum deadline. Therefore, the overall time complexity is O(n log n) due to sorting.
# Can this algorithm be used for any kind of job scheduling problem?

# Answer: No, this algorithm is designed specifically for problems where jobs have deadlines and profits. It works well when the objective is to maximize profit. It may not work for job scheduling problems that involve other constraints or objectives (like minimizing completion time).
# What happens if two jobs have the same profit?

# Answer: The algorithm will still prioritize jobs based on their profit first, but if two jobs have the same profit, they will be sorted based on the order they appear in the list (or based on their deadline if specified).