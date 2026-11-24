
# 🛒 E-Commerce Data Analysis & Big Data Processing

A Python-based Data Science project focused on generating, processing, and analysing e-commerce transaction data.

This project explores fundamental Data Science and Big Data concepts through hands-on implementation, including CSV data processing, sales analysis, data chunking, MapReduce simulation, and distributed storage simulation using Hadoop HDFS concepts.

The project uses **10,000 synthetic e-commerce transactions** to demonstrate how raw data can be transformed into meaningful business insights.

---

## 📌 Project Overview

E-commerce platforms generate massive amounts of transactional data every day. Analysing this data helps businesses understand sales performance, customer purchasing behaviour, and product profitability.

This project demonstrates how Python can be used to:

- Generate synthetic e-commerce transaction datasets.
- Read and process CSV files.
- Analyse sales and revenue.
- Identify popular products and payment methods.
- Divide large datasets into smaller chunks.
- Simulate the MapReduce processing approach.
- Understand distributed storage using HDFS concepts.
- Distribute data blocks across multiple DataNodes.
- Simulate block replication and DataNode failure.

---

## 🎯 Project Objectives

1. Generate 10,000 synthetic e-commerce transactions.
2. Perform basic data analysis using Python.
3. Calculate revenue and product performance metrics.
4. Understand Big Data processing fundamentals.
5. Implement data chunking using Python.
6. Simulate the Map and Reduce phases of MapReduce.
7. Understand Hadoop Distributed File System (HDFS).
8. Simulate block distribution across multiple DataNodes.
9. Understand block replication and fault tolerance.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| CSV Module | Reading and writing datasets |
| Random Module | Synthetic data generation |
| Dictionaries | Data aggregation and analysis |
| List Slicing | Dividing datasets into chunks |
| Enumerate | Tracking block positions |
| Tuples | Storing block IDs and data |
| VS Code | Development environment |
| GitHub | Version control and project hosting |

---

## 📂 Project Structure

```text
Ecommerce-Data-Analysis/
│
├── data/
│   └── transactions.csv
│
├── src/
│   ├── generate_data.py
│   ├── analyse_data.py
│   ├── distributed_analysis.py
│   └── hdfs_simulation.py
│
├── outputs/
│   ├── analysis_report.txt
│   └── distributed_analysis_report.txt
│
└── README.md
```

---

# 🚀 Activities Completed

## Activity 1: E-Commerce Transaction Data Analysis

Generated and analysed a synthetic dataset containing 10,000 e-commerce transactions.

### Features

- Generates random transaction records.
- Assigns customer IDs, products, quantities, and payment methods.
- Reads CSV data using Python.
- Calculates total transactions and revenue.
- Performs product-wise sales analysis.
- Identifies the most popular product.
- Identifies the highest revenue-generating product.
- Analyses payment method preferences.
- Calculates average transaction value.

### Key Metrics

- Total transactions.
- Total revenue.
- Total quantity sold.
- Product-wise quantity.
- Product-wise revenue.
- Most popular payment method.
- Percentage of UPI transactions.
- Average transaction value.

---

## Activity 2: Big Data Processing & MapReduce Simulation

Implemented a basic MapReduce workflow using Python to understand how large datasets can be divided and processed.

### 1. Data Chunking

- Reads the complete transaction dataset.
- Divides 10,000 transactions into smaller chunks.
- Uses a chunk size of 1,000 transactions.
- Creates 10 individual chunks.

### 2. Map Phase

Each chunk is processed independently to calculate:

- Number of transactions.
- Total revenue.
- Total quantity sold.

The results are stored in individual dictionaries.

### 3. Reduce Phase

Combines the intermediate results from all chunks to calculate:

- Grand total transactions.
- Grand total revenue.
- Grand total quantity sold.

### MapReduce Workflow

```text
       10,000 Transactions
                |
                v
        Divide into Chunks
                |
       +--------+--------+
       |        |        |
       v        v        v
     Chunk 1  Chunk 2  Chunk 3 ... Chunk 10
       |        |        |
       v        v        v
     MAP      MAP      MAP
       |        |        |
       +--------+--------+
                |
                v
              REDUCE
                |
                v
         Final Analysis
```

**Note:** This is a sequential Python simulation of the MapReduce workflow. It does not yet use actual distributed computers or parallel processing frameworks.

---

## Activity 3: Hadoop & HDFS Distributed Storage Simulation

Implemented a Python-based simulation to understand how Hadoop Distributed File System (HDFS) stores and manages large datasets across multiple DataNodes.

### 1. Data Block Creation

- Reads the 10,000 transaction dataset.
- Divides the dataset into smaller blocks.
- Uses a block size of 1,000 transactions.
- Creates 10 individual data blocks.
- Assigns a unique ID to each block.

### 2. DataNode Distribution

Simulated the distribution of data blocks across three DataNodes.

- Created three DataNodes.
- Distributed blocks using round-robin distribution.
- Used the modulo operator (%) to assign blocks.
- Preserved original block IDs using tuples.

### 3. Block Replication

Implemented a simplified replication-location simulation.

- Maintains a dictionary of block IDs and their replica locations.
- Records three DataNode locations for every block.
- Demonstrates the concept of replication factor 3.
- Helps understand data availability and redundancy.

### 4. DataNode Failure Simulation

Simulated the failure of a DataNode to understand fault tolerance.

- Simulates the failure of DataNode 1.
- Removes the failed DataNode from replica-location records.
- Checks the remaining available replica locations.
- Demonstrates how backup copies help maintain data availability.

### HDFS Workflow

```text
          10,000 Transactions
                   |
                   v
            Divide into Blocks
                   |
                   v
             10 Data Blocks
                   |
                   v
          Distribute Across Nodes
                   |
          +--------+--------+
          |        |        |
          v        v        v
       DataNode 1 DataNode 2 DataNode 3
          |        |        |
          +--------+--------+
                   |
                   v
             Block Replication
                   |
                   v
          Simulate Node Failure
                   |
                   v
          Check Available Replicas
```

### Concepts Demonstrated

- Hadoop architecture fundamentals.
- HDFS distributed storage.
- NameNode and DataNode roles.
- Data block distribution.
- Block replication.
- Replication factor.
- Fault tolerance.
- Data availability during node failure.

**Note:** This is a Python simulation of HDFS concepts. It does not run actual Hadoop or physically replicate data across multiple computers.

---

## 📊 Dataset Description

The project uses a synthetic dataset containing 10,000 transactions.

| Column | Description |
|---|---|
| Transaction_ID | Unique transaction identifier |
| Customer_ID | Customer identifier |
| Product | Purchased product |
| Quantity | Number of units purchased |
| Price | Price per unit |
| Payment_Method | Payment method used |

### Products Included

- Laptop
- Mobile
- Headphone
- Keyboard
- Mouse

### Payment Methods

- UPI
- Card
- Cash

---

## ⚙️ How to Run the Project

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Folder

```bash
cd Ecommerce-Data-Analysis
```

### Step 3: Generate Transaction Data

```bash
python src/generate_data.py
```

This generates the `transactions.csv` file inside the `data` folder.

### Step 4: Run Basic Data Analysis

```bash
python src/analyse_data.py
```

### Step 5: Run MapReduce Simulation

```bash
python src/distributed_analysis.py
```

This divides the transaction dataset into chunks, processes each chunk, and combines the results.

### Step 6: Run Hadoop & HDFS Simulation

```bash
python src/hdfs_simulation.py
```

This divides the dataset into blocks, distributes them across DataNodes, simulates replication, and demonstrates DataNode failure.

---

## 🧠 Concepts Learned

### Python Programming
- Python functions and loops.
- Lists, dictionaries, and tuples.
- File handling.
- CSV reading and writing.
- List slicing.
- Dictionary operations.
- Enumerate and modulo operator.

### Data Science
- Synthetic dataset generation.
- Data processing and aggregation.
- Revenue calculations.
- Product-wise analysis.
- Business insights from transactional data.

### Big Data
- Big Data processing fundamentals.
- Data chunking.
- MapReduce architecture.
- Map and Reduce phases.
- Hadoop architecture.
- HDFS distributed storage.
- NameNode and DataNode concepts.
- Block distribution and replication.
- Fault tolerance and data availability.

---

## 🔮 Future Improvements

- Implement data visualisation using Matplotlib.
- Generate automated analysis reports.
- Add error handling and data validation.
- Perform customer purchasing behaviour analysis.
- Explore actual Apache Hadoop and HDFS.
- Practise data processing using Apache Spark.
- Implement actual parallel processing.
- Explore Apache Hive for querying large datasets.

---

## 👨‍💻 Author

**Nakshatra Singh**

B.Tech – Information Technology

Aspiring AI Engineer | Python | Data Science | Machine Learning

---

*This project is part of my hands-on learning journey in Data Science, Big Data, and AI/ML.*

