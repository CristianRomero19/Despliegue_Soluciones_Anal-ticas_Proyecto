import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import joblib
import pandas as pd

from app import app

# Cargar el modelo
model = joblib.load('../model/model_attrition.joblib')


# Layout de la aplicación
layout = html.Div([
    html.H1("Enter Employee Details", style={'textAlign': 'center', 'color': 'green'}),
    
    # Tabla de 2 columnas
    html.Table([
        # Fila 1 - Age
        html.Tr([
            html.Td("Age:"),
            html.Td(dcc.Input(id='Age', type='number', placeholder='Enter Age')),
        ]),
        # Fila 2 - BusinessTravel
        html.Tr([
            html.Td("BusinessTravel:"),
            html.Td(dcc.Dropdown(
                id='BusinessTravel',
                options=[
                    {'label': 'Travel Rarely', 'value': 2},
                    {'label': 'Travel Frequently', 'value': 1},
                    {'label': 'Non-Travel', 'value': 0}
                ],
                value='Travel Rarely'
            )),
        ]),
        # Fila 3 - Department
        html.Tr([
            html.Td("Department:"),
            html.Td(dcc.Dropdown(
                id='Department',
                options=[
                    {'label': 'Sales', 'value': 2},
                    {'label': 'Research & Development', 'value': 1},
                    {'label': 'Human Resources', 'value': 0}
                ],
                value='Sales'
            )),
        ]),
        # Fila 4 - DistanceFromHome
        html.Tr([
            html.Td("DistanceFromHome:"),
            html.Td(dcc.Input(id='DistanceFromHome', type='number', placeholder='Distance in km')),
        ]),
        # Fila 5 - Education
        html.Tr([
            html.Td("Education:"),
            html.Td(dcc.Dropdown(
                id='Education',
                options=[
                    {'label': '1', 'value': 1},
                    {'label': '2', 'value': 2},
                    {'label': '3', 'value': 3},
                    {'label': '4', 'value': 4}
                ],
                value=1
            )),
        ]),
        # Fila 6 - EducationField
        html.Tr([
            html.Td("EducationField:"),
            html.Td(dcc.Dropdown(
                id='EducationField',
                options=[
                    {'label': 'Life Sciences', 'value': 1},
                    {'label': 'Human Resources', 'value': 0},
                    {'label': 'Technical Degree', 'value': 5},
                    {'label': 'Other', 'value': 4},
                    {'label': 'Medical', 'value': 3},
                    {'label': 'Marketing', 'value': 2}
                ],
                value='Life Sciences'
            )),
        ]),
        # Fila 7 - Gender
        html.Tr([
            html.Td("Gender:"),
            html.Td(dcc.Dropdown(
                id='Gender',
                options=[
                    {'label': 'Female', 'value': 0},
                    {'label': 'Male', 'value': 1}
                ],
                value='Female'
            )),
        ]),
        # Fila 8 - MaritalStatus
        html.Tr([
            html.Td("MaritalStatus:"),
            html.Td(dcc.Dropdown(
                id='MaritalStatus',
                options=[
                    {'label': 'Single', 'value': 2},
                    {'label': 'Married', 'value': 1},
                    {'label': 'Divorced', 'value': 0}
                ],
                value='Single'
            )),
        ]),
        # Fila 9 - NumCompaniesWorked
        html.Tr([
            html.Td("NumCompaniesWorked:"),
            html.Td(dcc.Input(id='NumCompaniesWorked', type='number', placeholder='number of companies he/she has worked for')),
        ]),
        # Fila 10 - TrainingTimesLastYear
        html.Tr([
            html.Td("TrainingTimesLastYear:"),
            html.Td(dcc.Input(id='TrainingTimesLastYear', type='number', placeholder='Training periods in the last year')),
        ]),
        # Fila 11 - YearsAtCompany
        html.Tr([
            html.Td("YearsAtCompany:"),
            html.Td(dcc.Input(id='YearsAtCompany', type='number', placeholder='Years at company')),
        ]),
    ], style={'margin': 'auto', 'padding': '20px', 'border': '1px solid #ddd', 'width': '50%'}),

    html.Br(),
    
    # Botón para predecir
    html.Div([
        html.Button('Predecir Attrition', id='predict-button', n_clicks=0, style={'backgroundColor': 'green', 'color': 'white'}),
    ], style={'textAlign': 'center'}),  # Centra el botón
    html.Br(),

    # Salida de la predicción
    html.Div([
        html.H3("Predicción: ", id='prediction-output', style={'color': 'green'})
    ], style={'textAlign': 'center'})  # Centra la salida de la predicción
])


@app.callback(
    Output('prediction-output', 'children'),
    Input('predict-button', 'n_clicks'),
    [
        Input('Age', 'value'),
        Input('BusinessTravel', 'value'),
        Input('Department', 'value'),
        Input('DistanceFromHome', 'value'),
        Input('Education', 'value'),
        Input('EducationField', 'value'),
        Input('Gender', 'value'),
        Input('MaritalStatus', 'value'),
        Input('NumCompaniesWorked', 'value'),
        Input('TrainingTimesLastYear', 'value'),
        Input('YearsAtCompany', 'value')
    ]
)
def update_output(n_clicks, Age, BusinessTravel, Department, DistanceFromHome, Education, EducationField, Gender, MaritalStatus, NumCompaniesWorked, TrainingTimesLastYear, YearsAtCompany):
    if n_clicks > 0:
        # Preparar los datos de entrada para el modelo
        input_data = pd.DataFrame({
            'Age': [Age],
            'BusinessTravel': [BusinessTravel],
            'Department': [Department],
            'DistanceFromHome': [DistanceFromHome],
            'Education': [Education],
            'EducationField': [EducationField],
            'Gender': [Gender],
            'MaritalStatus': [MaritalStatus],
            'NumCompaniesWorked': [NumCompaniesWorked],
            'TrainingTimesLastYear': [TrainingTimesLastYear],
            'YearsAtCompany': [YearsAtCompany]
        })

        # Hacer predicción
        prediction = model.predict(input_data)
        
        if prediction[0] == 1:
            return 'Attrition: SI'
        else:
            return 'Attrition: NO'

    return ''

if __name__ == '__main__':
    app.layout = layout
    app.run_server(debug=True, port=8050)