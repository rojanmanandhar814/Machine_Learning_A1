from dash import Dash, html
from dash import dcc, html
from dash.dependencies import Input, Output
import joblib

app = Dash(__name__)

app.layout = html.Div([
    html.Div(children='Hello World')
])

if __name__ == '__main__':
    app.run(debug=True)
    
    


# Load the model from the .model file
model = joblib.load('model.model')  # Update with your model's file name

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Car Price Prediction"),
    
    html.Label("Mileage (km)"),
    dcc.Input(id='input-mileage', type='number', value=10000, step=1000),
    html.Label("Engine Size (cc)"),
    dcc.Input(id='input-engine-size', type='number', value=1600, step=100),
    html.Label("Max Power (hp)"),
    dcc.Input(id='input-max-power', type='number', value=120, step=10),
    
    html.Div(id='predicted-price'),
])

@app.callback(
    Output('predicted-price', 'children'),
    [Input('input-mileage', 'value'),
     Input('input-engine-size', 'value'),
     Input('input-max-power', 'value')]
)
def update_predicted_price(mileage, engine_size, max_power):
    input_data = [mileage, engine_size, max_power]
    predicted_price = model.predict([input_data])[0]

    return f'Predicted Price: ${predicted_price:.2f}'

if __name__ == '__main__':
    app.run_server(debug=True)   