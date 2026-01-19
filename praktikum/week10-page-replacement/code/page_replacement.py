def fifo(reference_string, frame_size):
    frames = []
    page_faults = 0
    queue_index = 0
    for page in reference_string:
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                frames[queue_index] = page
                queue_index = (queue_index + 1) % frame_size
            page_faults += 1
    return page_faults

def lru(reference_string, frame_size):
    frames = []
    page_faults = 0
    recent_use = {}
    for i, page in enumerate(reference_string):
        if page not in frames:
            if len(frames) < frame_size:
                frames.append(page)
            else:
                lru_page = min(frames, key=lambda p: recent_use.get(p, -1))
                frames[frames.index(lru_page)] = page
            page_faults += 1
        recent_use[page] = i
    return page_faults

# Contoh eksekusi
reference_string = [7,0,1,2,0,3,0,4,2,3,0,3,2]
frame_size = 3

print("FIFO Page Faults:", fifo(reference_string, frame_size))
print("LRU Page Faults :", lru(reference_string, frame_size))