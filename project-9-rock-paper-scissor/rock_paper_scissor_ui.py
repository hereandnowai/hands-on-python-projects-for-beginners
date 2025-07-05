import gradio as gr
import json
import os
from rock_paper_scissor import play_round

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

    gr.Markdown("### Choose your move!")
    user_choice = gr.Radio(["rock", "paper", "scissor"], label="Your Move")
    play_button = gr.Button("Play!")
    game_result = gr.Textbox(label="Result")

    play_button.click(fn=play_round, inputs=user_choice, outputs=game_result)

    # Footer with social media links
    footer_html = f"<div style='text-align: center; margin-top: 20px;'>"
    for platform, url in brand_data["socialMedia"].items():
        footer_html += f"<a href='{url}' target='_blank' style='margin: 0 10px; text-decoration: none; color: {brand_data['colors']['primary']};'>{platform.capitalize()}</a>"
    footer_html += "</div>"
    gr.HTML(footer_html)

demo.launch(favicon_path=brand_data["logo"]["favicon"])