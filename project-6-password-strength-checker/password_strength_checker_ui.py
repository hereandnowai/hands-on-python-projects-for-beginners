import gradio as gr
from password_strength_checker import check_password_strength

gr.Interface(fn=check_password_strength,
             inputs=gr.Textbox(type="password", label="Enter your password"),
             outputs="text",
             title="Password Strength Checker").launch()