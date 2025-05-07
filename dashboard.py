import pandas as pd
import streamlit as st

st.title("Obsidian Vault Explorer 🚀")


@st.cache_data
def get_df():
    df = pd.DataFrame(pd.read_csv("output.csv"))
    return df


df = get_df()

def metrics():
    col1, col2, col3 = st.columns(3)
    col1.metric("Notes", len(df))
    


def notes_graph():
    st.subheader("Notes modified by time")
    note_index = df.index
    modified_time = pd.to_datetime(df['modified_time'])

    time = df.reset_index()
    date = modified_time.dt.date

    counts = date.groupby(date).size()
    time['note_quantity'] = date.map(counts)
    
    time['modified_time'] = date
 
    st.line_chart(time, x = "modified_time", y = "note_quantity")

def dashboard():
    st.table(df)


metrics()
notes_graph()
dashboard()