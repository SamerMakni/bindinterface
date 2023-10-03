import streamlit as st
import re
from Emailer import EmailSender
from captcha.image import ImageCaptcha
import random
import string
import time


def is_valid_email(email):
    # Simple email format validation using regex
    pattern = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
    return re.match(pattern, email)

captcha_codes = []

def contact():
    st.title("Contact")
    captcha_length = 5  # You can adjust the length of the CAPTCHA code
    captcha_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=captcha_length))
    captcha_codes.append(captcha_code)
    print(captcha_codes)
    print(f"this is the first captcha: {captcha_code}")
    with st.form("my_form"):
        # Contact Information
        name = st.text_input("Name", "")
        email = st.text_input("Email", "")
        subject = st.text_input("Subject", "")

        image_captcha = ImageCaptcha()
        captcha_image = image_captcha.generate(captcha_code)
        st.image(captcha_image, caption='CAPTCHA', width=150)
        captcha_input = st.text_input("Enter CAPTCHA", "")
        print(f"this is the input captcha:{captcha_input}")
        # Message
        message = st.text_area("Message", "")
        print(captcha_input)
        # Submit Button
        submitted = st.form_submit_button("Submit")
        if submitted:
            if name and email and subject and message and captcha_input: 
                print()
                if captcha_input == captcha_codes[len(captcha_codes) - 2]:
                    if is_valid_email(email):
                        email_ = EmailSender()
                        subject_ = f"Contact from {name}, [{email}, {subject}]"
                        email_.send_email("cidalsdb.contact@gmail.com", subject_, message)
                        st.success("Thank you! Your data access request has been submitted.")
                    else:
                        st.warning("Please enter a valid email address.")

                else:
                    st.warning("Incorrect CAPTCHA code. Please try again.")

            else:
                st.warning("Please fill out all the fields and enter the correct CAPTCHA code.")
