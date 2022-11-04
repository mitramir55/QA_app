import pytest
from app import load_wiki_summary


def test_load_wiki_summary():
        expected_var = "A vrddhi-derived form of Sanskrit mitra gives Maitreya, the name of a bodhisattva in Buddhist tradition."
        assert expected_var in load_wiki_summary("mitra")