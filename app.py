import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Hospital Readmission Dashboard", 
                   page_icon="🏥", layout="wide")


st.title("🏥 Hospital Patient Readmission Analysis")
st.markdown("### Identifying key risk factors for 30-day readmission")

@st.cache_data
def load_data():
    df = pd.read_csv("Data/cleaned_data.csv")
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("🔍 Filters")

age_filter = st.sidebar.multiselect(
    "Select Age Group",
    options=df['age'].unique(),
    default=df['age'].unique()
)

gender_filter = st.sidebar.multiselect(
    "Select Gender",
    options=df['gender'].unique(),
    default=df['gender'].unique()
)

# Apply Filters
df = df[(df['age'].isin(age_filter)) & (df['gender'].isin(gender_filter))]

st.success(f"✅ Data Loaded! Total Patients: {len(df):,}")
# KPI Metrics
col1, col2, col3, col4 = st.columns(4)

total_patients = len(df)
total_readmitted = df['readmitted_binary'].sum()
readmission_rate = (total_readmitted / total_patients) * 100
avg_stay = df['time_in_hospital'].mean()

with col1:
    st.metric("Total Patients", f"{total_patients:,}")
with col2:
    st.metric("Readmitted (<30 days)", f"{total_readmitted:,}")
with col3:
    st.metric("Readmission Rate", f"{readmission_rate:.2f}%")
with col4:
    st.metric("Avg Hospital Stay", f"{avg_stay:.2f} days")

st.markdown("---")

# Two columns for charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Readmission Distribution")
    fig1 = px.pie(df, names='readmitted', 
                  color='readmitted',
                  color_discrete_map={'NO':'green', '>30':'orange', '<30':'red'},
                  hole=0.4)
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    st.subheader("👴 Age vs Readmission")
    age_data = df.groupby(['age', 'readmitted']).size().reset_index(name='count')
    fig2 = px.bar(age_data, x='age', y='count', color='readmitted',
                  color_discrete_map={'NO':'green', '>30':'orange', '<30':'red'})
    st.plotly_chart(fig2, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    st.subheader("💊 Avg Medications vs Readmission")
    med_data = df.groupby('readmitted')['num_medications'].mean().reset_index()
    fig3 = px.bar(med_data, x='readmitted', y='num_medications',
                  color='readmitted',
                  color_discrete_map={'NO':'green', '>30':'orange', '<30':'red'})
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("🚨 Top 10 High Risk Diagnoses")
    diag_data = df[df['diag_1'] != 'Unknown'].groupby('diag_1').agg(
        total=('encounter_id', 'count'),
        readmitted=('readmitted_binary', 'sum')
    ).reset_index()
    diag_data['rate'] = (diag_data['readmitted'] / diag_data['total']) * 100
    diag_data = diag_data[diag_data['total'] > 100].sort_values('rate', ascending=False).head(10)
    
    fig4 = px.bar(diag_data, x='rate', y='diag_1', orientation='h',
                  labels={'rate': 'Readmission Rate (%)', 'diag_1': 'Diagnosis Code'})
    st.plotly_chart(fig4, use_container_width=True)
    
st.markdown("---")

# Raw Data Table
with st.expander("📋 View Raw Data"):
    st.dataframe(df.head(100))

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | Data Source: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/diabetes+130-us+hospitals+for+years+1999-2008)")