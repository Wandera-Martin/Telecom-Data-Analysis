import streamlit as st
from cProfile import label
import numpy as np
import pandas as pd
import plotly.graph_objects as go
#
import sys
sys.path.insert(0,'../scripts/')

#
import seaborn as sns
import matplotlib.pyplot as plt

#from load_data import load_data  
from user_overview import UserOverview
from plots import plot_hist,mult_hist

# Define functions for each page content
def User_Overview():
      st.title("User Overview Analysis")    # original dataset
      st.markdown(f'<h1 style="color:green;font-size:24px;">{"Sample Data from the original dataset"}</h1>', unsafe_allow_html=True)
      df = pd.read_csv("./data/telecom.csv",index_col=0)
      st.write(df.head(10))

    # cleaned dataset
      st.markdown(f'<h1 style="color:green;font-size:24px;">{"Sample Data from the cleaned dataset"}</h1>', unsafe_allow_html=True)
      df = pd.read_csv("./data/cleaned_data_source.csv",index_col=0)
      st.write(df.head(10))
    
    # display top 10 handsets used by users
      st.header('Display top 10 handsets used by customers')
      user_ov = UserOverview(df)
      top_10_handsets = user_ov.get_top_handsets(10)
      st.write(top_10_handsets)

      fig = go.Figure(go.Pie(labels = top_10_handsets.index,values = top_10_handsets.values))
      st.header("Top 10 Handset Type used by customers")
      st.plotly_chart(fig)

      # display top 3 manufacturers
      st.header('Display top 3 handset manufacturers')
      top_3_manufacturers = user_ov.get_top_manufacturers(3)
      st.write(top_3_manufacturers)

        
      # display the top_handsets result in bar graph
      # plt.figure(figsize=(10,5))
      # sns.barplot(x=top_3_manufacturers.index, y=top_3_manufacturers.values)
      # plt.title('Top 3 Handset Manufacturers', size=14, fontweight="bold")
      # plt.xlabel('Handset Manufacturers', size=13, fontweight="bold") 
      # plt.ylabel('Number of Users', size=13, fontweight="bold")
      # plt.show()

      fig = go.Figure(go.Pie(labels = top_3_manufacturers.index,
      values = top_3_manufacturers.values
      ))
      st.header("Top 3 Handset Manufacturers")
      st.plotly_chart(fig)
def User_Engagement():
  st.subheader("Data Exploration")
  st.write("This page allows you to explore the data.")


def User_Experience():
  st.subheader("Visualizations")
  st.write("")

def User_Satisfication():
  st.subheader("User Satisfication Analysis")
  st.write("")
  # Add additional information about the dashboard

# Set page configuration (optional)
st.set_page_config(
    page_title="My Streamlit Dashboard",
    page_icon="",
)

# Create a sidebar for navigation
st.sidebar.header("Navigation")
pages = ["Home", "Data Exploration", "Visualizations", "About"]
selection = st.sidebar.radio("Go to:", pages)

# Display the selected page content
if selection == "User Overview":
  User_Overview()
elif selection == "User Engagement":
  User_Engagement()
elif selection == "User Experience":
  User_Experience()
elif selection == "User Satisfication":
  User_Satisfication()

