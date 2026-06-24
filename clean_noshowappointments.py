import os
import pandas as pd

def run_data_integrity_pipeline(input_path, output_path):
    print("🚀 Starting Medical Appointments Data Integrity Engine...")
    
    # 1. Load the raw dataset
    if not os.path.exists(input_path):
        print(f"❌ Error: Raw file not found at {input_path}")
        return
    
    df = pd.read_csv(input_path)
    print(f"📊 Loaded baseline dataset with {len(df)} records.")
    
    # 2. Standardize column names (strip whitespace and lowercase)
    df.columns = df.columns.str.strip().str.lower()
    
    # 3. Initialize our tracking Audit Track column
    df['audit_age_flag'] = 'PASS'
    
    # 4. Define our strict logical age boundaries
    # Flags negative values and extreme outliers (> 110)
    outlier_mask = (df['age'] < 0) | (df['age'] > 110)
    
    # Apply the programmatic tracking flag
    df.loc[outlier_mask, 'audit_age_flag'] = 'FAIL_OUTLIER'
    
    # Count anomalies found
    anomaly_count = outlier_mask.sum()
    print(f"🔍 Audit Complete: Found {anomaly_count} records violating age boundaries.")
    
    # 5. Standardize other key categories (e.g., gender casing)
    if 'gender' in df.columns:
        df['gender'] = df['gender'].astype(str).str.upper().str.strip()
        
    # 6. Export the final high-integrity asset
    df.to_csv(output_path, index=False)
    print(f"💾 Production asset successfully exported to: {output_path}")
    print("✅ Pipeline execution complete.")

if __name__ == "__main__":
    # Define local repository structural paths
    INPUT_FILE = "noshowappointments_raw.csv"
    OUTPUT_FILE = "cleaned_noshowappointments.csv"
    
    run_data_integrity_pipeline(INPUT_FILE, OUTPUT_FILE)
