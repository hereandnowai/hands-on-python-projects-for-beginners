import gradio as gr
from die_rolling import roll_die

# Function to get the die face character
def display_die(die_number):
    die_faces = {
        1: '⚀',
        2: '⚁',
        3: '⚂',
        4: '⚃',
        5: '⚄',
        6: '⚅',
    }
    return die_faces.get(die_number)

with gr.Blocks() as demo:
    gr.Markdown("## Click the button to roll the die!")
    roll_btn = gr.Button("Roll the Die!")
    output_html = gr.HTML("<div style='font-size: 600px; text-align: center; margin: 20px;'>🎲</div>")

    def roll_and_show_die():
        die_number = roll_die()
        die_char = display_die(die_number)
        return f"<div style='font-size: 600px; text-align: center; margin: 20px;'>{die_char}</div>"

    roll_btn.click(fn=roll_and_show_die, inputs=None, outputs=output_html)

demo.launch()