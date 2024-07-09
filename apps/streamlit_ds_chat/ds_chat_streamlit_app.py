import coiled
import streamlit as st
import importlib
import os.path

from dask.distributed import Client

import pandas as pd

from vertex_ai_codegen import (
    start_code_generator_chat,
    GENERATION_CONFIG,
    SAFETY_SETTINGS,
)

st.title("DS chat with Google Vertex AI")

########################################################################################################################
# Initialization

# init chat model

if "vertex_ai_model" not in st.session_state:
    st.session_state["vertex_ai_model"] = "gemini-1.5-flash-001"

if "code_get_chat" not in st.session_state:
    chat = start_code_generator_chat(
        st.secrets["gcs_connections"], model_name=st.session_state["vertex_ai_model"]
    )
    st.session_state.code_get_chat = chat
else:
    chat = st.session_state.code_get_chat

# Create or connect to a Coiled cluster
with st.spinner("Creating or connecting to a Coiled cluster"):
    if "cluster" not in st.session_state:
        cluster = coiled.Cluster(
            name="my-cluster", n_workers=1, idle_timeout="20 minutes"
        )
        # n_workers – Number of workers in this cluster.
        # Can either be an integer for a static number of workers,
        # or a list specifying the lower and upper bounds for adaptively scaling up/ down workers
        # depending on the amount of work submitted.
        # Defaults to n_workers=[4, 20] which adaptively scales between 4 and 20 workers.
        client = Client(cluster)
        st.session_state.cluster = cluster
        st.session_state.client = client
    else:
        cluster = st.session_state.cluster
        client = st.session_state.client

########################################################################################################################
# Helpful sidebar

with st.sidebar:
    "[View the source code](https://github.com/Sklavit/pet_project/tree/20240629_ds_chat/apps/streamlit_ds_chat)"

########################################################################################################################
# Get data to analyze

# upload some dataset to analyze
uploaded_file = st.file_uploader("Upload a dataset to be analyzed", type=["csv"])

# NOTE this upload ALWAYS reload the page, which is a bit of dangerous
# TODO it is better to add buttons: 'reset and use new file', 'do all operations with new file'

if not uploaded_file:
    st.error("Upload dataset to work with")
else:
    # if uploaded_file:  # and question:  # and anthropic_api_key:
    dataframe = pd.read_csv(uploaded_file)
    st.dataframe(dataframe)

    ####################################################################################################################
    # Chat logic goes here

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # display all session history
    for message in st.session_state.messages:
        with st.chat_message(
            message["role"], avatar="🛑" if message["role"] == "error" else None
        ):
            st.markdown(message["content"])

    if prompt := st.chat_input("What do you what to ask about given dataset?"):
        # save user prompt
        st.session_state.messages.append({"role": "user", "content": prompt})

        # render user prompt in chat
        with st.chat_message("user"):
            st.markdown(prompt)

        # processing of the assistant response
        with st.chat_message("assistant"):
            # step 1. code generation
            with st.spinner(
                "Waiting for the whole generated code "
                "(streaming not working with Streamlit and this beta version of vertexAI)..."
            ):
                # TODO componentize this direct usage of chat.send_message
                api_response = chat.send_message(
                    prompt,
                    generation_config=GENERATION_CONFIG,
                    safety_settings=SAFETY_SETTINGS,
                    stream=False,
                )
                response = api_response.candidates[0].content.parts[0]._raw_part.text

            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

            # This response should be in the form of code
            if not (response.startswith("```python") and response.endswith("```")):
                st.error("AI response is not a code!")
                st.session_state.messages.append(
                    {"role": "assistant", "content": response}
                )
                st.session_state.messages.append(
                    {"role": "error", "content": "AI response is not a code!"}
                )
                st.rerun()

            # so, the response IS code. Save it to tmp file
            # TODO using only one and the same file is not safe in multiuser environment
            file = "task.py"
            with open(file, "w") as file:
                file.write(response[10:-3])

            msg = "Generated code was saved to the file"
            st.info(msg)
            st.session_state.messages.append({"role": "error", "content": msg})

            # Now we should run remote execution
            with st.spinner("Waiting for remote code execution..."):
                # Step 2: Upload the module file to all workers
                file_name = "task.py"
                client.upload_file(file_name)

                # Step 3: Verify the file upload
                def check_file(filename):
                    return os.path.exists(filename)

                st.info("Verifying file transfer...")
                st.info(
                    client.run(check_file, file_name)
                )  # Should print True on all workers

                # Step 4: Use the uploaded module in a distributed task
                def use_uploaded_module():
                    try:
                        module = importlib.import_module(file_name[:-3])
                        print(f"Successfully imported {file_name}")
                    except ImportError as e:
                        print(f"Error importing {file_name}: {e}")
                        return None

                    return module.run({"df_table": dataframe})

                result = client.run(use_uploaded_module)

                st.info(result)

            # TODO save results in the history

            result = next(iter(result.values()))
            # Let's show some charts
            chart = result.get("chart")
            if chart:
                st.write("Chart is here")
                kwargs = chart.get("kwargs", {})
                # p = figure(
                #     title=kwargs.get("title"),
                #     x_axis_label=kwargs.get("x_axis_label"), y_axis_label=kwargs.get("y_axis_label"))
                #
                # p.vbar(
                #     x=kwargs.get("x"), top=kwargs.get("top"), width=kwargs.get("width"))

                # x = [1, 2, 3, 4, 5]
                # y = [6, 7, 2, 4, 5]
                #
                # p = figure(
                #     title='simple line example',
                #     x_axis_label='x',
                #     y_axis_label='y')
                #
                # p.line(x, y, legend_label='Trend', line_width=2)
                #
                # st.bokeh_chart(p, use_container_width=True)

                st.bar_chart(
                    data=pd.DataFrame({"x": kwargs.get("x"), "top": kwargs.get("top")}),
                )
                # x='x', y='top', x_label=kwargs.get("x_axis_label"), y_label=kwargs.get("y_axis_label"),
                # color=None, horizontal=False,
                # width=None, height=None,
                # use_container_width=True)
