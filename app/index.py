import dash
from dash import dcc, html, Input, Output
import dash_iconify as dicon
import joblib
import dash_mantine_components as dmc
from dash_iconify import DashIconify
from dash_mantine_components import MantineProvider
import plotly.express as px
import main
import attrition
import pandas as pd
from app import app


# Establecer la versión de React utilizada por Dash (esto es opcional, pero puedes dejarlo si es necesario)
dash._dash_renderer._set_react_version('18.2.0')

# Función para crear un enlace de navegación
def create_nav_link(icon, label, href):
    return dcc.Link(
        dmc.Group(
            flex='row',
            align='center',
            gap=10,
            children=[
                dmc.ThemeIcon(
                    DashIconify(icon=icon, width=18),
                    size=25,
                    radius=5,
                    c='indigo',
                    variant="filled"
                ),
                dmc.Text(label, size="sm", c="gray")
            ]
        ),
        href=href,
        style={"textDecoration": "none"},
    )

# Asignar el layout correctamente, envuelto por MantineProvider
app.layout = MantineProvider(
    theme={"colorScheme": "light"},  # Puedes ajustar el tema aquí
    children=html.Div(
        children=[
            # Barra lateral de navegación con HTML y CSS
            html.Div(
                children=[
                    html.Div(
                        className='sidebar',
                        children=[
                            html.Div(
                                children=[
                                    create_nav_link("mdi:home", "Home", "/home"),
                                    create_nav_link("mdi:people", "Employee Base", "/main"),
                                    create_nav_link("mdi:magnify", "Attrition Prediction", "/attrition"),
                                ]
                            )
                        ]
                    )
                ],
                className="container"
            ),
            # El contenido de la página cambiará aquí
            dcc.Location(id='url', refresh=False),  # Manejador de URL
            html.Div(id='page-content')  # Contenido de la página que se actualiza
        ]
    )
)

# Callback para actualizar el contenido según la URL
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    # Cambiar contenido basado en la URL
    if pathname == '/main':
        return main.layout
    elif pathname == '/attrition':
        return attrition.layout
    elif pathname == '/home' or pathname == '/':
        return html.Div("Home Page")
    else:
        return html.Div("404 Page Not Found")


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run_server(debug=True)






