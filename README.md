# Efficient Page Replacement Algorithm Simulator

A Streamlit-based web application that simulates and compares different page replacement algorithms used in operating systems. This tool helps visualize and understand how different page replacement strategies work in memory management.

## 🚀 Features

- **Interactive Web Interface**: Built with Streamlit for an intuitive user experience
- **Multiple Algorithms**: Simulates three popular page replacement algorithms:
  - First-In-First-Out (FIFO)
  - Least Recently Used (LRU)
  - Optimal Page Replacement
- **Real-time Visualization**: 
  - Bar charts comparing page faults
  - Pie charts showing hit ratios
  - Detailed step-by-step execution tables
- **Customizable Parameters**:
  - Adjustable number of memory frames
  - Custom reference string input
  - Algorithm selection

## 🛠️ Prerequisites

- Python 3.x
- pip (Python package installer)

## 📦 Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd <repository-directory>
```

2. Install the required packages:
```bash
pip install streamlit pandas numpy matplotlib
```

## 💻 Usage

1. Run the application:
```bash
streamlit run filename.py
```

2. The web interface will open in your default browser. You can then:
   - Enter a reference string (space-separated numbers)
   - Select the number of memory frames
   - Choose which algorithms to simulate
   - Click "🚀 Run Simulation" to see the results

## 📝 Example Inputs & Outputs

### Input Example:
```
Enter the page reference string (space-separated): 7 0 1 2 0 3 0 4 2 3 0 3 2
Enter the number of frames: 3
Select algorithms: FIFO, LRU, Optimal
```

### Output Example:
The application will display:
- A table with the number of page faults and hit ratios for each algorithm
- Bar charts comparing the page faults for each algorithm
- Pie charts comparing the hit ratios for each algorithm
- Step-by-step details of how each algorithm managed the page references

## 🔍 How It Works

### FIFO (First In, First Out)
This algorithm replaces the oldest page in memory when a page fault occurs.

### LRU (Least Recently Used)
This algorithm replaces the page that has not been used for the longest time.

### Optimal Algorithm
This algorithm replaces the page that will not be used for the longest period in the future.

### Algorithm Logic
- **Page Hits**: When a page is already in memory (cache), it counts as a page hit.
- **Page Faults**: When a page is not in memory, it counts as a page fault. The algorithm replaces the least recently or optimally selected page.

## 📊 Visualization

The simulator generates visualizations to help you compare the performance of each algorithm:

- **Bar Chart**: Displays the total number of page faults for each algorithm
- **Pie Chart**: Shows the hit ratio distribution across the selected algorithms
- **Detailed Steps**: Provides a detailed view of the state of memory for each page reference, indicating whether the page was a hit or miss

## 💡 Algorithm Insights

- **FIFO**: Replaces the oldest page in memory when a page fault occurs
- **LRU**: Replaces the least recently used page
- **Optimal**: Replaces the page that won't be used for the longest time in the future

## 🤝 Contributing

Feel free to open issues, contribute code, or suggest improvements!

## 📱 Contact & Support

If you need help or have any questions, feel free to reach out via GitHub or email.

## 📝 License

This project is open source and available under the MIT License. 

## 👀 Screenshots

*(Include your screenshots here)*

### Application Interface
*(Add your application interface screenshot)*

### Output Graphs
*(Add your output graphs screenshots)* 
