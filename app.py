import streamlit as st
import random
import toml
#from api_call_test import search_sample
from Gemini_api import initialize_conversation
from Gemini_api import converse_conversation
from reference_buttons import make_button

#Intialize GCP detials-----------------------------------
project_id = "YOUR PROJECT ID"
location = "LOCATION"          # Values: "global", "us", "eu"
engine_id = "ENGINE ID"
data_store_id = "DATA STORE ID"



title = 'https://raw.githubusercontent.com/jordanpym17/streamlit_stuff/main/title.png'
avatar ='https://raw.githubusercontent.com/jordanpym17/streamlit_stuff/main/Picture2.png'
avatar2 ='https://raw.githubusercontent.com/jordanpym17/streamlit_stuff/main/user.png' 
info = 'https://raw.githubusercontent.com/jordanpym17/streamlit_stuff/main/text_sappi_sync.jpg'

CURRENT_THEME = "dark"
IS_DARK_THEME = True

st.image(image=title)
#st.image(image=info)
st.write(":mag: Welcome to SappiSync!  Sappi's very own AI virtual assistant")
st.write(" :computer: For full code overview: [Github repository](https://github.com/jordanpym17/streamlit_stuff.git)") 
st.write(":books: Loaded with 1053 documents from Ngodwana")
st.write(":people_holding_hands: Developed by Jordan Pym and Aletia van Rooyen for the 2024 EIT Challenge")
st.write(" :envelope_with_arrow: [Suggestions/questions/concerns](https://forms.office.com/r/NeaLXgyy9W?origin=lprLink)")


# Check if the conversation is already initialized
if 'conversation_name' not in st.session_state:
    st.session_state.client, st.session_state.conversation_name, st.session_state.parent = initialize_conversation(project_id, location, data_store_id)
    st.session_state.conversation_log = []

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"],avatar=avatar if message["role"]=="assistant" else avatar2):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Ask me a question?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user",avatar=avatar2):
        st.markdown(prompt)
        if prompt.lower() == "new chat":
            st.session_state.messages = []
            st.experimental_rerun()  # Rerun the app

    # Response from Discovery engine in layered
    response_all = converse_conversation(st.session_state.client, st.session_state.conversation_name, st.session_state.parent, prompt)
    response = response_all.reply.summary.summary_text
    references = response_all.reply.summary.summary_with_metadata.references

    # Display assistant response in chat message container
    with st.chat_message("assistant",avatar=avatar):
        st.markdown(response)
        for reference in references: 
            make_button(reference.uri)
        

    i = 1
    for reference in references:
        reference_text = f"[{i}] **{reference.title}**"
        response += f"\n{reference_text}\n"
        i += 1

    st.session_state.messages.append({"role": "assistant", "content": response})
