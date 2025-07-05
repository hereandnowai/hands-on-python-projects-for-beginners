import gradio as gr
import json
import os
from die_rolling import roll_die

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

def display_die(die_number):
    die_faces = {
        1: 'https://upload.wikimedia.org/wikipedia/commons/1/1b/Dice-1-b.svg',
        2: 'https://upload.wikimedia.org/wikipedia/commons/5/5f/Dice-2-b.svg',
        3: 'https://upload.wikimedia.org/wikipedia/commons/b/b1/Dice-3-b.svg',
        4: 'https://upload.wikimedia.org/wikipedia/commons/f/fd/Dice-4-b.svg',
        5: 'https://upload.wikimedia.org/wikipedia/commons/0/08/Dice-5-b.svg',
        6: 'https://upload.wikimedia.org/wikipedia/commons/2/26/Dice-6-b.svg',
    }
    return die_faces.get(die_number)

with gr.Blocks(theme=theme) as demo:
    gr.Image(brand_data["logo"]["title"], height=100, width=400, container=False, show_label=False)
    gr.Markdown(f"## {brand_data['slogan']}")

    with gr.Row():
        roll_btn = gr.Button("Roll the Die", variant="primary")

    with gr.Row():
        die_image = gr.Image(label="Die Face", interactive=False, height=200, width=200)

    def roll_and_display():
        number = roll_die()
        image_path = display_die(number)
        return image_path

    roll_btn.click(fn=roll_and_display, inputs=None, outputs=die_image)

    # Footer with social media links
    footer_html = f"<div style='text-align: center; margin-top: 20px;'>"
    for platform, url in brand_data["socialMedia"].items():
        footer_html += f"<a href='{url}' target='_blank' style='margin: 0 10px; text-decoration: none; color: {brand_data['colors']['primary']};'>{platform.capitalize()}</a>"
    footer_html += "</div>"
    gr.HTML(footer_html)

demo.launch(favicon_path=brand_data["logo"]["favicon"])