import gradio as gr
import json
import os
from hangman import initialize_game, process_guess, get_hangman_drawing

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
#hangman_image_textbox textarea {
    font-family: monospace !important;
}
"""

with gr.Blocks(theme=theme, css=custom_css) as demo:
    gr.Image(brand_data["logo"]["title"], height=100, width=400, container=False, show_label=False)
    gr.Markdown(f"## {brand_data['slogan']}")

    # Game state components (hidden)
    current_display_word = gr.State()
    current_chances = gr.State()
    current_message = gr.State()

    with gr.Row():
        with gr.Column():
            hangman_image = gr.Textbox(elem_id="hangman_image_textbox", label="Hangman", interactive=False, lines=8, max_lines=8)
            game_message = gr.Textbox(label="Game Status", interactive=False)
        with gr.Column():
            display_word_output = gr.Textbox(label="Word to Guess", interactive=False)
            chances_output = gr.Textbox(label="Chances Left", interactive=False)
            guess_input = gr.Textbox(label="Enter your guess (single letter)")
            guess_button = gr.Button("Guess")
            new_game_button = gr.Button("New Game")

    def start_new_game():
        display_word, chances, drawing, message = initialize_game()
        return display_word, chances, drawing, message

    def make_a_guess(character):
        display_word, chances, drawing, message = process_guess(character.lower())
        return display_word, chances, drawing, message

    # Event handlers
    guess_button.click(
        fn=make_a_guess,
        inputs=guess_input,
        outputs=[display_word_output, chances_output, hangman_image, game_message]
    )

    new_game_button.click(
        fn=start_new_game,
        inputs=None,
        outputs=[display_word_output, chances_output, hangman_image, game_message]
    )

    # Initialize game on load
    demo.load(
        fn=start_new_game,
        inputs=None,
        outputs=[display_word_output, chances_output, hangman_image, game_message]
    )

    # Footer with social media links
    footer_html = f"<div style='text-align: center; margin-top: 20px;'>"
    for platform, url in brand_data["socialMedia"].items():
        footer_html += f"<a href='{url}' target='_blank' style='margin: 0 10px; text-decoration: none; color: {brand_data['colors']['primary']};'>{platform.capitalize()}</a>"
    footer_html += "</div>"
    gr.HTML(footer_html)

demo.launch(favicon_path=brand_data["logo"]["favicon"])