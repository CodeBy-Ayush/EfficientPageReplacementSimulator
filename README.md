# 📌 Page Replacement Algorithm Simulator

A powerful Streamlit-based web application designed to simulate and compare different page replacement algorithms used in operating systems. This tool provides an interactive and visual approach to understanding how memory management techniques work.

---

## 🚀 Features

✅ **User-Friendly Web Interface**: Built with Streamlit for smooth interactivity.
✅ **Supports Multiple Algorithms**: Simulates three popular page replacement algorithms:
  🟢 First-In-First-Out (FIFO)
🔵 Least Recently Used (LRU)
🟠 Optimal Page Replacement

✅ Real-Time Visualizations:
📊 Bar Charts – Compare page faults across algorithms at a glance
🎯 Pie Charts – Visualize hit ratio distribution for better insights
📄 Step-by-Step Execution Logs – Track algorithm behavior in real time

✅ Customizable Simulation Parameters:
⚙️ Adjustable Memory Frame Size – Fine-tune simulations for different scenarios
📜 User-Defined Reference String – Test with custom input patterns
✅ Selective Algorithm Execution – Run one or multiple algorithms as needed

🚀 Experience a powerful and interactive page replacement simulator!

---

## 📌 Prerequisites

Ensure you have the following installed before running the application:

- 🐍 Python 3.x
- 📦 pip (Python package installer)

---

## 📥 Installation Guide

Follow these steps to set up and run the simulator:

1️⃣ **Clone this repository:**
```bash
git clone <repository-url>
cd <repository-directory>
```

2️⃣ **Install required dependencies:**
```bash
pip install streamlit pandas numpy matplotlib
```

---

## 🖥️ Running the Application

Launch the application using the following command:
```bash
streamlit run filename.py
```

This will open the simulator in your default web browser. Now, you can:
- 🔢 Enter a page reference string
- 📏 Set the number of memory frames
- 🛠️ Select which algorithms to simulate
- 🚀 Click "Run Simulation" to view results

---

## 🔎 Example Inputs & Outputs

### 🎯 Example Input:
```
Reference String: 7 0 1 2 0 3 0 4 2 3 0 3 2
Number of Frames: 3
Selected Algorithms: FIFO, LRU, Optimal
```

### 📊 Example Output:
The application will display:
- 📋 A summary table with page faults and hit ratios for each algorithm.
- 📊 Bar chart comparing page faults across different algorithms.
- 🎯 Pie chart illustrating hit ratio distribution.
- 📝 A step-by-step breakdown of page replacements.

---

## 📜 License

This project is open-source and available under the MIT License. Feel free to contribute and enhance its capabilities!

---

## 🤝 Contributing

We welcome contributions! If you’d like to improve this simulator, follow these steps:

1️⃣ Fork the repository
2️⃣ Create a new branch for your feature
3️⃣ Commit your changes
4️⃣ Submit a pull request

---

## 📧 Contact

For queries, suggestions, or contributions, reach out via email or open an issue in the repository.

Happy Coding! 🎉🚀

