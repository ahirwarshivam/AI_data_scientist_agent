import streamlit as st
from agents.dataset_agent import DatasetAgent

st.title("Upload Dataset")
st.write("Upload a CSV dataset to begin the analysis.")

uploaded_file = st.file_uploader(
    "Choose a CSV file",
    type=["csv"]
)

if uploaded_file is not None:

    agent = DatasetAgent()

    dataframe = agent.load_dataset(uploaded_file)

    agent.validate_dataset(dataframe)

    st.session_state["dataset"] = dataframe

    st.success("Dataset uploaded successfully.")

    
# summary of the data set
    summary = agent.get_dataset_summary(dataframe)
    st.subheader("Dataset Summary")
    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Rows", summary["rows"])
    col2.metric("Columns", summary["columns"])
    col3.metric("Missing Values", summary["missing_values"])
    col4.metric("Duplicate Rows", summary["duplicate_rows"])
    col5.metric("Memory (KB)", summary["memory_usage"])

    column_info = agent.get_column_information(dataframe)

    st.subheader("Column Information")
    st.dataframe(column_info, use_container_width=True)


# Quality report
    quality = agent.get_data_quality(dataframe)
    #st.write(quality)


    st.subheader("Data Quality Report")
    st.success("Dataset loaded successfully.")

    if quality["missing_values"] == 0:
        st.success("No missing values found.")
    else:
        st.warning(f'{quality["missing_values"]} missing values detected.')

    if quality["duplicate_rows"] == 0:
        st.success("No duplicate rows found.")
    else:
        st.warning(f'{quality["duplicate_rows"]} duplicate rows detected.')

    if quality["unique_columns"]:
        st.success("All column names are unique.")
    else:
        st.error("Duplicate column names detected.")

    st.info(
        f"Numerical Columns: {quality['numerical_columns']} | "
        f"Categorical Columns: {quality['categorical_columns']}"
    )

    if quality["missing_values"] == 0 and quality["duplicate_rows"] == 0:
        st.success("Dataset is ready for preprocessing.")
    else:
        st.warning("Cleaning is recommended before preprocessing.")

# preview of the dataset
    st.subheader("Dataset Preview")
    st.dataframe(dataframe.head())
    
