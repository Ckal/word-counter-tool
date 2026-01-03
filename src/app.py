from transformers.tools.base import launch_gradio_demo
from word_counter import WordCounterTool

# Version: 1.0.1 - Testing deployment pipeline
launch_gradio_demo(WordCounterTool)
