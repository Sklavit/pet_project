import streamlit as st

#
# import vertexai
# from vertexai.generative_models import GenerativeModel, Part
# import vertexai.preview.generative_models as generative_models
# from google.oauth2.service_account import Credentials
#
# from datetime import datetime

import pandas as pd

import datetime

st.title("DS chat with Google Vertex AI")

########################################################################################################################
# Initialization


########################################################################################################################
# Helpful sidebar

# TODO do I need this?
with st.sidebar:
    # anthropic_api_key = st.text_input("Anthropic API Key", key="file_qa_api_key", type="password")  # TODO update
    "[View the source code](https://github.com/Sklavit/pet_project/tree/20240629_ds_chat/apps/streamlit_ds_chat)"


########################################################################################################################
# Get data to analyze

# upload some dataset to analyze
uploaded_file = st.file_uploader("Upload a dataset to be analyzed", type=["csv"])

# NOTE this upload ALWAYS reload the page, which is a bit of dangerous
# TODO it is better to add buttons: 'reset and use new file', 'do all operations with new file'


# if uploaded_file and question and not anthropic_api_key:   # TODO delete ?
#     st.info("Please add your Anthropic API key to continue.")

if not uploaded_file:
    st.error("Upload dataset to work with")
else:
    # if uploaded_file:  # and question:  # and anthropic_api_key:
    dataframe = pd.read_csv(uploaded_file)
    st.dataframe(dataframe)

    st.write(datetime.datetime.utcnow())
    st.write("### Answer")
    st.text("This is a text", help="this is help")

    ####################################################################################################################
    # Chat logic goes here

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("What is up?"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner(
                "Wait for the whole response (streaming not working with Streamlit)..."
            ):
                # api_response = chat.send_message(
                #     [prompt],
                #     generation_config=generation_config,
                #     safety_settings=safety_settings,
                #     stream=False,
                # )
                # response = api_response.candidates[0].content.parts[0]._raw_part.text
                response = "AI was questioned. Test answer `here`. :) "
                st.markdown(response)

            print(("response:", response))
            st.session_state.messages.append({"role": "assistant", "content": response})
