**data/raw/ :** To Store csv files

**data/processed/ :** To Store parquet/pq files (efficient data management)

**Format used:**

Age : Float : expecting till 1 decimal

Income : Numeric : check differnet methode/ float can be used

Date : Datetime64 : convinient to manage dates with this type

**How the Code Reads and Writes Data**

It is designed to be flexible and robust in handling data I/O:

Environment Variables: The paths to the raw and processed data directories are configured using environment variables (DATA_DIR_RAW and PROCESS_DIR_RAW). If these are not set, the code falls back to default paths (data/raw and data/processed respectively), making the script portable and easy to configure.

Utility Functions: The notebook defines helper functions, write_df and read_df, to manage file operations. These functions automatically detect the desired file format (CSV or Parquet) based on the file extension of the provided path. This abstraction simplifies the code and removes the need to call specific pd.to_csv or pd.to_parquet functions in the main logic.
