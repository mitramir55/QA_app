import pytest
import app
from app import load_wiki_summary, answer_question, load_qa_pipeline



def test_load_wiki_summary():
    expected_var = "A vrddhi-derived form of Sanskrit mitra gives Maitreya, the name of a bodhisattva in Buddhist tradition."
    assert expected_var in load_wiki_summary("mitra")
    
def test_load_wiki_summary_fail():
    expected_var = "A vrddhi-derived form of Sanskrit mitra gives Maitreya, the name of a bodhisattva in Buddhist tradition."
    assert expected_var not in load_wiki_summary("word")

def test_load_wiki_summary_symbols():
    with pytest.raises(Exception):
        load_wiki_summary("~")
        
def test_answer_question():
    expected_var = "Indo-Iranian"
    question = "what is the origin of mitra"
    qa_pipeline = load_qa_pipeline()
    assert expected_var == answer_question(qa_pipeline, question, load_wiki_summary("mitra"))["answer"]
    
def test_answer_question_fail():
    expected_var = "Indo-Iranian"
    question = "what is the origin of mitra"
    qa_pipeline = load_qa_pipeline()
    assert expected_var != answer_question(qa_pipeline, question, load_wiki_summary("word"))
    
def test_component():
    topic = "mitra"
    question = "what is the origin of mitra"
    expected_var = "A vrddhi-derived form of Sanskrit mitra gives Maitreya, the name of a bodhisattva in Buddhist tradition."

    if topic:
    # load wikipedia summary of topic
        summary = load_wiki_summary(topic)
        assert expected_var in summary

    # perform question answering
    if question != "":
        # load question answering pipeline
        qa_pipeline = load_qa_pipeline()

        # answer query question using article summary
        result = answer_question(qa_pipeline, question, summary)
        answer = result["answer"]
        assert answer == "Indo-Iranian"
        