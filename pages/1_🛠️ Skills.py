import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

from module.formated import Title
# from module.imported import DataImport

title = "SkillQuest"
t = Title().page_config(title)

st.header("🛠️ Top Skills for Data Nerds 🤓")

col1, col2 = st.columns(2)
with col1:
    job_title = st.selectbox("Job Title:",
                 ["Data Engineer", "Data Scientist", "Data Analyst",
                  "Bussiness Analyst", "Software Engineer",
                  "ML Engineer", "Cloud Engineer"],  
                  )
with col2:
    country = st.selectbox("Country:", 
                 ["India", "United States", "Canada"]
                 )
    
skills = st.radio("Skills:",
         ["Languages", "Tools", "Databases",
          "Cloud", "Libraries", "Frameworks"],
          horizontal = True)

data_path = f"Dataset/skills/{country}/{skills}.csv"
df = pd.read_csv(data_path)
data = {
    'Skill': [],
    'Percentage': []
}
counter = 0
for i in range(len(df)):
    skill = df["Skills"][i]
    percent = df[job_title][i]
    if percent != 0:
        data['Skill'].append(skill)
        data["Percentage"].append(percent)
        counter+=1
    
source = pd.DataFrame(data)
selector = alt.selection_single(encodings=['x', 'y'])

#Creating horizontal bar graph
hor_bar = alt.Chart(source).mark_bar(
    cornerRadiusBottomRight=4,
    cornerRadiusTopRight=4,
    size=25 
).encode(
    x=alt.X('Percentage:Q', axis=alt.Axis(format='', labelFontSize=0, titleFontSize=0, labelPadding=20)),
    y=alt.Y('Skill:N', sort=None, title="", axis=alt.Axis(labelFontSize=20)).sort('-x'),
    color=alt.Color('Percentage:Q', scale=alt.Scale(scheme='darkmulti'), legend=None),
    #color=alt.condition(selector, 'Percentage:Q', alt.value('lightgray'), legend=None),
    tooltip=['Skill:N', alt.Tooltip('Percentage:Q', format=".2%")]#hover effect on bars
).add_selection(
    selector
).properties(
    width=700,
    height=(counter*35 + 50) 
)

#Adding salary at the end of each bar
text = hor_bar.mark_text(
    dx=3, 
    align='left', 
    size=20
).encode(
    text=alt.Text("Percentage:Q", format='.2%')
)

graph = hor_bar + text
graph = graph.configure_axis(grid=False)

# Display the chart
st.altair_chart(graph)