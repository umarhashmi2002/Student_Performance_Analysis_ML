import streamlit as st
import nbformat
import matplotlib.pyplot as plt

# Function to read notebook file
def read_notebook(notebook_path):
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook_content = nbformat.read(f, as_version=4)
    return notebook_content

# Function to extract Matplotlib plots
def extract_graphs_and_charts(notebook):
    graphs_and_charts = []
    for cell in notebook.cells:
        if cell.cell_type == 'code':
            code = cell.source
            exec(code, globals())
            if 'plt' in globals():
                if plt.gcf().get_axes():
                    graphs_and_charts.append(plt.gcf())
                plt.close()
    return graphs_and_charts

# Streamlit UI
def main():
    st.title('Student Performance Analysis')

    st.sidebar.header('Navigation')
    page = st.sidebar.radio("Go to", ('Exploratory Data Analysis', 'Model Training'))

    if page == 'Exploratory Data Analysis':
        st.header('Exploratory Data Analysis')
        st.markdown("This section presents the exploratory data analysis (EDA) of student performance.")
        try:
            eda_notebook = read_notebook('D:\\OneDrive\\Desktop\\Ai_Project\\notebook\\1 . EDA STUDENT PERFORMANCE .ipynb')
            graphs_and_charts = extract_graphs_and_charts(eda_notebook)
            for item in graphs_and_charts:
                if isinstance(item, plt.Figure):
                    st.pyplot(item)
        except Exception as e:
            st.error(f"Error occurred: {e}")

    elif page == 'Model Training':
        st.header('Model Training Results')
        st.markdown("This section presents the results of model training.")
        try:
            model_notebook = read_notebook('D:\\OneDrive\\Desktop\\Ai_Project\\notebook\\2. MODEL TRAINING.ipynb')
            graphs_and_charts = extract_graphs_and_charts(model_notebook)
            for item in graphs_and_charts:
                if isinstance(item, plt.Figure):
                    st.pyplot(item)
        except Exception as e:
            st.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
