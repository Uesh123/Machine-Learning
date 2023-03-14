import gradio as gr
import pandas as pd
import numpy as np
from joblib import load

def predict_price(
    symboling ,normalized_losses, make ,
    fuel_type,aspiration,num_of_doors,body_style,           
    drive_wheels,engine_location,wheel_base,         
    length,width,height,                   
    curb_weight,engine_type,num_of_cylinders,         
    engine_size,fuel_system,bore,                      
    stroke,compression_ratio,horsepower,                
    peak_rpm,city_mpg,highway_mpg                 
):
    
# load model
    model = load('automobile_price_prediction.jb')

    # Create a dict array from the parameters
    data = {
        'symboling': [symboling],
        'normalized-losses': [normalized_losses],
        'make': [make],
        'fuel-type': [fuel_type],
        'aspiration': [aspiration],
        'num-of-doors': [num_of_doors],
        'body-style': [body_style],
        'drive-wheels': [drive_wheels],
        'engine-location': [engine_location],
        'wheel-base': [wheel_base],
        'length': [length],
        'width': [width],
        'height': [height],
        'curb-weight': [curb_weight],
        'engine-type': [engine_type],
        'num-of-cylinders': [num_of_cylinders],
        'engine-size': [engine_size],
        'fuel-system': [fuel_system],
        'bore': [bore],
        'stroke': [stroke],
        'compression-ratio': [compression_ratio],
        'horsepower': [horsepower],
        'peak-rpm': [peak_rpm],
        'city-mpg': [city_mpg],
        'highway-mpg': [highway_mpg],
    }
    Xinp = pd.DataFrame(data)
    print(Xinp)

    # Predict the price
    price = model.predict(Xinp)

    # return the price
    return price[0]

# Create the gradio interface

ui = gr.Interface(
    fn = predict_price,
    inputs = [
        gr.inputs.Textbox(placeholder='symboling', default=0, numeric=True,label='Symboling'),
        gr.inputs.Textbox(placeholder='normalized_losses', default=100, numeric=True,label='Normalized Losses'),
        gr.inputs.Textbox(placeholder='Make', default='audi',label='make'),
        gr.inputs.Textbox(placeholder='Fuel Type', default='gas',label='fuel'),
        gr.inputs.Textbox(placeholder='Aspiration', default='std',label='aspiration'),
        gr.inputs.Textbox(placeholder='Number of Doors', default='two',label='doors'),
        gr.inputs.Textbox(placeholder='Body Style', default='sedan',label='body'),
        gr.inputs.Textbox(placeholder='Drive Wheels', default='fwd',label='wheels'),
        gr.inputs.Textbox(placeholder='Engine Location', default='front',label='engloc'),
        gr.inputs.Textbox(placeholder='Wheel Base', default=100, numeric=True,label='wheelbase'),
        gr.inputs.Textbox(placeholder='Length', default=100, numeric=True,label='length'),
        gr.inputs.Textbox(placeholder='Width', default=100, numeric=True,label='width'),
        gr.inputs.Textbox(placeholder='Height', default=100, numeric=True,label='height'),
        gr.inputs.Textbox(placeholder='Curb Weight', default=100, numeric=True,label='curbweight'),
        gr.inputs.Textbox(placeholder='Engine Type', default='dohc',label='engtype'),
        gr.inputs.Textbox(placeholder='Number of Cylinders', default=4, numeric=True,label='cyl'),
        gr.inputs.Textbox(placeholder='Engine Size', default=100, numeric=True,label='engsize'),
        gr.inputs.Textbox(placeholder='Fuel System', default='mpfi',label='fuelsys'),
        gr.inputs.Textbox(placeholder='Bore', default=100, numeric=True,label='bore'),
        gr.inputs.Textbox(placeholder='Stroke', default=100, numeric=True,label='stroke'),
        gr.inputs.Textbox(placeholder='Compression Ratio', default=100, numeric=True,label='compratio'),
        gr.inputs.Textbox(placeholder='Horsepower', default=100, numeric=True,label='hp'),
        gr.inputs.Textbox(placeholder='Peak RPM', default=100, numeric=True,label='peakrpm'),
        gr.inputs.Textbox(placeholder='City MPG', default=100, numeric=True,label='citympg'),
        gr.inputs.Textbox(placeholder='Highway MPG', default=100, numeric=True,label='highwaympg'),
],
    outputs = "text",
)

if __name__ == "__main__":
    ui.launch(share=True)