import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Startup Analysis", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv('big_startup_secsees_dataset.csv')
    df['funding_total_usd'] = pd.to_numeric(df['funding_total_usd'].replace('-', '0'), errors='coerce').fillna(0)
    df['founded_at'] = pd.to_datetime(df['founded_at'], errors='coerce')
    df['country_code'] = df['country_code'].fillna('Unknown')
    return df

df = load_data()

st.title("🚀 Startup Success Dashboard")

st.sidebar.title("Select Analysis")
option = st.sidebar.selectbox("Choose a visualization:", 
    ["Top Countries", "Startup Status", "Market Categories", "US Regional Analysis"])

if option == "Top Countries":
    st.header("Top 10 Countries by Number of Startups")
    top_countries = df['country_code'].value_counts().head(10)
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=top_countries.index, y=top_countries.values, palette='viridis', ax=ax)
    st.pyplot(fig)
    st.write("The United States (USA) is the overwhelming leader in the global startup ecosystem.")

elif option == "Startup Status":
    st.header("Distribution of Startup Status")
    fig, ax = plt.subplots()
    df['status'].value_counts().plot.pie(autopct='%1.1f%%', startangle=140, ax=ax)
    st.pyplot(fig)

elif option == "Market Categories":
    st.header("Top 10 Startup Categories")
    top_cats = df['category_list'].str.split('|').explode().value_counts().head(10)
    fig, ax = plt.subplots()
    sns.barplot(x=top_cats.values, y=top_cats.index, palette='magma', ax=ax)
    st.pyplot(fig)

elif option == "US Regional Analysis":
    st.header("Top 10 US States by Startup Count")
    usa_states = df[df['country_code'] == 'USA']['state_code'].value_counts().head(10)
    fig, ax = plt.subplots()
    sns.barplot(x=usa_states.index, y=usa_states.values, palette='rocket', ax=ax)
    st.pyplot(fig)
