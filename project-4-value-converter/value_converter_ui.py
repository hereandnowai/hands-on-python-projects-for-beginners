import gradio as gr
import json
import os
from value_converter import convert_celsius_to_fahrenheit, convert_fahrenheit_to_celsius, convert_currency_api, convert_cm_to_feet_inches, convert_feet_inches_to_cm

# Construct the absolute path to branding.json
branding_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'branding.json'))

with open(branding_path) as f:
    brand_data = json.load(f)["brand"]

# Define the theme with the custom font
theme = gr.themes.Soft(
    primary_hue="yellow",
    secondary_hue="teal",
    font=gr.themes.GoogleFont("Chau Philomene One")
)

with gr.Blocks(theme=theme) as demo:
    gr.Image(brand_data["logo"]["title"], height=100, width=400, container=False, show_label=False)
    gr.Markdown(f"## {brand_data['slogan']}")

    with gr.Tab("Temperature Converter"):
        with gr.Row():
            temp_input = gr.Number(label="Temperature")
            temp_unit = gr.Radio(["Celsius", "Fahrenheit"], label="Unit")
        temp_output = gr.Textbox(label="Converted Temperature")
        temp_button = gr.Button("Convert Temperature")

        def temp_conversion(temp, unit):
            if unit == "Celsius":
                return f"{convert_celsius_to_fahrenheit(temp):.2f} Fahrenheit"
            else:
                return f"{convert_fahrenheit_to_celsius(temp):.2f} Celsius"
        temp_button.click(fn=temp_conversion, inputs=[temp_input, temp_unit], outputs=temp_output)

    with gr.Tab("Currency Converter"):
        with gr.Row():
            amount_input = gr.Number(label="Amount")
            from_currency_input = gr.Textbox(label="From Currency (e.g., USD)")
            to_currency_input = gr.Textbox(label="To Currency (e.g., EUR)")
        currency_output = gr.Textbox(label="Converted Amount")
        currency_button = gr.Button("Convert Currency")

        def currency_conversion(amount, from_curr, to_curr):
            result = convert_currency_api(amount, from_curr, to_curr)
            if "Error" in result or "Invalid" in result or "Network" in result:
                return result
            return f"{amount} {from_curr.upper()} = {result} {to_curr.upper()}"
        currency_button.click(fn=currency_conversion, inputs=[amount_input, from_currency_input, to_currency_input], outputs=currency_output)

    with gr.Tab("Length Converter"):
        with gr.Row():
            length_type = gr.Radio(["CM to Ft/In", "Ft/In to CM"], label="Conversion Type")
            cm_input = gr.Number(label="Centimeters (if CM to Ft/In)")
            feet_input = gr.Number(label="Feet (if Ft/In to CM)")
            inches_input = gr.Number(label="Inches (if Ft/In to CM)")
        length_output = gr.Textbox(label="Converted Length")
        length_button = gr.Button("Convert Length")

        def length_conversion(conv_type, cm, feet, inches):
            if conv_type == "CM to Ft/In":
                return convert_cm_to_feet_inches(cm)
            else:
                return convert_feet_inches_to_cm(feet, inches)
        length_button.click(fn=length_conversion, inputs=[length_type, cm_input, feet_input, inches_input], outputs=length_output)

    # Footer with social media links
    footer_html = f"<div style='text-align: center; margin-top: 20px;'>"
    for platform, url in brand_data["socialMedia"].items():
        footer_html += f"<a href='{url}' target='_blank' style='margin: 0 10px; text-decoration: none; color: {brand_data['colors']['primary']};'>{platform.capitalize()}</a>"
    footer_html += "</div>"
    gr.HTML(footer_html)

demo.launch(favicon_path=brand_data["logo"]["favicon"])