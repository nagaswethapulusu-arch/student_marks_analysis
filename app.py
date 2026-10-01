import streamlit as st
import pandas as pd

st.title("Student Marks Analysis")

students = ["Asha", "Ravi", "Meena", "Kiran", "Swetha", "Harsh", "Rupesh", "Akhil"]
marks = [78, 85, 62, 90, 71, 89, 70, 65]

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

st.table(pd.DataFrame({"Student": students, "Marks": marks}))

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total", total)
c2.metric("Average", round(average, 2))
c3.metric("Highest", highest)
c4.metric("Lowest", lowest)

st.write(f"Topper: {students[marks.index(highest)]} ({highest})")
st.write(f"Lowest: {students[marks.index(lowest)]} ({lowest})")