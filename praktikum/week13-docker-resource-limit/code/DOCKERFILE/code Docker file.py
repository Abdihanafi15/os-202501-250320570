import time

# Menguji CPU (komputasi berulang)
def cpu_test():
    print("CPU test started")
    x = 0
    for i in range(1, 100000000):
        x += i
    print("CPU test finished")

# Menguji Memori (alokasi bertahap)
def memory_test():
    print("Memory test started")
    a = []
    try:
        for i in range(1, 1000000):
            a.append("A" * 10000)  # alokasi memori besar
            if i % 100000 == 0:
                print(f"Allocated {i} chunks")
                time.sleep(0.5)
    except MemoryError:
        print("MemoryError: memory limit reached!")

    print("Memory test finished")

if __name__ == "__main__":
    cpu_test()
    memory_test()
