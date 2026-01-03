from transformers.tools.base import launch_gradio_demo
from word_counter import WordCounterTool

# Version: 1.0.2 - Testing with fixed deploy workflow
launch_gradio_demo(WordCounterTool)
