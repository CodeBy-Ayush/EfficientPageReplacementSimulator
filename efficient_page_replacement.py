import matplotlib.pyplot as plt # Importing matplotlib library

# FIFO (First-In, First-out) page replacements Algo
def Calculate_fifo_faults(pages, total_frame):
  #Initialize the variable count page fault
    count = 0
    #store pages in memory
    memory_queue = []
    
    for page in pages:
        if page not in memory_queue:
            if len(memory_queue) < total_frame:
                memory_queue.append(page)
            else:
                memory_queue.pop(0)
                memory_queue.append(page)
            count += 1  # count pages fault 

    return count # return total no of page faults

# LRU (Least Recently Used) Algorithm
def Calculate_lru_faults(pages, total_frame):
    fault_count = 0
    recent_page = []

    for page in pages:
        if page not in recent_page:
            if len(recent_page) < total_frame:
                recent_page.append(page)
            else:
                recent_page.pop(0)
                recent_page.append(page)
            fault_count += 1
        else:
            recent_page.remove(page)
            recent_page.append(page)

    return fault_count

# Optimal Page Replacement Algo
def optimal_page_rep(pages, total_frame):
    faults_count = 0
    memory = []

    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < total_frame:
                memory.append(page)
            else:
                future_page = pages[i+1:]
                indices = [future_page.index(p) if p in future_page else float('inf') for p in memory]
                memory.pop(indices.index(max(indices)))
                memory.append(page)
            faults_count += 1

    return faults_count

# Main Function to Handle User Input
def main():
    page = list(map(int, input("Enter ref string (space-separated): ").split()))
    frame = int(input("Enter number of frame: "))

    count = Calculate_fifo_faults(page, frame)
    fault_count = Calculate_lru_faults(page, frame)
    faults_count = optimal_page_rep(page, frame)

    print(f"FIFO Page Faults: {count}")
    print(f"LRU Page Faults: {fault_count}")
    print(f"Optimal Page Faults: {faults_count}")

    # Graphical Representation
    algorithms = ["FIFO", "LRU", "Optimal"]
    fault = [count, fault_count, faults_count]

    plt.bar(algorithms, fault, color=['blue', 'red', 'green'])
    plt.xlabel("Page Replacement Algorithms")
    plt.ylabel("Page Faults")
    plt.title("Page Replacement Performance")
    plt.show()

if __name__ == "__main__":
    main()
