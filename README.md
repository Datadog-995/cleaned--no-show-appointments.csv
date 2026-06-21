# Medical Appointment No-Shows: Data Cleaning & Integrity Project

## 📌 Project Overview
This portfolio piece demonstrates an end-to-end data cleaning pipeline performed on a dataset of over 100,000 medical appointments. The goal of this project was to transform raw, messy operational data into a high-integrity, analytics-ready dataset to help determine the key drivers behind patient no-shows.

---

## 📊 Live Deliverable
* [**View the Cleaned Dataset in an Interactive Spreadsheet**](https://docs.google.com/spreadsheets/d/1w2FuaO9mIev--0tGGNVfgH5k_CKZejQj3LCvYHjfk0I/edit?gid=1674569316#gid=1674569316)

---

## 🛠️ Data Integrity & Auditing Workflow

To guarantee absolute accuracy, the dataset underwent a strict **Human-in-the-Loop** verification process using **Python (Pandas)** for programmatic cleaning and **OpenRefine** for a thorough structural audit.

### 1. OpenRefine Auditing & Faceting
* **Column Inspection:** Utilized text facets on categorical columns (e.g., `gender`, `neighbourhood`) to catch hidden trailing spaces, formatting inconsistencies, and spelling variations.
* **Numeric Auditing:** Evaluated the distribution of numeric fields using numeric facets to identify outliers and logical errors.
* **Integrity Validation:** Monitored the structural relationship between IDs to ensure no structural data loss occurred during formatting.

### 2. Programmatic Cleaning (Pandas)
* **Data Type Enforcement:** Converted identification numbers and dates into proper machine-readable formats.
* **Feature Engineering:** Developed custom script logic to create an `audit_age` verification tracker, isolating records with negative ages or unrealistic values.
* **Handling Missingness:** Standardized empty values and removed true duplicate records to establish a single source of truth.

---

## 📁 Repository Files
* `cleaned--no-show-appointments.csv`: The final, optimized CSV file.
* `README.md`: Project documentation and portfolio presentation.
