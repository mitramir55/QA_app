#  Copyright Mitra Mirshafiee, 2022 Licensed under MIT License.
#  See the LICENSE.txt for more information.

import wikipedia
import streamlit as st
from tokenizers import Tokenizer
from transformers import pipeline, Pipeline 


@st.cache(hash_funcs={Tokenizer: lambda _: None}, allow_output_mutation=True)
def load_qa_pipeline() -> Pipeline:
    qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")
    return qa_pipeline

@st.cache
def load_wiki_summary(query: str) -> str:
    results = wikipedia.search(query)
    summary = wikipedia.summary(results[0], sentences=10)
    return summary

def answer_question(pipeline: Pipeline, question: str, paragraph: str) -> dict:
    input = {
        "question": question,
        "context": paragraph
    }
    output = pipeline(input)
    return output


st.image(r"assets\first.jpg")

st.markdown("[Source](https://towardsdatascience.com/automatic-question-answering-ac7593432842)")
# display title and description
st.title("Wikipedia Question Answering")
st.write("Search topic, Ask questions, Get Answers")

# display topic input slot
topic = st.text_input("SEARCH TOPIC", "")

# display article paragraph
article_paragraph = st.empty()

# display question input slot
question = st.text_input("QUESTION", "")

if topic:
    # load wikipedia summary of topic
    summary = load_wiki_summary(topic)

    # display article summary in paragraph
    article_paragraph.markdown(summary)

    # perform question answering
    if question != "":
        # load question answering pipeline
        qa_pipeline = load_qa_pipeline()

        # answer query question using article summary
        result = answer_question(qa_pipeline, question, summary)
        answer = result["answer"]

        # display answer
        st.write(answer)

