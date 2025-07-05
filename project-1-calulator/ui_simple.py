from calculator import calculate
import gradio as gr
import json
import os

# Construct the absolute path to branding.json, which is in the parent directory
branding_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'branding.json'))

with open(branding_path) as f:
    brand_data = json.load(f)["brand"]

gr.Interface(
    fn=calculate,
    inputs=[gr.Number(label="First Number"), gr.Radio(["+", "-", "*", "/"], label="Operation"), gr.Number(label="Second Number")],
    outputs=gr.Textbox(label="Result"),
    title=brand_data["organizationShortName"],
    description=brand_data["slogan"],
    theme=gr.themes.Soft()
).launch()