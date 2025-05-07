import pandas as pd
import streamlit as st

# *Daily Pulse*
#    Generate a line chart of notes **created per day** for the last 90 days.
#    👉 Hint: groupby(created_date).size()


def daily(df):

    st.subheader("Notes created by day")

    # get created_time

    created_time = pd.to_datetime(df['created_time'])
    created_time = created_time.dt.date
    df['created_time'] = created_time

    # group notes by quantity

    note_index = df.index
    note_index = df.groupby(created_time).size()
    df['note_quantity'] = df['created_time'].map(note_index)


    # paint graph

    #st.line_chart(created_time)

    st.line_chart(df, x = "created_time", y = "note_quantity")

    
   