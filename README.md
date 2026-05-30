# 🏥 Hospital Patient Readmission Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue)
![PySpark](https://img.shields.io/badge/PySpark-3.x-orange)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
![Status](https://img.shields.io/badge/Status-In%20Progress-orange)

## 📌 Problem Statement
Hospitals lose millions and patients suffer when they are 
readmitted within 30 days of discharge. This project identifies 
key risk factors that lead to readmission using real-world 
patient data from 130 US hospitals.

## 📊 Dataset
| Detail | Info |
|---|---|
| Source | UCI ML Repository |
| Name | Diabetes 130-US Hospitals (1999-2008) |
| Rows | 101,766 patients |
| Columns | 50 features |

🔗 [Download Dataset](https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008)

## 🛠️ Tools Used
- 🐍 Python (Pandas, NumPy, Matplotlib, Seaborn)
- ⚡ PySpark (SQL Analysis)
- 📊 Power BI (Dashboard)
- ☁️ Databricks Community Edition

## 📁 Project Structure

    hospital-readmission/
    ├── data/
    │   ├── diabetic_data.csv            # Raw data
    │   └── cleaned_data.csv             # Cleaned data
    ├── notebooks/
    │   ├── 01_data_cleaning.ipynb       # Data Cleaning
    │   ├── 02_EDA.ipynb                 # Exploratory Data Analysis
    │   └── 03_PySpark_Analysis.ipynb    # PySpark SQL Analysis
    ├── dashboard/                        # Power BI Dashboard
    └── README.md

## ✅ Project Phases
- [x] Phase 1 — Data Cleaning ✅
- [x] Phase 2 — Exploratory Data Analysis (EDA) ✅
- [x] Phase 3 — PySpark SQL Analysis ✅
- [ ] Phase 4 — Power BI Dashboard 🔄

## 💡 Key Findings
| Finding | Insight |
|---|---|
| 👴 Age Group | Patients aged 20-30 have highest readmission rate (14.24%) |
| ⚖️ Gender | Gender does not significantly impact readmission rate |
| 🛏️ Hospital Stay | Readmitted patients stayed avg 4.77 days |
| 💊 Medications | Readmitted patients took avg 16.9 medications |
| 🏥 Diagnoses | Patients with 16 diagnoses are at extreme risk |
| 🚨 High Risk | V58 diagnosis has 41.67% readmission rate |

## 📈 EDA Charts
| Chart | Insight |
|---|---|
| Readmission Distribution | 11.2% patients high risk 🚨 |
| Age vs Readmission | 20-30 age group most affected |
| Gender vs Readmission | Almost equal (11.25% vs 11.06%) |
| Time in Hospital | Early discharge = more risk |
| Medications | More meds = more risk |
| Diagnoses | More diagnoses = more risk |
| Correlation Heatmap | number_inpatient most correlated |

## 🔍 PySpark SQL Analysis
| Query | Result |
|---|---|
| Age vs Readmission | [20-30) → 14.24% Highest 🚨 |
| Gender vs Readmission | Female 11.25% vs Male 11.06% |
| Avg Hospital Stay | Readmitted → 4.77 days |
| Top High Risk Diagnosis | V58 → 41.67% readmission 🚨 |
| High Risk Patients | 16 diseases + 57 medications 😮 |

## 🚀 How to Run

    # Clone the repo
    git clone https://github.com/balajimakkena/hospital-readmission.git

    # Install libraries
    pip install pandas numpy matplotlib seaborn pyspark

    # Open notebooks
    jupyter notebook

## 👨‍💻 Author
**Balaji**
 