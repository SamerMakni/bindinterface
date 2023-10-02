import streamlit as st
import re
from Emailer import EmailSender

def is_valid_email(email):
    # Simple email format validation using regex
    pattern = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
    return re.match(pattern, email)


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
                if is_valid_email(email):
                    email_ = EmailSender()
                    subject_ = f"Contact from {name}, [{email}, {subject}]"
                    email_.send_email("cidalsdb.contact@gmail.com", subject_, message)
                    st.success("Thank you! Your data access request has been submitted.")
                else:
                    st.warning("Please enter a valid email address.")
            else:
                st.warning("Please fill out all the fields.")