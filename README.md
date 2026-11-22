# 🛒 E-Commerce Data Analysis & Big Data Processing

A Python-based Data Science project focused on generating, processing, and analysing e-commerce transaction data.

This project explores fundamental Data Science and Big Data concepts through hands-on implementation, including CSV data processing, sales analysis, data chunking, and MapReduce simulation.

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
- Combine intermediate results into a final analysis.

---

## 🎯 Project Objectives

1. Generate 10,000 synthetic e-commerce transactions.
2. Perform basic data analysis using Python.
3. Calculate revenue and product performance metrics.
4. Understand Big Data processing fundamentals.
5. Implement data chunking using Python.
6. Simulate the Map and Reduce phases of MapReduce.

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| CSV Module | Reading and writing datasets |
| Random Module | Synthetic data generation |
| Dictionaries | Data aggregation and analysis |
| List Slicing | Dividing datasets into chunks |
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
│   └── distributed_analysis.py
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

---

## 🧠 Concepts Learned

- Python functions and loops.
- Lists and dictionaries.
- File handling.
- CSV reading and writing.
- Data processing and aggregation.
- Synthetic dataset generation.
- Data chunking and list slicing.
- MapReduce architecture fundamentals.
- Map and Reduce phases.
- Basic Big Data processing concepts.
- GitHub project management.

---

## 🔮 Future Improvements

- Implement data visualisation using Matplotlib.
- Generate automated analysis reports.
- Add error handling and data validation.
- Perform customer purchasing behaviour analysis.
- Explore Apache Hadoop and HDFS.
- Practise data processing using Apache Spark.
- Implement actual parallel processing.

---

## 👨‍💻 Author

**Nakshatra Singh**

B.Tech – Information Technology

Aspiring AI Engineer | Python | Data Science | Machine Learning

---

*This project is part of my hands-on learning journey in Data Science, Big Data, and AI/ML.*
