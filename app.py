import torch
import wikipedia
import transformers
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

# Main app engine
if __name__ == "__main__":
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


class Solution:

    # def is_palindrom(self, s, i, j):
    #     l, r = i, j

    #     while l < r:
    #         if s[l] != s[r]: return False
    #         l, r = l + 1, r - 1 
    #     return True

    def partition(self, s: str) -> List[List[str]]:

        all_parts = []
        part = []

        def dfs(i):
            if i == len(s):
                all_parts.append(part.copy())
                return
            for j in range(i+1, len(s)+1):
                # j+1?
                # s[i:j] == s[i:j][::-1]
                #if self.is_palindrom(s, i, j):
                if s[i:j] == s[i:j][::-1]:
                    part.append(s[i:j])
                    dfs(j)

                    # if it is a palindrom the whole list of partitions will be 
                    # added to the all_pars
                    part.pop()
        dfs(0)
        return all_parts

def palindrom_substrings(s:str) -> list[list]:
    """
    find all the substrings that are palindromes and form s
    """
    partition = []
    ret_list = []

    def dfs(idx):
        """
        gets the index for starting the partition and 
        adds palindromes to ret_list
        """
        if idx == len(s):
            ret_list.append(partition.copy())
            return
        
        for j in range(idx + 1, len(s) + 1):
            if s[idx:j] == s[idx:j][::-1]:
                partition.append(s[idx:j])
                dfs(j)

                # we have to remove what we added here because we will have 
                # to check if partition has the whole s by checking if 
                # idx == len(s)
                partition.pop()
            
        dfs(0)
        return ret_list
palindrom_substrings('aab')



from functools import cache

@cache
def palindrom_substrings_2(s:str) -> list[list]:
    ret_list = []
    if not s: return [[]]

    for i in range(1, len(s) + 1):
        if s[:i] == s[:i][::-1]:
            for suffix in palindrom_substrings_2(s[i:]):
                ret_list .append([s[:i]] + suffix)
    return ret_list

palindrom_substrings_2('aab')