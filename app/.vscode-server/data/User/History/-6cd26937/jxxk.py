from dash import Dash, html

app = Dash(__name__)
filename = 'C:\\Users\\Rojan\\Desktop\\ML\\Assignment 1\\car_price_prediction.model'
loaded_model = pickle.load(open(filename, 'rb'))


if __name__ == '__main__':
    app.run(debug=True)
    
    
    