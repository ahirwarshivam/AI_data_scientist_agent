import pandas as pd

# loading the data
class DatasetAgent:

    def load_dataset(self, uploaded_file):
        """Load the uploaded CSV file into a pandas DataFrame."""
        return pd.read_csv(uploaded_file)
    
# preview of the data set (whether the uploaded dataset is empty or not)
    def validate_dataset(self, dataframe):
        
        if dataframe.empty:
            raise ValueError("The uploaded dataset is empty.")

        return True

    
# dataset summary   
    def get_dataset_summary(self, dataframe):

        summary = {
            "rows": dataframe.shape[0],
            "columns": dataframe.shape[1],
            "missing_values": dataframe.isnull().sum().sum(),
            "duplicate_rows": dataframe.duplicated().sum(),
            "memory_usage": round(
                dataframe.memory_usage(deep=True).sum() / 1024,
                2
            )
        }

        return summary
    

# columns information of the dataset
    def get_column_information(self, dataframe):
    
        column_info = pd.DataFrame({
        "Column": dataframe.columns,
        "Data Type": dataframe.dtypes.astype(str),
        "Missing Values": dataframe.isnull().sum().values
    })
        return column_info

# Data quality informztion    
    def get_data_quality(self, dataframe):
        quality = {
        "missing_values": dataframe.isnull().sum().sum(),
        "duplicate_rows": dataframe.duplicated().sum(),
        "unique_columns": dataframe.columns.is_unique,
        "is_empty": dataframe.empty
    }
        return quality
        
    