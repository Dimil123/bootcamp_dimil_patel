**Handling Missing Values**

**fill_missing_median(df, column=None)**

Replaces missing values with the median of each numeric column.

If column is specified, applies only to that column.

Recommended when you want to preserve distribution and reduce sensitivity to outliers.

**drop_missing(df, columns=None, threshold=None)**

Drops rows with missing values.

If columns is provided, removes rows missing in those specific columns.

If threshold is set (e.g., 0.8), drops rows with fewer than 80% non-missing values.

Default behavior removes all rows with any missing values.

**Feature Normalization / Standardization**

normalize_data(df, columns=None, method='minmax')

Scales numerical columns to prepare for ML models.

Options:

method='minmax' → rescales values to the range [0,1].

method='standard' → applies z-score standardization (mean 0, variance 1).

Defaults to applying scaling on all numeric columns.

Uses scikit-learn’s MinMaxScaler and StandardScaler.
