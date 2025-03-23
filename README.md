# Efficient Page Replacement Simulator

A simulator for efficient page replacement algorithms in Operating Systems.

## Features
- Implements **FIFO (First-In-First-Out), LRU (Least Recently Used), and Optimal Page Replacement** algorithms.
- Simulates page replacement strategies to analyze page faults and performance.
- Provides easy-to-read outputs to understand memory management.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/CodeBy-Ayush/EfficientPageReplacementSimulator.git
   ```
2. Navigate to the project directory:
   ```bash
   cd EfficientPageReplacementSimulator
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the Python script and provide the required inputs:
```bash
python efficient_page_replacement.py
```
Example input and expected output:
```
Enter number of frames: 3
Enter reference string (space-separated): 7 0 1 2 0 3 4 2 3 0 3 2 1 2 0 1 7 0 1

Algorithm: FIFO
Page Faults: 12
```

## Algorithms Implemented
### 1. FIFO (First-In-First-Out)
- The oldest page in memory is replaced first.

### 2. LRU (Least Recently Used)
- The page that hasn't been used for the longest time is replaced.

### 3. Optimal Page Replacement
- The page that will not be used for the longest time in the future is replaced.

## Contributing
Feel free to contribute by submitting issues or pull requests.

## License
This project is licensed under the MIT License.

