import streamlit as st

import streamlit as st

# Create a title for the website
st.title("Student Information Form by ABHINAV BHATT ")

# Create a form with input fields
with st.form("student_form"):
    # Create input fields for name, mother's name, address, class, and aim
    name = st.text_input("Name")
    mother_name = st.text_input("Mother's Name")
    address = st.text_area("Address")
    class_ = st.selectbox("Class",
                          ["Class 1", "Class 2", "Class 3", "Class 4", "Class 5", "Class 6", "Class 7", "Class 8",
                           "Class 9", "Class 10", "Class 11", "Class 12"])
    aim = st.text_area("Aim")

    # Create a submit button
    submitted = st.form_submit_button("Done")

# Check if the form has been submitted
if submitted:
    # Create a column to display the data
    st.write("## Student Information")
    col1, col2 = st.columns(2)

    # Display the data in the column
    with col1:
        st.write("### Personal Details")
        st.write(f"**Name:** {name}")
        st.write(f"**Mother's Name:** {mother_name}")
        st.write(f"**Address:** {address}")

    with col2:
        st.write("### Academic Details")
        st.write(f"**Class:** {class_}")
        st.write(f"**Aim:** {aim}")