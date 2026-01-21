# ===================================
# PROGRAM DETEKSI DEADLOCK (TABEL)
# ===================================

# 1. Dataset berbentuk tabel (list of dict)
table = [
    {"Proses": "P1", "Allocation": "R1", "Request": "R2"},
    {"Proses": "P2", "Allocation": "R2", "Request": "R3"},
    {"Proses": "P3", "Allocation": "R3", "Request": "R1"}
]

# Menampilkan tabel dataset
print("DATASET:")
print("Proses | Allocation | Request")
for row in table:
    print(f"{row['Proses']}     | {row['Allocation']}         | {row['Request']}")

# 2. Mencatat resource yang sedang dipegang
allocation = {}
for row in table:
    allocation[row["Allocation"]] = row["Proses"]

# 3. Membentuk Wait-For Graph
graph = {}
for row in table:
    process = row["Proses"]
    request = row["Request"]

    holder = allocation.get(request)
    if holder:
        graph.setdefault(process, []).append(holder)

# 4. Fungsi DFS untuk deteksi siklus
visited = set()
rec_stack = set()

def detect_deadlock(p):
    visited.add(p)
    rec_stack.add(p)

    for neighbor in graph.get(p, []):
        if neighbor not in visited:
            if detect_deadlock(neighbor):
                return True
        elif neighbor in rec_stack:
            return True

    rec_stack.remove(p)
    return False

# 5. Eksekusi deteksi deadlock
deadlock = False
for p in graph:
    if p not in visited:
        if detect_deadlock(p):
            deadlock = True
            break

# 6. Menampilkan hasil
print("\nWAIT-FOR GRAPH:")
for p in graph:
    print(f"{p} -> {graph[p]}")

print("\nHASIL EKSEKUSI:")
if deadlock:
    print("DEADLOCK TERDETEKSI")
else:
    print("TIDAK ADA DEADLOCK")
