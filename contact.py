import streamlit as st
def contact():
    st.title("Contact Us")
    with st.form("my_form"):
        # Contact Information
        name = st.text_input("Name", "")
        email = st.text_input("Email", "")
        subject = st.text_input("Subject", "")

        # Message
        message = st.text_area("Message", "")

        # Submit Button
        submitted = st.form_submit_button("Submit")
        if submitted:
            if name and email and subject and message:
                st.success("Thank you! Your message has been submitted.")
            else:
                st.warning("Please fill out all the fields.")