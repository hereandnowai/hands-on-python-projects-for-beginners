import gradio as gr
from number_guessing import make_guess

gr.Interface(fn=make_guess,
             inputs=gr.Number(label="Enter your guess (0-9)"),
             outputs="text",
             title="Simple Number Guessing Game").launch()