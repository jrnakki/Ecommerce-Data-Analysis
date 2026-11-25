

# 🛒 E-Commerce Data Analysis & Big Data Processing

A Python-based Data Science project focused on generating, processing, analysing, and mining e-commerce transaction data.

This project explores practical Data Science and Big Data concepts through hands-on implementation, including CSV data processing, sales analysis, data chunking, MapReduce simulation, Hadoop and HDFS simulation, and customer behaviour analysis.

The project uses **10,000 synthetic e-commerce transactions** to demonstrate how raw transaction data can be transformed into meaningful business insights.

---

## 📌 Project Overview

The main objective of this project is to understand how data is generated, stored, processed, analysed, and interpreted in real-world Data Science workflows.

The project is divided into multiple practical activities:

1. Big Data Fundamentals – E-commerce Data Generation & Analysis
2. Distributed Processing – Chunking & MapReduce Simulation
3. Hadoop & HDFS – Distributed Storage Simulation
4. Apache Hive & Spark – SQL and Big Data Processing Concepts *(practical implementation in progress)*
5. Data Mining – Customer Spending, Product Patterns & Business Insights

---

## 🎯 Project Objectives

- Generate and analyse large synthetic transaction datasets.
- Understand CSV data processing using Python.
- Perform product-wise and customer-wise analysis.
- Understand data chunking and MapReduce concepts.
- Simulate distributed storage using Hadoop and HDFS concepts.
- Discover customer purchasing patterns.
- Identify high-value customers.
- Analyse payment method preferences.
- Generate meaningful business insights from raw data.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| CSV Module | Reading and processing transaction data |
| Dictionaries & Lists | Data storage and aggregation |
| SQL | Learning structured data queries |
| Hadoop Concepts | Understanding distributed storage |
| HDFS Concepts | Simulating block distribution and replication |
| MapReduce | Simulating distributed data processing |
| Git & GitHub | Version control and project management |

---

## 📁 Project Structure

```text
Ecommerce-Data-Analysis/
│
├── data/
│   └── transactions.csv
│
├── outputs/
│   ├── analysis_report.txt
│   ├── data_mining_report.txt
│   ├── distributed_analysis_report.txt
│   └── hdfs_simulation_output.txt
│
├── src/
│   ├── generate_data.py
│   ├── analyse_data.py
│   ├── distributed_analysis.py
│   ├── hdfs_simulation.py
│   └── data_mining.py
│
└── README.md
```

### Folder Description

- **data/** – Contains the generated e-commerce transaction dataset.
- **outputs/** – Contains reports and outputs from the practical activities.
- **src/** – Contains Python source code for data generation, analysis, processing, and simulation.
- **README.md** – Project documentation.

---

# 🚀 Practical Activities

## Activity 1 – Big Data Fundamentals: E-Commerce Data Generation & Analysis

**Objective:** Generate and analyse a dataset containing 10,000 e-commerce transactions.

### Dataset Generation

Created a synthetic e-commerce dataset using Python's `random` and `csv` modules.

The dataset contains the following fields:

| Column | Description |
|---|---|
| Transaction_ID | Unique transaction identifier |
| Customer_ID | Customer identifier |
| Product | Purchased product |
| Quantity | Number of units purchased |
| Price | Price per unit |
| Payment_Method | UPI, Card, or Cash |

### Products Included

- Laptop
- Mobile
- Headphone
- Keyboard
- Mouse

### Analysis Performed

- Total number of transactions
- Total revenue
- Total quantity sold
- Product-wise sales analysis
- Product-wise revenue analysis
- Most and least popular products
- Payment method analysis
- Average transaction value
- Payment method percentages

### Concepts Learned

- CSV file handling
- `csv.writer()`
- `csv.DictReader()`
- Python dictionaries
- Loops and conditional statements
- Data aggregation
- Basic statistical analysis

---

## Activity 2 – Distributed Data Processing: MapReduce Simulation

**Objective:** Understand how large datasets can be divided into smaller chunks and processed independently.

Implemented a simplified MapReduce workflow using Python.

### Implementation

**1. Data Reading**

Read the 10,000 transactions from the CSV dataset.

**2. Data Chunking**

Divided the dataset into 10 chunks, each containing 1,000 transactions.

**3. Map Phase**

Each chunk was processed independently to calculate:

- Number of transactions
- Total revenue
- Total quantity sold

**4. Reduce Phase**

Combined the results from all chunks to calculate the final totals.

### Processing Workflow

```text
       10,000 Transactions
                |
                v
          Data Chunking
                |
       ---------------------
       |         |         |
       v         v         v
    Chunk 1   Chunk 2   Chunk 3 ... Chunk 10
       |         |         |
       v         v         v
    Mapping   Mapping   Mapping
       |         |         |
       ---------------------
                |
                v
           Reduce Phase
                |
                v
          Final Analysis
```

### Concepts Learned

- Big Data processing
- Data partitioning
- Chunk-based processing
- MapReduce architecture
- Aggregation of intermediate results

**Note:** This is a sequential Python simulation of MapReduce. It demonstrates the processing logic but does not perform actual parallel or distributed execution.

---

## Activity 3 – Hadoop & HDFS: Distributed Storage Simulation

**Objective:** Understand how Hadoop Distributed File System (HDFS) stores large datasets using blocks and multiple DataNodes.

Implemented a simplified HDFS storage simulation using Python.

### Implementation

**1. Block Creation**

- Divided 10,000 transactions into 10 blocks.
- Each block contains 1,000 transactions.

**2. Block Distribution**

Distributed blocks across three simulated DataNodes:

- DataNode 1
- DataNode 2
- DataNode 3

Used round-robin distribution to assign blocks.

**3. Block Identification**

Assigned unique IDs to blocks, such as:

- Block 1
- Block 2
- Block 3

**4. Replication Simulation**

Created a dictionary to represent the locations of each block across three DataNodes.

**5. DataNode Failure Simulation**

Simulated the failure of a DataNode by removing its location from the replica-location records.

### HDFS Simulation Workflow

```text
          Transaction Dataset
                   |
                   v
             Block Creation
                   |
          -------------------
          |        |        |
          v        v        v
       Block 1  Block 2  Block 3 ...
          |        |        |
          v        v        v
      DataNode 1 DataNode 2 DataNode 3
          |        |        |
          -------------------
                   |
                   v
          Replica Location Records
                   |
                   v
          DataNode Failure Simulation
```

### Concepts Learned

- Hadoop architecture
- HDFS
- NameNode and DataNode concepts
- Data blocks
- Block distribution
- Replication
- Fault tolerance

**Note:** This is a Python-based conceptual simulation. It tracks block locations but does not physically replicate data or run an actual Hadoop cluster.

---

## Activity 4 – Apache Hive & Spark

**Objective:** Learn how large datasets can be queried and processed using Big Data technologies.

### Concepts Explored

**Apache Hive**
- Data warehousing concepts
- SQL-like query language (HiveQL)
- Structured data querying
- Grouping and aggregation

**Apache Spark**
- Distributed data processing
- Large-scale data processing concepts
- Batch processing
- Comparison between traditional Python processing and Spark

**Status:** Learning and practical implementation in progress.

---

## Activity 5 – Data Mining: Customer Behaviour & Business Insights

**Objective:** Discover useful patterns, customer behaviour, and business insights from the e-commerce transaction dataset.

Implemented a data mining program using Python dictionaries, loops, functions, and aggregation techniques.

### 1. Product Purchase Pattern Analysis

Calculated the total units sold for each product.

Products analysed:
- Laptop
- Mobile
- Headphone
- Keyboard
- Mouse

Identified:
- Highest-selling product
- Lowest-selling product
- Product-wise sales percentages

### 2. Customer Spending Analysis

Calculated the total spending of individual customers.

Implemented:
- Customer-wise spending aggregation
- Highest-spending customer identification
- Lowest-spending customer identification
- Average customer spending

### 3. High-Value Customer Identification

Identified customers whose total spending exceeded ₹5,00,000.

Calculated:
- Number of high-value customers
- Total spending by high-value customers
- Their contribution to overall revenue

### 4. Payment Method Analysis

Analysed the distribution of payment methods:

- UPI
- Card
- Cash

Calculated transaction counts and percentage contributions for each payment method.

### 5. Business Insights

Generated a final report containing:

- Most-selling product and units sold
- Least-selling product and units sold
- Most-used payment method
- Highest-spending customer
- Number of high-value customers
- Total revenue from high-value customers
- High-value customer contribution to total revenue

### Example Business Findings

One sample analysis identified:

- Headphones as the highest-selling product.
- Laptop as the lowest-selling product.
- Cash as the most-used payment method.
- High-value customers as an important contributor to total revenue.

*Exact results may vary when a new random dataset is generated.*

### Concepts Learned

- Data mining fundamentals
- Customer segmentation
- Customer spending analysis
- Product sales analysis
- Dictionary-based aggregation
- Maximum and minimum value identification
- Percentage calculations
- Business insight generation
- Report generation

---

# 📊 Key Learning Outcomes

Through this project, I gained practical experience with:

| Area | Skills Developed |
|---|---|
| Python Programming | Functions, loops, dictionaries, lists |
| Data Handling | CSV reading and writing |
| Data Analysis | Revenue, sales and customer analysis |
| Big Data | Chunking and MapReduce concepts |
| Distributed Storage | HDFS block distribution simulation |
| Data Mining | Customer behaviour and purchasing patterns |
| SQL | Basic queries and aggregation |
| Problem Solving | Breaking large tasks into smaller functions |
| GitHub | Project organisation and documentation |

---

# ▶️ How to Run the Project

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project

```bash
cd Ecommerce-Data-Analysis
```

### 3. Generate the Dataset

```bash
python src/generate_data.py
```

### 4. Run Activity 1 – Data Analysis

```bash
python src/analyse_data.py
```

### 5. Run Activity 2 – MapReduce Simulation

```bash
python src/distributed_analysis.py
```

### 6. Run Activity 3 – HDFS Simulation

```bash
python src/hdfs_simulation.py
```

### 7. Run Activity 5 – Data Mining

```bash
python src/data_mining.py
```

**Requirements:** Python 3.x. The implemented Python activities use standard-library modules, so no external Python packages are currently required.

---

# ⚠️ Dataset Limitations

- The dataset contains synthetic, randomly generated transactions.
- It is intended for educational and practical learning purposes.
- It does not represent actual e-commerce business transactions.
- Analysis results can change when the dataset is regenerated.
- Hadoop, HDFS, and MapReduce activities are conceptual Python simulations, not production distributed systems.

---

# 🔮 Future Improvements

- Implement actual Apache Hive queries.
- Perform distributed data processing using PySpark.
- Add data visualisations using Matplotlib.
- Implement customer segmentation using Machine Learning.
- Add predictive sales analysis.
- Build an interactive dashboard using Streamlit.
- Improve report generation by automatically saving analysis results to text files.

---

# 👨‍💻 Author

**B.Tech – Information Technology Student**

Interested in:
- Data Science
- Artificial Intelligence
- Machine Learning
- Big Data Technologies
- Python Development

This project is part of my hands-on learning journey towards becoming an **AI Engineer**.

---

⭐ If you find this project useful, feel free to explore the repository!

