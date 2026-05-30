# 🏥 Hospital Patient Readmission Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.x-green)
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
- 🗃️ SQL
- 📊 Power BI


## 📁 Project Structure

    hospital-readmission/
    ├── data/
    │   ├── diabetic_data.csv        # Raw data
    │   └── cleaned_data.csv         # Cleaned data
    ├── notebooks/
    │   ├── 01_data_cleaning.ipynb   # Data Cleaning
    │   └── 02_EDA.ipynb             # Exploratory Data Analysis
    ├── sql/                         # SQL Queries
    ├── dashboard/                   # Power BI Dashboard
    └── README.md

## ✅ Project Phases
- [x] Phase 1 — Data Cleaning ✅
- [x] Phase 2 — Exploratory Data Analysis (EDA) ✅
- [ ] Phase 3 — SQL Analysis
- [ ] Phase 4 — Power BI Dashboard

## 💡 Key Findings

| Finding | Insight |
|---|---|
| 👴 Age Group | Patients aged 60-80 have the highest readmission rate |
| 🛏️ Early Discharge | Patients discharged early are more likely to return |
| 💊 Medications | Patients with more medicines have higher readmission risk |
| 🏥 Diagnoses | Patients with 5+ diagnoses are 2x more likely to be readmitted |
| ⚖️ Gender | Gender does not significantly impact readmission rate |

## 📈 EDA Charts
| Chart | Insight |
|---|---|
| Readmission Distribution | 11.2% patients high risk 🚨 |
| Age vs Readmission | 60-80 most affected |
| Gender vs Readmission | Almost equal |
| Time in Hospital | Early discharge = more risk |
| Medications | More meds = more risk |
| Diagnoses | More diagnoses = more risk |
| Correlation Heatmap | number_inpatient most correlated |

## 🚀 How to Run
```bash
# Clone the repo
git clone https://github.com/Balajimakkena/Hospital_Readmission.git

# Install libraries
pip install pandas numpy matplotlib seaborn

# Open notebooks
jupyter notebook
```

## 👨‍💻 Author
**Balaji**
 