import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
st.title('Hello Wilders, welcome to my application!')
st.write("La création de l'application par Jouini Zied")
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_voiture = pd.read_csv(link)
df_voiture
genre = st.radio( "Select Country of origin",
                 ('Japan', 'USA', 'Europe'))   
if genre == 'USA':
    df1 = df_voiture.loc[df_voiture["continent"] ==" US."] 
    df1 
    viz_correlation=sns.heatmap(df1.corr(), center=0,cmap = sns.color_palette("vlag", as_cmap=True),annot=True)
    st.pyplot(viz_correlation.figure)
    st.line_chart(df1['hp'])  
if genre == 'Europe':
    df2 = df_voiture.loc[df_voiture["continent"] ==" Europe."] 
    df2
    viz_correlation=sns.heatmap(df2.corr(), center=0,cmap = sns.color_palette("vlag", as_cmap=True),annot=True)
    st.pyplot(viz_correlation.figure)
    st.line_chart(df2['hp'])   
else:
    df3 = df_voiture.loc[df_voiture["continent"] ==" Japan."]
    df3
    viz_correlation=sns.heatmap(df3.corr(), center=0,cmap = sns.color_palette("vlag", as_cmap=True),annot=True)
    st.pyplot(viz_correlation.figure)
    st.line_chart(df3['hp'])
   
   
    