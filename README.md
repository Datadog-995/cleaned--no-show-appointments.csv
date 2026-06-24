# Medical Appointment No-Shows: Data Cleaning & Integrity Project

## 📌 Project Overview
This portfolio piece demonstrates an end-to-end data cleaning pipeline performed on a dataset of over 100,000 medical appointments. The goal of this project was to transform raw, messy operational data into a high-integrity, analytics-ready dataset to help determine the key drivers behind patient no-shows.
## 🔄 Data Transformation (Before vs. After)

To illustrate the cleaning depth, here is a snapshot of how the raw operational data was structured versus its final, high-integrity state:

### ❌ Raw "Dirty" Dataset Sample
| PatientId | AppointmentID | Gender | ScheduledDay | Age | Neighbourhood | No-show |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2.31E+11 | 5642903 | F   | 2016-04-29T16:08:27Z | -1 |  JARDIM CAMBURI | No |
| 44452185 | 5642494 | M | 2016-04-29T14:43:56Z | 62 | JARDIM CAMBURI  | no |
| 9.92E+13 | 5514122 | f | 2016-04-29T07:13:31Z | 115 | MARIA ORTIZ | YES |

###  Final Cleaned Dataset Sample
| Patient ID | Appointment ID | Gender | Scheduled Date | Age | Audit Age Tracker | Neighborhood | No-Show |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 231421000000 | 5642903 | Female | 2016-04-29 | 0 | Flagged (Negative Age) | Jardim Camburi | No |
| 000444521852 | 5642494 | Male | 2016-04-29 | 62 | Verified | Jardim Camburi | No |
| 992415000000 | 5514122 | Female | 2016-04-29 | 115 | Flagged (Review >100) | Maria Ortiz | Yes |

*Key Transformations Shown: Standardized ID notation, uniform text casing, stripped whitespace, normalized date strings, corrected Boolean logic (Yes/No), and initialized the structural anomaly tracker (`audit_age`).*
-----

## 🛠️ Data Integrity & Auditing Workflow

To guarantee absolute accuracy, the dataset underwent a strict verification process using **Python (Pandas)** for programmatic cleaning and **OpenRefine** for a thorough structural audit.

### 1. OpenRefine Auditing & Faceting
* **Column Inspection:** Utilized text facets on categorical columns to catch hidden trailing spaces, formatting inconsistencies, and spelling variations.
* **Numeric Auditing:** Evaluated the distribution of numeric fields using numeric facets to identify outliers and logical errors.
* **Integrity Validation:** Monitored the structural relationship between IDs to ensure no structural data loss occurred during formatting.

### 2. Programmatic Cleaning (Pandas)
* **Data Type Enforcement:** Converted identification numbers and dates into proper machine-readable formats.
* **Feature Engineering:** Developed custom script logic to create an `audit_age` verification tracker, isolating records with negative ages or unrealistic values.

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
---

## 🗺️ Project Navigation Roadmap
For freelance clients and technical reviewers, here is the recommended sequence to navigate this data integrity audit:
