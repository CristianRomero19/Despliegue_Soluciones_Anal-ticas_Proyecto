import dash
from dash import dcc, html

dash._dash_renderer._set_react_version('18.2.0')

# Definir el layout de la página
layout = html.Div(
    children=[
        html.H1("¡Hola Mundo!"),  # Título principal
        html.P("Este es un dashboard básico utilizando Dash.")  # Parrafo con descripción
    ]
)

# Ejecutar la aplicación en el servidor
if __name__ == '__main__':
    app.run_server(debug=True)
