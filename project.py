# Project name: SJF Non-Preemptive Scheduling with Job Queue


# Step 1: Get number of jobs
n = int(input("Enter number of jobs (at least 3): "))

while n < 3:

    print("Minimum 3 jobs required.")
    n = int(input("Enter number of jobs: "))

# Step 2: Take input for each job

jobs = []

for i in range(n):
    pid = input(f"Enter Job ID for job {i+1}: ")
    arrival = int(input(f"Enter Arrival Time for {pid}: "))
    burst = int(input(f"Enter Burst Time for {pid}: "))

    jobs.append({
        "id": pid,
        "arrival": arrival,
        "burst": burst,
        "done": False
    })

# Step 3: Initialize time and stats
time = 0
done_jobs = 0
order = []
total_tat = 0
total_wt = 0

# Step 4: Run the job queue
while done_jobs < n:

    # pick jobs that have arrived and not done yet
    # queue = [p for p in jobs if p["arrival"] <= time and not p["done"]]
    queue = []
    for p in jobs:
        if p["arrival"] <= time and not p["done"]:
            queue.append(p)


    if not queue:
        time += 1
        continue
    # continue means skip the rest loop and start aagain form begining.

    # pick job with smallest burst time
    queue.sort(key=lambda x: (x["burst"], x["arrival"]))

    # lamda is temprory function which return x:

    job = queue[0]

    # schedule job
    job["start"] = time
    job["complete"] = time + job["burst"]
    job["tat"] = job["complete"] - job["arrival"]
    job["wt"] = job["tat"] - job["burst"]
    
    time = job["complete"]
    job["done"] = True
    done_jobs += 1
    order.append(job["id"])
    
    total_tat += job["tat"]
    total_wt += job["wt"]

# Step 5: Print results
print("\nJob Execution Order:", " -> ".join(order))

# .join(order) will add -> betweeen in list

print("-" * 60)

# you can also use this:
# for i in range(60):
#     print("-", end="")  # print dash without new line

# print()  # move to the next line after printing all dashes

print("ID   | Arrival | Burst | Complete | Turnaround | Waiting")
print("-" * 60)
for i in jobs:
    print ( f"{i['id']:>4} |"
          f"{i['arrival']:>7} |" 
          f"{i['burst']:>5} |" 
          f"{i['complete']:>8} |" 
          f"{i['tat']:>10} |" 
          f"{i['wt']:>7}")


# Step 6: Print average times

avg_tat = total_tat / n
avg_wt = total_wt / n
print("-" * 60)
print(f"Average Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time   : {avg_wt:.2f}")
