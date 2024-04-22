import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

from module.formated import Title
# from module.imported import DataImport

title = "SkillQuest"
t = Title().page_config(title)

st.header("💸 Salary for Data Nerds")

col1, col2 = st.columns(2)
with col1:
    type = st.radio("Salary aggregation:",
             ["Annually", "Hourly"],
             horizontal=True)

with col2:
    country = st.selectbox("Country:", 
                 ["India", "United States", "Canada"]
                 )

data_path = f"Dataset/Salary/{country}.csv"
df = pd.read_csv(data_path)
data = {
    'Job': [],
    'Avg_Salary': []
}
counter = 0
for i in range(len(df)):
    job = df["Jobs"][i]
    avg_salary = df[type][i]
    if avg_salary != 0:
        data['Job'].append(job)
        data["Avg_Salary"].append(avg_salary)
        counter+=1
    
source = pd.DataFrame(data)
selector = alt.selection_single(encodings=['x', 'y'])

#Creating horizontal bar graph
hor_bar = alt.Chart(source).mark_bar(
    cornerRadiusBottomRight=4,
    cornerRadiusTopRight=4,
    size=25 
).encode(
    x=alt.X('Avg_Salary:Q', axis=alt.Axis(format='', labelFontSize=0, titleFontSize=0, labelPadding=20)),
    y=alt.Y('Job:N', sort=None, title="", axis=alt.Axis(labelFontSize=15)).sort('-x'),
    color=alt.Color('Avg_Salary:Q', scale=alt.Scale(scheme='purplebluegreen'), legend=None),
    tooltip=['Job:N', alt.Tooltip('Avg_Salary:Q', format="$,")]#hover effect on bars
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
    text=alt.Text("Avg_Salary:Q", format='$,')
)

graph = hor_bar + text
graph = graph.configure_axis(grid=False)

# Display the chart
st.altair_chart(graph)