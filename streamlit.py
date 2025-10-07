import streamlit as st

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  

    def total(self):
        return sum(self.marks)

    def average(self):
        return self.total() / len(self.marks)

    def grade(self):
        avg = self.average()
        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 45:
            return "C"
        else:
            return "F"



st.title("Student Report Card Generator")

name = st.text_input("Enter Student Name")
marks_input = st.text_area("Enter marks separated by commas (e.g. 85,90,78)")

if st.button("Generate Report"):
    try:
        marks = list(map(int, marks_input.split(",")))
        student = Student(name, marks)

        st.success(f"Report Card for {student.name}")
        st.write(f"**Total Marks:** {student.total()}")
        st.write(f"**Average Marks:** {student.average()}")
        st.write(f"**Grade:** {student.grade()}")

    except:
        st.error("Please enter valid numbers for marks, separated by commas.")