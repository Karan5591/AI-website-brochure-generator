import gradio as gr
from src.brocher_generator import create_broucher

Company_name = gr.Textbox(label = "Company Name")
Company_url = gr.Textbox(label="Company URL")
output_text = gr.Markdown(label= "Response")

view = gr.Interface (
    fn=create_broucher,
    title="Create Company Broucher",
    inputs=[Company_name, Company_url],
    outputs=[output_text],
    examples=[
      ["huggingFace", "https://huggingface.com"]   
    ],
    flagging_mode="never"
)

view.launch(inbrowser=True)