from transformers import AutoTokenizer
from transformers import Tool

class WordCounterTool(Tool):
    name = "word_counter"
    description = "This tool counts the words of a text."
    inputs = ["text"]
    outputs = ["text"]

    def __call__(self, text: str):
        words = text.split(" ")
        return len(words)
        