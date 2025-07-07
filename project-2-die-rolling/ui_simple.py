import gradio as gr
from die_rolling import roll_die

# Function to get the die face image URL
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

with gr.Blocks() as demo:
    gr.Markdown("## Click the button to roll the die!")
    roll_btn = gr.Button("Roll the Die!")
    output_image = gr.Image(label="Result", height=300, width=300)

    def roll_and_show_image():
        die_number = roll_die()
        return display_die(die_number)

    roll_btn.click(fn=roll_and_show_image, inputs=None, outputs=output_image)

demo.launch()