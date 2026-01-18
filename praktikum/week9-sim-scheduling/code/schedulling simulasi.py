def fcfs(processes):
    current_time = 0
    total_waiting = 0
    total_turnaround = 0

    # urutkan berdasarkan arrival time
    processes.sort(key=lambda x: x[1])

    print("=== FCFS ===")
    print("PID | AT | BT | WT | TAT")
    print("---------------------------")

    for pid, arrival, burst in processes:

        if current_time < arrival:
            current_time = arrival

        waiting = current_time - arrival
        turnaround = waiting + burst

        current_time += burst
        total_waiting += waiting
        total_turnaround += turnaround

        print(f"{pid:>3} | {arrival:>2} | {burst:>2} | {waiting:>2} | {turnaround:>3}")

    n = len(processes)
    print("---------------------------")
    print(f"Rata-rata Waiting   : {total_waiting / n:.2f}")
    print(f"Rata-rata Turnaround: {total_turnaround / n:.2f}")

def sjf_non_preemptive(processes):
    time = 0
    completed = []
    results = []

    n = len(processes)

    while len(completed) < n:
        # proses yang sudah datang & belum selesai
        ready = [p for p in processes
                 if p["arrival"] <= time and p["pid"] not in completed]

        if not ready:
            time += 1
            continue

        # pilih burst time paling kecil
        selected = min(ready, key=lambda x: x["burst"])

        waiting = time - selected["arrival"]
        turnaround = waiting + selected["burst"]

        results.append({
            "pid": selected["pid"],
            "arrival": selected["arrival"],
            "burst": selected["burst"],
            "waiting": waiting,
            "turnaround": turnaround
        })

        time += selected["burst"]
        completed.append(selected["pid"])

    return results

def print_table(title, results):
    print(f"=== {title} ===")
    print("PID | AT | BT | WT | TAT")
    print("---------------------------")

    total_waiting = 0
    total_turnaround = 0

    for r in results:
        print(f"{r['pid']:>3} | {r['arrival']:>2} | {r['burst']:>2} | {r['waiting']:>2} | {r['turnaround']:>3}")
        total_waiting += r["waiting"]
        total_turnaround += r["turnaround"]

    n = len(results)
    print("---------------------------")
    print(f"Rata-rata Waiting   : {total_waiting / n:.2f}")
    print(f"Rata-rata Turnaround: {total_turnaround / n:.2f}")
