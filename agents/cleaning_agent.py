import pandas as pd

# Handles dataset cleaning and preprocessing
class CleaningAgent:
    
    # Analyze missing values in the dataset
    def analyze_missing_values(self, dataframe):

        missing = dataframe.isnull().sum()

        missing = missing[missing > 0]

        report = pd.DataFrame({
            "Column": missing.index,
            "Missing Values": missing.values,
            "Missing Percentage": (
                missing.values / len(dataframe) * 100
            ).round(2)
        })

        return report