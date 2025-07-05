import gradio as gr
import json
import os

# Construct the absolute path to branding.json, which is in the parent directory
branding_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'branding.json'))

with open(branding_path) as f:
    brand_data = json.load(f)["brand"]

def calculate(num1, op, num2):
    if op == "+": return num1 + num2
    elif op == "-": return num1 - num2
    elif op == "*": return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2

gr.Interface(
    fn=calculate,
    inputs=["number", gr.Radio(["+", "-", "*", "/"]), "number"],
    outputs="text",
    title=brand_data["organizationShortName"],
    description=brand_data["slogan"],
    theme=gr.themes.Soft()
).launch()
