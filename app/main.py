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
                                        dmc.Text('Current Number of Employees', size='l', c='dimmed', fw='bold'),                                       
                                        
                                    ]
                                ),
                                dmc.Group(
                                    align='center',
                                    justify='center',
                                    gap='xs',
                                    style={'margin-top': 2},
                                    children=[
                                        dmc.Text(id='totalemp', size='xl', style={'font-family': 'IntegralCF-ExtraBold'})
                                        
                                    ]
                                ),
                                dmc.Group(
                                    align='center',
                                    justify='center',
                                    gap='xs',
                                    style={'margin-top': 2},
                                    children=[
                                        dmc.Text('Attrition Rate', id='attrition_rate', size='m', c='red')
                                    ]
                                ),
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
                                        dmc.Text('Average Job Satisfaction', size='l', c='dimmed', fw='bold'),
                                        
                                    ]
                                ),
                                dmc.Group(
                                    align='center',
                                    justify='center',
                                    gap='xs',
                                    style={'margin-top': 2},
                                    children=[
                                        dmc.Text(id='sat', size='xl', style={'font-family': 'IntegralCF-ExtraBold'})
                                        
                                    ]
                                ),
                                dmc.Group(
                                    align='center',
                                    justify='center',
                                    gap='xs',
                                    style={'margin-top': 2},
                                    children=[
                                        dmc.Text(id='job_satisf', size='m', c='dimmed')
                                    ]
                                ),
                                
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
                                        dmc.Text('Average Performance Grade', size='l', c='dimmed', fw='bold'),                                        
                                    ]
                                ),
                                dmc.Group(
                                    align='center',
                                    justify='center',
                                    gap='xs',
                                    style={'margin-top': 2},
                                    children=[
                                        dmc.Text(id='avg_performance', size='xl', style={'font-family': 'IntegralCF-ExtraBold'})                                        
                                    ]
                                ),
                                dmc.Group(
                                    align='center',
                                    justify='center',
                                    gap='xs',
                                    style={'margin-top': 2},
                                    children=[
                                        dmc.Text(id='pr_above', size='m', c='dimmed')
                                    ]
                                ),
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
                            withBorder=False,                    
                            p='sm',
                            style={'height': '350px', 'width': '400px'},
                            children=[
                                dmc.Title('Gender Distribution', order=4, style={'font-family': 'IntegralCF-Regular', 'text-align': 'center', 'color': 'grey'}),
                                dcc.Graph(id='gender_figure')
                            ]
                        ),
                        # Segunda gráfica
                        dmc.Paper(
                            radius="md",
                            withBorder=False,                
                            p='sm',
                            style={'height': '350px', 'width': '400px'},
                            children=[
                                dmc.Title('OverTime Distribution', order=4, style={'font-family': 'IntegralCF-Regular', 'text-align': 'center', 'color': 'grey'}),
                                dcc.Graph(id='age_figure')
                            ]
                        ),
                        # Tercera gráfica
                        dmc.Paper(
                            radius="md",
                            withBorder=False,
                            p='sm',
                            style={'height': '350px', 'width': '400px'},
                            children=[
                                dmc.Title('Department Distribution', order=4, style={'font-family': 'IntegralCF-Regular', 'text-align': 'center', 'color': 'grey'}),
                                dcc.Graph(id='department_figure')
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
    Output('gender_figure', 'figure'),
    Output('age_figure', 'figure'),
    Output('department_figure', 'figure'),
    Input('totalemp', 'children')  # Puedes cambiar esto a cualquier Input que necesites
)
def update_graph(input_value):
    # Crear las gráficas
    gender_figure = px.pie(sc, names='Gender', color='Gender', hole=0.5, labels=['Female', 'Male'])
    age_figure = px.bar(hh, x='OverTime', y=0, color='Attrition', barmode='group', text_auto=True)
    department_figure = px.bar(old, x='Department', y=0, color='Attrition', barmode='group', text_auto=True)

    return gender_figure, age_figure, department_figure

@app.callback(
        Output('totalemp', 'children'),
        Output('attrition_rate', 'children'),
        Output('sat', 'children'),
        Output('job_satisf', 'children'),
        Output('avg_performance', 'children'),
        Output('pr_above', 'children'),
        Input('totalemp', 'children')
)


def update_card(input_value):

    attrition_rate = df['Attrition'].replace('Yes', 1).replace('No', 0).astype(int).mean()
    avg_performance = df.PerformanceRating.mean()
    pr_above = df.query('PerformanceRating == 4').shape[0]
    sat = df.JobSatisfaction.mean()
    job_satisf = df.query('JobSatisfaction == 4').shape[0]
    totalemp = df.shape[0]

    return "{:,}".format(totalemp), f'{"{:.2f}%".format(attrition_rate * 100)} Attrition Rate', "{:,.2f}".format(sat), f'{"{:,}".format(job_satisf)} employees above 3', "{:,.2f}".format(avg_performance), f'Approx. {pr_above} employees above 3'

if __name__ == '__main__':
    app.layout = layout
    app.run_server(debug=True, port=8050)
