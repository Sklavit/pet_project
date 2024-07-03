import json
from pprint import pprint

API_TOKEN = st.secrets["HF_API_KEY"]

import requests

headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/microsoft/DialoGPT-large"
# def query(payload):
#     response = requests.post(API_URL, headers=headers, json=payload)
#     print('response', response.status_code)
#     return response.json()
#
# data = query(
#     {
#         "inputs": {
#             "past_user_inputs": ["Which movie is the best ?"],
#             "generated_responses": ["It's Die Hard for sure."],
#             "text": "Can you explain why ?",
#         },
#     }
# )
# # Response
# # This is annoying
# # data.pop("warnings")
# pprint((
#     data,
#     {
#         "generated_text": "It's the best movie ever.",
#         "conversation": {
#             "past_user_inputs": [
#                 "Which movie is the best ?",
#                 "Can you explain why ?",
#             ],
#             "generated_responses": [
#                 "It's Die Hard for sure.",
#                 "It's the best movie ever.",
#             ],
#         },
#         # "warnings": ["Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation."],
#     },
# ))

# from transformers import pipeline
#
# messages = [
#     {"role": "user", "content": "Who are you?"},
# ]
# pipe = pipeline("text-generation", model="microsoft/DialoGPT-large")
# pipe(messages)

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")

chat_history_ids = None

# Let's chat for 5 lines
for step in range(5):
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizer.encode(
        input(">> User:") + tokenizer.eos_token, return_tensors="pt"
    )

    # append the new user input tokens to the chat history
    bot_input_ids = (
        torch.cat([chat_history_ids, new_user_input_ids], dim=-1)
        if step > 0
        else new_user_input_ids
    )

    # generated a response while limiting the total chat history to 1000 tokens,
    chat_history_ids = model.generate(
        bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id
    )

    # pretty print last ouput tokens from bot
    print(
        "DialoGPT: {}".format(
            tokenizer.decode(
                chat_history_ids[:, bot_input_ids.shape[-1] :][0],
                skip_special_tokens=True,
            )
        )
    )
