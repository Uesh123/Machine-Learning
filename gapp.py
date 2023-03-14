import gradio as gr

def gapp_fun (text):
    return text.split()

ui = gr.Interface(
    fn = gapp_fun,
    inputs = 'text',
    outputs = 'text',
)

if __name__=="__main__":
    ui.launch()