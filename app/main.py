import dash
from dash import Input, Output, html, dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import pandas as pd
import plotly.express as px

from app import app

dash._dash_renderer._set_react_version('18.2.0')

# Cargar datos fuera de las callbacks
df = pd.read_csv('./data/Human_Resources.csv')
sc = df.query('Attrition == "No"')
df = df.infer_objects()

hh = df[['OverTime', 'Attrition']].groupby(['OverTime', 'Attrition']).size().to_frame().reset_index()
old = df[['Department', 'Attrition']].groupby(['Department', 'Attrition']).size().to_frame().reset_index()


# Layout del dashboard
layout = html.Div(
    style={'margin-top': '30px'},
    children=[  
        dmc.MantineProvider(
            theme={"colorScheme": "light"},
            children=[  
                dmc.Center(
                    dmc.Title(
                        children='Base Empleados',
                        order=3,
                        style={'font-family': 'IntegralCF-ExtraBold', 'text-align': 'center', 'color': 'slategray'}
                    )
                ),
                dmc.Space(),
                dmc.Center(
                    dmc.Divider(label='Overview', labelPosition='center', size='xl')
                ),
                dmc.Group(
                    align='center',
                    justify='center',
                    grow=True,
                    gap='md',
                    children=[  
                        # Primera Tarjeta
                        dmc.Paper(
                            radius="md",
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height': '175px', 'width': '300px'},
                            children=[
                                dmc.Center(
                                    dmc.ThemeIcon(
                                        size=50,
                                        radius="xl",
                                        color="violet",
                                        variant="light",
                                        children=[DashIconify(icon="fluent:people-community-20-filled", width=30)]
                                    )
                                ),
                                dmc.Group(
                                    align='center',
                                    justify='center',
                                    gap='xs',
                                    style={'margin-top': 10},
                                    children=[
                                        dmc.Text('Current Number of Employees', size='xs', c='dimmed'),
                                        dmc.Text(id='totalemp', size='xl', style={'font-family': 'IntegralCF-ExtraBold'}),
                                        dmc.Text('Attrition Rate', id='attrition_rate', size='xs', c='red')
                                    ]
                                )
                            ]
                        ),
                        # Segunda Tarjeta
                        dmc.Paper(
                            radius="md",
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height': '175px', 'width': '300px'},
                            children=[
                                dmc.Center(
                                    dmc.ThemeIcon(
                                        size=50,
                                        radius="xl",
                                        color="blue",
                                        variant="light",
                                        children=[DashIconify(icon="mdi:account-cash", width=30)]
                                    )
                                ),
                                dmc.Group(
                                    align='center',
                                    justify='center',
                                    gap='xs',
                                    style={'margin-top': 10},
                                    children=[
                                        dmc.Text('Monthly Payroll Cost', size='xs', c='dimmed'),
                                        dmc.Text(id='payroll_cost', size='xl', style={'font-family': 'IntegralCF-ExtraBold'}),
                                        dmc.Text('In USD', size='xs', c='dimmed')
                                    ]
                                )
                            ]
                        ),
                        # Tercera Tarjeta
                        dmc.Paper(
                            radius="md",
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height': '175px', 'width': '300px'},
                            children=[
                                dmc.Center(
                                    dmc.ThemeIcon(
                                        size=50,
                                        radius="xl",
                                        color="green",
                                        variant="light",
                                        children=[DashIconify(icon="mdi:calendar-check", width=30)]
                                    )
                                ),
                                dmc.Group(
                                    align='center',
                                    justify='center',
                                    gap='xs',
                                    style={'margin-top': 10},
                                    children=[
                                        dmc.Text('Average Tenure (Years)', size='xs', c='dimmed'),
                                        dmc.Text(id='avg_tenure', size='xl', style={'font-family': 'IntegralCF-ExtraBold'})
                                    ]
                                )
                            ]
                        ),
                    ]
                ),
                dmc.Center(
                    dmc.Divider(label='Estadísticas descriptivas', labelPosition='center', size='xl')
                ),
                dmc.Group(
                    align='center',
                    justify='center',
                    grow=True,
                    gap='md',
                    children=[  
                        # Primera gráfica
                        dmc.Paper(
                            radius="md",
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height': '350px', 'width': '400px'},
                            children=[
                                dmc.Title('Gender Distribution', order=4, style={'font-family': 'IntegralCF-Regular', 'text-align': 'center', 'color': 'grey'}),
                                dcc.Graph(id='gender')
                            ]
                        ),
                        # Segunda gráfica
                        dmc.Paper(
                            radius="md",
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height': '350px', 'width': '400px'},
                            children=[
                                dmc.Title('OverTime Distribution', order=4, style={'font-family': 'IntegralCF-Regular', 'text-align': 'center', 'color': 'grey'}),
                                dcc.Graph(id='age')
                            ]
                        ),
                        # Tercera gráfica
                        dmc.Paper(
                            radius="md",
                            withBorder=True,
                            shadow='xs',
                            p='sm',
                            style={'height': '350px', 'width': '400px'},
                            children=[
                                dmc.Title('Department Distribution', order=4, style={'font-family': 'IntegralCF-Regular', 'text-align': 'center', 'color': 'grey'}),
                                dcc.Graph(id='department')
                            ]
                        ),
                    ]
                ),
                dmc.Space(h=50)
            ]
        )
    ]
)

# Callback para actualizar las gráficas
@app.callback(
    Output('gender', 'figure'),
    Output('age', 'figure'),
    Output('department', 'figure'),
    Input('totalemp', 'children')  # Puedes cambiar esto a cualquier Input que necesites
)
def update_graph(input_value):
    # Crear las gráficas
    gender_figure = px.pie(sc, names='Gender', color='Gender', hole=0.5, labels=['Female', 'Male'], title='Gender Distribution')
    age_figure = px.bar(hh, x='OverTime', y=0, color='Attrition', barmode='group', text_auto=True, title='OverTime Distribution')
    department_figure = px.bar(old, x='Department', y=0, color='Attrition', barmode='group', text_auto=True, title='Department Distribution')

    return gender_figure, age_figure, department_figure


if __name__ == '__main__':
    app.layout = layout
    app.run_server(debug=True, port=8050)
