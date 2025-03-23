import matplotlib.pyplot as plt

# FIFO Page Replacement Algorithm
def fifo_page_replacement(pages, frames):
    page_faults = 0
    queue = []
    
    for page in pages:
        if page not in queue:
            if len(queue) < frames:
                queue.append(page)
            else:
                queue.pop(0)
                queue.append(page)
            page_faults += 1

    return page_faults

# LRU Page Replacement Algorithm
def lru_page_replacement(pages, frames):
    page_faults = 0
    stack = []

    for page in pages:
        if page not in stack:
            if len(stack) < frames:
                stack.append(page)
            else:
                stack.pop(0)
                stack.append(page)
            page_faults += 1
        else:
            stack.remove(page)
            stack.append(page)

    return page_faults

# Optimal Page Replacement Algorithm
def optimal_page_replacement(pages, frames):
    page_faults = 0
    memory = []

    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                future_pages = pages[i+1:]
                indices = [future_pages.index(p) if p in future_pages else float('inf') for p in memory]
                memory.pop(indices.index(max(indices)))
                memory.append(page)
            page_faults += 1

    return page_faults

# Input Handling
def main():
    pages = list(map(int, input("Enter reference string (space-separated): ").split()))
    frames = int(input("Enter number of frames: "))

    fifo_faults = fifo_page_replacement(pages, frames)
    lru_faults = lru_page_replacement(pages, frames)
    optimal_faults = optimal_page_replacement(pages, frames)

    print(f"FIFO Page Faults: {fifo_faults}")
    print(f"LRU Page Faults: {lru_faults}")
    print(f"Optimal Page Faults: {optimal_faults}")

    # Graphical Representation
    algorithms = ["FIFO", "LRU", "Optimal"]
    faults = [fifo_faults, lru_faults, optimal_faults]

    plt.bar(algorithms, faults, color=['blue', 'red', 'green'])
    plt.xlabel("Page Replacement Algorithms")
    plt.ylabel("Page Faults")
    plt.title("Page Replacement Performance")
    plt.show()

if __name__ == "__main__":
    main()

