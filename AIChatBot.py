import google.generativeai as genai
import streamlit as st
import os


# Configuration of API key
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

#To intialize the generative model
model = genai.GenerativeModel('gemini-1.5-flash')

#function to get resonse from model
def getResponseFromModel(user_input):
    response = model.generate_content(user_input)
    return response.text

# Streamlit Interface
st.set_page_config(page_title="AI Chatbot" , layout = "centered")

st.title(" 🤖 AI ChatBOT 🤖 ")
st.write("Powered by Gemini")

if "history" not in st.session_state:
    st.session_state["history"] = []

# Display chat history
for user_message, bot_message in st.session_state.history:
    st.markdown(f"""
    <div style="
        background-color: #d1d3e0; 
        border-radius: 15px; 
        padding: 10px 15px; 
        margin: 5px 0; 
        max-width: 70%; 
        text-align: left; 
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>You:</b> {user_message} 😊</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="
        background-color: #e1ffc7; 
        border-radius: 15px; 
        padding: 10px 15px; 
        margin: 5px 0; 
        max-width: 70%; 
        text-align: left; 
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>Bot:</b> {bot_message} 🤖</p>
    </div>
    """, unsafe_allow_html=True)
    
# user_input = input("Enter your Prompt = ")
# output = get_chatbot_response(user_input)

# print(output)

with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("", max_chars=2000)
    submit_button = st.form_submit_button("Send")

    if submit_button:
        if user_input:
            response = getResponseFromModel(user_input)
            st.session_state.history.append((user_input, response))
        else:
            st.warning("Please Enter A Prompt")