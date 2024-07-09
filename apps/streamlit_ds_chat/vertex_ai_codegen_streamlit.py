import streamlit as st

import vertexai
from vertexai.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models
from google.oauth2.service_account import Credentials

from datetime import datetime


st.title(
    "Chat with Google Vertex AI to experiment with prompts which could be used for the orchestrator agent."
)

########################################################################
# init chat model

chat = None

if "vertex_ai_model" not in st.session_state or chat is None:
    st.session_state["vertex_ai_model"] = "gemini-1.5-flash-001"

    credentials = Credentials.from_service_account_info(st.secrets["gcs_connections"])
    vertexai.init(
        project="pivotal-cable-428219-c5",
        location="us-central1",
        credentials=credentials,
    )
    model = GenerativeModel(
        st.session_state[
            "vertex_ai_model"
        ],  # by default it will be "gemini-1.5-flash-001",
        # NOTE this is v1 of instructions, They worked well enough to generate steps
        # system_instruction=[
        #     "You are a data scientist manager."
        #     "You responsibility is to provide a plan of actions, which should be taken to answer the given question."
        #     "Each new question will be marked by tags: <q> and </q>."
        #     "If you don't have enough data to answer the question, respond: <not enough data/>"
        #     "Information about loaded data will be provided between tags <locals> and </locals> in JSON format."
        #     "You will be questioned with analytical questions about the data available in <locals>."
        #     "You should respond with step by step plan of data transformation which are needed to answer the given question."
        #     "Place the plan's steps inside <step></step> tags."
        #     "You must include explanations or any other important information into your answer, and they should be marked with <comments></<comments> tags."
        #     # "You should not include any explanations."
        #     # "You must include explanations or any other important information into your answer, but it should be clearly marked as comments."
        #     "User may update the state of <locals> with messages starting with 'Update locals:'. You should update the state of <locals> respectively"
        #     "On message starting with '`locals' you should return the current state of <locals>."
        #     ,
        #     "<locals>{files: ['fruits.csv'], "
        #     "df_table: {type: pandas.DataFrame, columns: ['','person','fruit','likes']}}</locals>"
        # ],
        # system_instruction=[
        #     "You are a data scientist manager."
        #     "You responsibility is to provide a plan of actions, which should be taken to answer the given question."
        #     "Each new question will be marked by tags: <q> and </q>."
        #     "If you don't have enough data to answer the question, respond: <not enough data/>"
        #     "Information about loaded data will be provided between tags <locals> and </locals> in JSON format."
        #     "You will be questioned with analytical questions about the data available in <locals>."
        #     "Write a full python module, which should contain only 1 function def run(data). "
        #     "The data parameter is expected to be a dictionary, with the same keys as <locals> and with corresponding values. "
        #     "The function should return the answer to the question. "
        #     "The answer should be represented in the most structured way: "
        #     "it should be a single number if possible, it may be list, or pandas.DataFrame. "
        #     "The function should not return the string unless it is directly requested by the user question. "
        #     "For example, the function may return string, if question was asked about something specific, like name of the person, "
        #     "who satisfy some conditions. For example: `<s>Who likes the most number of fruits?</s>`. "
        #     # "If the user request demands from you to draw some chart, you should return dictionary, "
        #     # "Return json with keys: chart_type: streamlit chart type, kwargs: dict with kwargs for the corresponding streamlit charting tool."
        #     "You must include explanations or any other important information into your answer in the form of code comments."
        #     "User may update the state of <locals> with messages starting with 'Update locals:'. You should update the state of <locals> respectively"
        #     "On message starting with '`locals' you should return the current state of <locals>."
        #     ,
        #     "<locals>{"
        #     "df_table: {type: pandas.DataFrame, columns: ['','person','fruit','likes']}"
        #     "}</locals>"
        # ],
        # v3 with charts
        system_instruction=[
            "You are a data scientist manager."
            "You responsibility is to provide a plan of actions, which should be taken to answer the given question."
            "Each new question will be marked by tags: <q> and </q>."
            "If you don't have enough data to answer the question, respond: <not enough data/>"
            "Information about loaded data will be provided between tags <locals> and </locals> in JSON format."
            "You will be questioned with analytical questions about the data available in <locals>."
            "Write a full python module, which should contain only 1 function def run(data). "
            "The data parameter is expected to be a dictionary, with the same keys as <locals> and with corresponding values. "
            "The function should return the answer to the question in form of dictionary. "
            "Key `results` should include the answer represented in the most structured way: "
            "it should be a single number if possible, it may be list, or pandas.DataFrame. "
            "The function should not return the string unless it is directly requested by the user question. "
            "For example, the function may return string, if question was asked about something specific, like name of the person, "
            "who satisfy some conditions. For example: `<s>Who likes the most number of fruits?</s>`. "
            "Key `chart` should be `None` if no charts need, and be a dictionary if a chart is requested. "
            "This dictionary should contain the following keys: "
            "`chart_type`: Bokeh chart type, "
            "`kwargs`: dict with kwargs for the corresponding Bokeh charting tool."
            "You must include explanations or any other important information into your answer in the form of code comments."
            "User may update the state of <locals> with messages starting with 'Update locals:'. You should update the state of <locals> respectively"
            "On message starting with '`locals' you should return the current state of <locals>.",
            "<locals>{"
            "df_table: {type: pandas.DataFrame, columns: ['','person','fruit','likes']}"
            "}</locals>",
        ],
    )
    chat = model.start_chat()

generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}

#####################################


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# streaming is not working with streamlit, exceptions inside `vertexai.generative_models import GenerativeModel`
USE_STREAMING = False

if prompt := st.chat_input("What is up?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        if USE_STREAMING:
            api_response_stream = chat.send_message(
                [prompt],
                generation_config=generation_config,
                safety_settings=safety_settings,
                stream=True,
            )

            def stream_data():
                for api_response in api_response_stream:
                    chunk = api_response.candidates[0].content.parts[0]._raw_part.text
                    print(f"{datetime.now()}: {chunk}")
                    yield chunk

            response = st.write_stream(stream_data)
        else:
            with st.spinner(
                "Wait for the whole response (streaming not working with Streamlit)..."
            ):
                api_response = chat.send_message(
                    [prompt],
                    generation_config=generation_config,
                    safety_settings=safety_settings,
                    stream=False,
                )
                response = api_response.candidates[0].content.parts[0]._raw_part.text
                st.write(response)

        print(("response:", response))
        st.session_state.messages.append({"role": "assistant", "content": response})
