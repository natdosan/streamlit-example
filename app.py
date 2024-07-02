import altair as alt
import pandas as pd
import streamlit as st

initial_user_data = {
    'patient_id': ['UCSD', 'NYU', 'Columbia', 'UCSD', 'NYU', 'UCSD'],
    'fetal_fraction_percent': [4, 13, 5, 8, 9, 20],
    'difference_biorad_nipt': [12.1, 8.5, 4.5, 4.9, 6.3, 14.9],
}
user_data = {}

# Streamlit app header
st.title('Enter Patient Data Below')

# Input boxes for user data
user_patient_id = st.text_input('Enter ID in the following format: ABCD1234', value='')
user_ff_percent = st.number_input('Enter FF %', min_value=0.0, step = 0.01)
user_diff_biorad_nipt = st.number_input('Enter Difference in Gestational Age', min_value=0.0, max_value=300.0, value=0.0)

user_data = {
    'patient_id': initial_user_data['patient_id'] + [user_patient_id],
    'fetal_fraction_percent': initial_user_data['fetal_fraction_percent'] + [user_ff_percent],
    'difference_biorad_nipt': initial_user_data['difference_biorad_nipt'] + [user_diff_biorad_nipt],
}
df = pd.DataFrame([user_data])

st.write('User Data:', df)

if st.button('Visualize Data'):
    # Group by patient_id and calculate mean fetal_fraction_percent
    grouped_data = df.groupby('patient_id').mean().reset_index()
    
    chart = alt.Chart(grouped_data).mark_bar().encode(
        x='patient_id',
        y='fetal_fraction_percent'
    ).properties(
        width=400,
        height=300
    )
    
    st.altair_chart(chart, use_container_width=True)