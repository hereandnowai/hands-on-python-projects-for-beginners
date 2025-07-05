import gradio as gr
import json
import os
from tic_tac_toe import get_board_display, play_move, reset_game

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

custom_css = """
#tic_tac_toe_board_textbox textarea {
    font-family: monospace !important;
}
"""

with gr.Blocks(theme=theme, css=custom_css) as demo:
    gr.Image(brand_data["logo"]["title"], height=100, width=400, container=False, show_label=False)
    gr.Markdown(f"## {brand_data['slogan']}")

    game_board = gr.Textbox(elem_id="tic_tac_toe_board_textbox", label="Tic Tac Toe Board", interactive=False, lines=5, max_lines=5)
    game_message = gr.Textbox(label="Game Status", interactive=False)

    with gr.Row():
        for i in range(1, 10):
            # Using a lambda to capture the current value of i
            btn = gr.Button(str(i), elem_id=f"btn_{i}")
            btn.click(fn=lambda pos=i: play_move(pos), inputs=None, outputs=[game_board, game_message])

    reset_button = gr.Button("Reset Game")
    reset_button.click(fn=reset_game, inputs=None, outputs=[game_board, game_message])

    # Initialize board on load
    demo.load(fn=reset_game, inputs=None, outputs=[game_board, game_message])

    # Footer with social media links
    footer_html = f"<div style='text-align: center; margin-top: 20px;'>"
    for platform, url in brand_data["socialMedia"].items():
        footer_html += f"<a href='{url}' target='_blank' style='margin: 0 10px; text-decoration: none; color: {brand_data['colors']['primary']};'>{platform.capitalize()}</a>"
    footer_html += "</div>"
    gr.HTML(footer_html)

demo.launch(favicon_path=brand_data["logo"]["favicon"])