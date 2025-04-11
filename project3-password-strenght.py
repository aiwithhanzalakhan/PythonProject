import re 
import streamlit as web

web.set_page_config(page_title="Password Strenght Checker", page_icon="☄️", layout="centered")

#css

web.markdown("""
        <style>
            .main {text-align:center}
            .webTextInput {width: 50%; background-color: #4CAF50; color: white; font-size: 18px;}
            .webButton button:hover {background-color: #45a049}
        </style>
""", unsafe_allow_html=True)

web.title("Password Strenght Generator")
web.write("Enter Your Password Below To Check Its Security Level 🔍")

def checkPasswordStrenght(password):
    score = 0
    feedback = []
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password Should ** Be AtLeast 8 Character Long **")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1

    else:
        feedback.append("❌ Password Should Include** Both Uppercase (A-Z) and Lowercase (a-z) Letters **")

    if re.search(r'\d', password):
        score += 1

    else:
        feedback.append("❌ Password Should Include** atLeast one number (0-9) **")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    
    else:
        feedback.append("❌ Include** at Least one special Character (!@#$%^&*) **")



    if score == 4:
        web.success("✅ Strong Password")
    elif score == 3:
        web.info("⚠️ Moderate Password - Consider improving security by adding more features")
    else:
        web.error("❌ Week Password - Follow the Suggetion below to strenght it")

    
    if feedback:
        with web.expander(" Improve Your Password"):
            for item in feedback:
                web.write(item)
password = web.text_input("Enter your Password:", type="password", help="Ensure Your password is strong")

if web.button("Check Strenght"):
    if password:
        checkPasswordStrenght(password)
    else:
        web.warning('Please enter a password first')

