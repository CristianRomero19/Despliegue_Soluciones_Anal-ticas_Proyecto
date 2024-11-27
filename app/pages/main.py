import dash
from dash import Input, Output, html, dcc
import dash_mantine_components as dmc
from dash_iconify import DashIconify
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from app import app

dash._dash_renderer._set_react_version('18.2.0')

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
                dmc.Space(),
                dmc.Space(),
                dmc.Space(),
                dmc.Center(
                    dmc.Divider(label='Overview', labelPosition='center', size='xl')
                ),
                dmc.Space(),
                dmc.Space(),
                dmc.Space(),
                dmc.Space(),
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
                                        children=[
                                            DashIconify(icon="fluent:people-community-20-filled", width=30)
                                        ]
                                    )
                                ),
                                dmc.Group(
                                    align='center',
                                    justify='center',
                                    gap='xs',
                                    style={'margin-top': 10},
                                    children=[
                                        dmc.Text(
                                            'Current Number of Employees',
                                            size='xs',
                                            c='dimmed',
                                            style={'font-family': 'IntegralCF-RegularOblique'}
                                        ),
                                        dmc.Text(
                                            id='totalemp',
                                            size='xl',
                                            style={'font-family': 'IntegralCF-ExtraBold'}
                                        ),
                                        dmc.Text(
                                            'Attrition Rate',
                                            id='attrition_rate',
                                            size='xs',
                                            c='red',
                                            style={'font-family': 'IntegralCF-RegularOblique'}
                                        )
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
                                        children=[
                                            DashIconify(icon="mdi:account-cash", width=30)
                                        ]
                                    )
                                ),
                                dmc.Group(
                                    align='center',
                                    justify='center',
                                    gap='xs',
                                    style={'margin-top': 10},
                                    children=[
                                        dmc.Text(
                                            'Monthly Payroll Cost',
                                            size='xs',
                                            c='dimmed',
                                            style={'font-family': 'IntegralCF-RegularOblique'}
                                        ),
                                        dmc.Text(
                                            id='payroll_cost',
                                            size='xl',
                                            style={'font-family': 'IntegralCF-ExtraBold'}
                                        ),
                                        dmc.Text(
                                            'In USD',
                                            size='xs',
                                            c='dimmed',
                                            style={'font-family': 'IntegralCF-RegularOblique'}
                                        )
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
                                        children=[
                                            DashIconify(icon="mdi:calendar-check", width=30)
                                        ]
                                    )
                                ),
                                dmc.Group(
                                    align='center',
                                    justify='center',
                                    gap='xs',
                                    style={'margin-top': 10},
                                    children=[
                                        dmc.Text(
                                            'Average Tenure (Years)',
                                            size='xs',
                                            c='dimmed',
                                            style={'font-family': 'IntegralCF-RegularOblique'}
                                        ),
                                        dmc.Text(
                                            id='avg_tenure',
                                            size='xl',
                                            style={'font-family': 'IntegralCF-ExtraBold'}
                                        )
                                    ]
                                )
                            ]
                        ),
                    ]
                ),
                dmc.Space(),
                dmc.Space(),
                dmc.Space(),
                dmc.Space(),
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
                                dmc.Title(
                                    'Gender Distribution',
                                    order=4,
                                    style={
                                        'font-family': 'IntegralCF-Regular',
                                        'text-align': 'center',
                                        'color': 'grey',
                                        'letter-spacing': '1px'
                                    }
                                ),
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
                                dmc.Title(
                                    'Age Distribution',
                                    order=4,
                                    style={
                                        'font-family': 'IntegralCF-Regular',
                                        'text-align': 'center',
                                        'color': 'grey',
                                        'letter-spacing': '1px'
                                    }
                                ),
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
                                dmc.Title(
                                    'Department Distribution',
                                    order=4,
                                    style={
                                        'font-family': 'IntegralCF-Regular',
                                        'text-align': 'center',
                                        'color': 'grey',
                                        'letter-spacing': '1px'
                                    }
                                ),
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


@app.callback(Output('totalemp', 'children'),
              Output('attrition_rate', 'children'),
              Output('performance', 'children'),
              Output('pr_above', 'children'),
              Output('jobsatisf', 'children'),
              Output('totaljob', 'children'),
              Input('url', 'pathname'))

def update_card1(n):
    sc = pd.read_csv('./data/Human_Resources.csv')
    sc = sc.infer_objects()

    te = sc['Attrition'].replace('Yes', 1).replace('No', 0).astype(int).mean()
    pr = sc.PerformanceRating.mean()
    pr_above = sc.query('PerformanceRating == 4').shape[0]
    sat = sc.JobSatisfaction.mean()
    atr = sc.query('JobSatisfaction == 4').shape[0]

    return "{:,}".format(sc.EmployeeNumber.nunique()), f'{"{:.2f}%".format(te * 100)} Attrition Rate', "{:,}".format(pr), f'Approx. {pr_above} employees above 3', "${:,.2f}".format(sat), f'{"${:,.2f}".format(atr)} employees above 3'


@app.callback(Output('gender', 'figure'),
              Output('overtime', 'figure'),
              Output('department', 'figure'),
              Input('url', 'pathname'))
def update_graphs(n):
    df = pd.read_csv('./data/Human_Resources.csv')
    sc = df.query('Attrition == "No"')

    # Gender pie chart
    fig = px.pie(
        sc,
        names='Gender',
        color='Gender',
        hole=0.5,
        labels=['Female', 'Male'],
        color_discrete_map={'Male': '#0F203A', 'Female': '#F39A59'}
    )
    fig.update_traces(textposition='outside', textinfo='percent+label+value', hovertemplate="%{customdata[0]}<extra></extra>")
    fig.update_layout(showlegend=False, plot_bgcolor='#fff', paper_bgcolor='#fff', height=300)

    # OverTime bar chart
    hh = df[['OverTime', 'Attrition']].groupby(['OverTime', 'Attrition']).size().to_frame().reset_index()
    fig1 = px.bar(
        hh,
        x='OverTime',
        y=0,
        color='Attrition',
        barmode='group',
        text_auto=True,
        color_discrete_map={'No': '#cbccce', 'Yes': '#174b7d'}
    )
    fig1.update_yaxes(range=[0, hh[0].max() * 1.2], title='# of Employees')
    fig1.update_layout(plot_bgcolor='#fff', paper_bgcolor='#fff', height=300)

    # Department bar chart
    old = df[['Department', 'Attrition']].groupby(['Department', 'Attrition']).size().to_frame().reset_index()
    fig2 = px.bar(
        old,
        x='Department',
        y=0,
        color='Department',
        text_auto=True,
        color_discrete_map={'Research & Development': '#174b7d', 'Human Resources': '#F39A59', 'Sales': '#0F203A'}
    )
    fig2.update_yaxes(range=[0, old[0].max() * 1.2], title='# of Customers')
    fig2.update_layout(plot_bgcolor='#fff', paper_bgcolor='#fff', height=300)

    return fig, fig1, fig2


if __name__ == '__main__':
    app.layout = layout
    app.run_server(debug=True, port=8050)


