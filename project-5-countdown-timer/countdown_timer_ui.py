import gradio as gr
from countdown_timer import set_countdown

gr.Interface(fn=set_countdown,
             inputs=gr.Number(label="Enter seconds"),
             outputs="text",
             title="Simple Countdown Timer").launch()