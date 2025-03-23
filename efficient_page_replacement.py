import matplotlib.pyplot as plt # Importing matplotlib library

# FIFO (First-In, First-out) page replacements Algo
def fifo_page_rep(pages, frame):
  #Initialize the variable count page fault
    page_fault = 0
    #store pages in memory
    queue = []
    
    for page in pages:
        if page not in queue:
            if len(queue) < frame:
                queue.append(page)
            else:
                queue.pop(0)
                queue.append(page)
            page_fault += 1  # count pages fault 

    return page_fault # return total no of page faults

# LRU (Least Recently Used) Algorithm
def lru_page_rep(pages, frame):
    page_fault = 0
    stack = []

    for page in pages:
        if page not in stack:
            if len(stack) < frame:
                stack.append(page)
            else:
                stack.pop(0)
                stack.append(page)
            page_fault += 1
        else:
            stack.remove(page)
            stack.append(page)

    return page_fault

# Optimal Page Replacement Algo
def optimal_page_rep(pages, frame):
    page_fault = 0
    memory = []

    for i, page in enumerate(pages):
        if page not in memory:
            if len(memory) < frame:
                memory.append(page)
            else:
                future_pages = pages[i+1:]
                indices = [future_pages.index(p) if p in future_pages else float('inf') for p in memory]
                memory.pop(indices.index(max(indices)))
                memory.append(page)
            page_fault += 1

    return page_fault

# Main Function to Handle User Input
def main():
    pages = list(map(int, input("Enter ref string (space-separated): ").split()))
    frame = int(input("Enter number of frame: "))

    fifo_fault = fifo_page_rep(pages, frame)
    lru_fault = lru_page_rep(pages, frame)
    optimal_fault = optimal_page_rep(pages, frame)

    print(f"FIFO Page Faults: {fifo_fault}")
    print(f"LRU Page Faults: {lru_fault}")
    print(f"Optimal Page Faults: {optimal_fault}")

    # Graphical Representation
    algorithms = ["FIFO", "LRU", "Optimal"]
    fault = [fifo_fault, lru_fault, optimal_fault]

    plt.bar(algorithms, fault, color=['blue', 'red', 'green'])
    plt.xlabel("Page Replacement Algorithms")
    plt.ylabel("Page Faults")
    plt.title("Page Replacement Performance")
    plt.show()

if __name__ == "__main__":
    main()
