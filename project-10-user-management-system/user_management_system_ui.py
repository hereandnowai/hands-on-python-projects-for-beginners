import gradio as gr
import json
import os
from user_management_system import add_entry, update_entry, delete_entry, search_entry, get_all_entries_display, reset_database, SRNO, NAME, AGE, GENDER, OCCUPATION

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

    with gr.Tab("Add Entry"):
        with gr.Row():
            add_name = gr.Textbox(label="Name")
            add_age = gr.Number(label="Age")
            add_gender = gr.Radio(["Male", "Female", "Other"], label="Gender")
            add_occupation = gr.Textbox(label="Occupation")
        add_button = gr.Button("Add Entry")
        add_output = gr.Textbox(label="Status")
        add_button.click(fn=add_entry, inputs=[add_name, add_age, add_gender, add_occupation], outputs=add_output)

    with gr.Tab("Update Entry"):
        with gr.Row():
            update_search_by = gr.Radio([SRNO, NAME, AGE, GENDER, OCCUPATION], label="Search By")
            update_search_value = gr.Textbox(label="Search Value")
        gr.Markdown("### Enter New Details:")
        with gr.Row():
            update_name = gr.Textbox(label="New Name")
            update_age = gr.Number(label="New Age")
            update_gender = gr.Radio(["Male", "Female", "Other"], label="New Gender")
            update_occupation = gr.Textbox(label="New Occupation")
        update_button = gr.Button("Update Entry")
        update_output = gr.Textbox(label="Status")
        update_button.click(fn=update_entry, inputs=[update_search_by, update_search_value, update_name, update_age, update_gender, update_occupation], outputs=update_output)

    with gr.Tab("Delete Entry"):
        with gr.Row():
            delete_search_by = gr.Radio([SRNO, NAME, AGE, GENDER, OCCUPATION], label="Search By")
            delete_search_value = gr.Textbox(label="Search Value")
        delete_button = gr.Button("Delete Entry")
        delete_output = gr.Textbox(label="Status")
        delete_button.click(fn=delete_entry, inputs=[delete_search_by, delete_search_value], outputs=delete_output)

    with gr.Tab("Search Entry"):
        with gr.Row():
            search_search_by = gr.Radio([SRNO, NAME, AGE, GENDER, OCCUPATION], label="Search By")
            search_search_value = gr.Textbox(label="Search Value")
        search_button = gr.Button("Search Entry")
        search_output = gr.Textbox(label="Search Result")
        search_button.click(fn=search_entry, inputs=[search_search_by, search_search_value], outputs=search_output)

    with gr.Tab("Display All Entries"):
        display_all_button = gr.Button("Display All Entries")
        display_all_output = gr.Textbox(label="All Entries")
        display_all_button.click(fn=get_all_entries_display, inputs=None, outputs=display_all_output)

    with gr.Tab("Reset Database"):
        reset_button = gr.Button("Reset Database")
        reset_output = gr.Textbox(label="Reset Status")
        reset_button.click(fn=reset_database, inputs=None, outputs=reset_output)

    # Footer with social media links
    footer_html = f"<div style='text-align: center; margin-top: 20px;'>"
    for platform, url in brand_data["socialMedia"].items():
        footer_html += f"<a href='{url}' target='_blank' style='margin: 0 10px; text-decoration: none; color: {brand_data['colors']['primary']};'>{platform.capitalize()}</a>"
    footer_html += "</div>"
    gr.HTML(footer_html)

demo.launch(favicon_path=brand_data["logo"]["favicon"])