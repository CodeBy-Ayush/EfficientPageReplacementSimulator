# Efficient Page Replacement Algorithm Simulator

## 📌 About the Project
This project implements **three page replacement algorithms**:
- **FIFO (First In First Out)**
- **LRU (Least Recently Used)**
- **Optimal Page Replacement**

It helps users understand how different memory management techniques perform by computing **total page faults** and visualizing the results using **Google Colab**.

---
## ⚙️ Features
✅ Implements **FIFO, LRU, and Optimal** algorithms  
✅ Accepts **user input for frames and page references**  
✅ Calculates **total page faults** for each algorithm  
✅ Generates **visualization using Python Matplotlib**  
✅ Runs directly on **Google Colab (No Local Installation Needed!)**  
✅ Well-structured **GitHub commits for version control**  

---
## 🔧 How to Run the Code on Google Colab
### **1️⃣ Open Google Colab and Create a New Notebook**
1. Open [Google Colab](https://colab.research.google.com/)
2. Click on **New Notebook**

### **2️⃣ Install Required Python Libraries**
In the first cell, run this command to install dependencies:
```python
!pip install matplotlib numpy
```

### **3️⃣ Copy and Paste the Python Code**
- Copy the **Python script** from [page_replacement.py](page_replacement.py)
- Paste it into a new code cell in Google Colab
- Run the cell

### **4️⃣ Enter User Input When Prompted**
- **Example Input:**
  ```
  Enter the page reference string (space-separated): 7 0 1 2 0 3 0 4 2 3 0 3 2
  Enter the number of frames: 3
  ```
- **Example Output:**
  json
  ```
  FIFO Page Faults: 10
  LRU Page Faults: 9
  Optimal Page Faults: 7
  ```

### **5️⃣ View the Graphical Output**
After execution, Google Colab will generate a **bar chart** comparing the algorithms' performance.

---
## 📊 Example Visualization Output
📊 **Page Replacement Algorithm Comparison**
- 🔴 FIFO: **10 Page Faults**  
- 🔵 LRU: **9 Page Faults**  
- 🟢 Optimal: **7 Page Faults**  

📌 **This graph helps visualize which algorithm is more efficient based on page faults.**  


---
## 📜 License  
This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---
## 🚀 Author  
👤 **Ayush Kumar**

