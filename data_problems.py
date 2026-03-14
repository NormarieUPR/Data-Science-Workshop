import streamlit as st
import pandas as pd 

st.write( """

# Data Science WorkShop Part 1
         
### ColorStack UPRM
         
Feel free to interact with the website and play around with the values of the data provided below!
         
#### Resources:
         
Some links that might be useful when implementing your own datasets 

- [10 minutes to panda](https://pandas.pydata.org/docs/user_guide/10min.html)
         
Most importantly have fun :)
         

""") 

st.write(""" ## 1. Import the data set(s) 
         
Here is an example importing a the *csv* file we are using today: """ )

st.code("df = pd.read_csv('students.csv')", language="python")


df = pd.read_csv('students.csv')


st.write("A common first step in data analysis is using head() to display the first few rows and get a quick understanding of the dataset.")
st.write("**Dataset Shape:** (row, columns)", df.shape)
st.dataframe(df.head())
st.space(size="small")

st.write("## 2. Filter Your Data ")
major = st.selectbox("Choose a major", df["major"].unique()) 

filtered = df[df["major"] == major]

st.write(filtered)

st.space(size="small")
st.write("### GPA vs Study Hours")
st.write("""Vizualize the relaitionship between GPA and study hours 
- Does it defer from major to major?
- Does study hours affect GPA?
- What type of graph is showing? """)

option = st.selectbox("Filter by major or all", ["All Students", "Filtered by Major"] )
gpavsstudy = df  
if option == "All students":
    gpavsstudy = df
if option == "Filtered by Major":
    gpavsstudy = filtered
st.scatter_chart(gpavsstudy, x="study_hours_per_week", y= "gpa", height="content")

st.write(""" ### Club vs Satisfaction
        
Are students happier when they join clubs? """)

clubs = df.groupby("num_clubs")["satisfaction_score"].mean()

st.bar_chart(clubs)


st.write(""" ### Make comparisons yourself !
Ask yourself how different columns relate to each other.
and if they are relevant for the purpose of your project""")

x = st.selectbox("Choose a x axis", df.columns)

y = st.selectbox("Choose a y axis", df.columns)

st.scatter_chart(df,x=x,y=y)

st.write(" #### Ask yourself:")
st.write("""  - Do students who study more sleep less?

- Do students with jobs have lower GPA?

- Do students who live far away attend less?

- Do students with clubs have higher satisfaction?""")