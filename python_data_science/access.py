import os
import streamlit as st
import pandas as pd
import fsspec
import duckdb
import time
# Assume `RP` is a variable that holds a path segment specific to the execution context
fs = fsspec.filesystem("")
#RP = "RP1"

# Construct the directory path using `../{RP}`
#directory_path = os.path.join(os.path.dirname(__file__), RP)
#directory_path = os.path.join(os.path.dirname(__file__), "..", RP)
# Access files within the directory
#data_files = os.listdir(directory_path)
#for file in data_files:
    # Perform operations on each file
   # print(file)

with st.sidebar:
        st.title("Mapping Tool")
        progress_or_map = st.selectbox('Research Project', ['Map Studies', 'Progress Monitor'])
        avail_studies = []
        RP = st.selectbox('Research Project', ['RP1', 'RP2'])
        avail_studies = [f for f in fs.ls(f"/{RP}/") if fs.isdir(f)]
        avail_studies = [f.split('/')[-1] for f in avail_studies if f.split('/')[-1][0] != '.']
        study = st.selectbox('Study', avail_studies)
        tables = [f for f in fs.glob(f"../{RP}/{study}/metadata/recommendations_by_table/*_variables_with_recommendations_with_datetimeid.csv")]
        tables = [x.split('/')[-1].split('_variables_with_recommendations_with_datetimeid.csv')[0] for x in tables]
        table = st.selectbox('Table', tables)
        st.divider()
        variables_status = st.selectbox('View variables:',mapping_options)
        st.divider()
        col1, col2= st.columns(2)
        with col1:
            show_about = st.checkbox("About",value = True, help = 'Show an about section for the dataset you have selected. Hiding this can make the mapping process faster as you will not need to scroll up and down to submit')
        with col2:
            original_order = st.checkbox('Unsort', value  = True, disabled = True, help = 'Show variables in the original order of incoming datasets')
        st.divider()
        st.write('Please ensure the mapping process is undertaken whilst consulting synthetic data and study documents available from: https://web.csag.uct.ac.za/hub/hub/user-redirect/lab/tree/heat_center/data/health_open/ as well as the target codebook at https://app.box.com/file/1267505872263?s=cydg74tfdltgzxhg3by3goy550j3j022')
        st.write('Contact peter.marsh@uct.ac.za if the above link does not work.')

    
   # results_file = f'results/{RP}/{study}/{table}.csv'
    #input_path = f"../{RP}/{study}"


    
    
print("finished")
