import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np



N = 100                            #            grid discretization
m_min = 0                          # kg         minimum honey's mass
m_max_m = 12                       # kg         maximum honey's mass
m_max_us = 25                      # lb         maximum honey's mass
m_step_m = 0.5                     # kg         honey's mass' step
m_step_us = 1                      # lb         honey's mass' step
a_min = 0                          # L          minimum water's volume
a_max_m = 30                       # L          maximum water's volume
a_max_us = 7                       # gal        maximum water's volume
a_step_m = 1                       # L          water's volume's step
a_step_us = 0.5                    # gal        water's volume's step
m_gravity_0 = 1.4                  # kg/L       default honey's gravity
m_gravity_min = 1.2                # kg/L       minimum honey's gravity
m_gravity_max = 1.6                # kg/L       maximum honey's gravity
m_gravity_step = 0.01              # kg/L       honey's gravity's step
m_gravity_step_label = 0.05        # kg/L       honey's gravity's step for the ticks
a_gravity = 1                      # kg/L       water's gravity
q_min_m = 1                        # L          minimum produced quantity
q_min_us = 0.5                     # gal        minimum produced quantity
q_max_m = 30                       # L          maximum produced quantity
q_max_us = 7                       # gal        maximum produced quantity
q_step_m = 1                       # L          produced quantity's step
q_step_us = 0.5                    # gal        produced quantity's step
sg_min = 1.000                     # kg/L       minimum start gravity
sg_max = 1.240                     # kg/L       maximum start gravity
sg_step = 0.010                    # kg/L       start gravity's step
pabv_min = 0.01                    # %          minimum potential percentage of alcohol by volume
pabv_max = 0.32                    # %          maximum potential percentage of alcohol by volume
pabv_step = 0.01                   # %          potential percentage's of alcohol by volume step
q_label = 'Produced quantity'      #            produced quantity's label
q_unit = 'L'                       #            produced quantity's unit
sg_label = 'Start gravity'         #            start gravity's label
sg_unit = 'kg/L'                   #            start gravity's unit
pabv_label = 'Alcohol by volume'   #            potential percentage's of alcohol by volume label
pabv_unit = ''                     #            potential percentage's of alcohol by volume unit
q_format = '.0f'                   #            produced quantity's format viewed on the graph
q_hoverformat = '.1f'              #            produced quantity's format viewed by hover
sg_format = '.3f'                  #            start gravity's format viewed on the graph
sg_hoverformat = '.3f'             #            start gravity's format viewed by hover
pabv_format = '%.0f'               #            potential percentage's of alcohol by volume format viewed on the graph
pabv_hoverformat = '.3p'           #            potential percentage's of alcohol by volume format viewed by hover





blue = '#6683f3'
green = '#57bdc9'
yellow = '#e5e467'
orange = '#ff9266'
red = '#de7677'
grey = '#e0e1f5'
black = '#212121'
fontsize = 18
fontfamily = 'Tahoma'




app = dash.Dash()

app.layout = html.Div([html.Div([html.P('Honey\'s gravity',
                                        style = dict(fontFamily = fontfamily,
                                                     fontSize = fontsize)),

                                 html.Div([dcc.Slider(id = 'gravity_slider',
                                                      min = m_gravity_min,
                                                      max = m_gravity_max,
                                                      step = m_gravity_step,
                                                      value = m_gravity_0,
                                                      marks = {n: label for n, label in zip(np.round(np.arange(m_gravity_min, m_gravity_max + m_gravity_step_label, m_gravity_step_label), 2),
                                                                                            [str(x) for x in np.round(np.arange(m_gravity_min, m_gravity_max + m_gravity_step_label, m_gravity_step_label), 2).tolist()])})],
                                          style = dict(width = '50%')),

                                 html.P(id = 'gravity_value',
                                        style = dict(fontFamily = fontfamily,
                                                     fontSize = fontsize)),

                                 dcc.RadioItems(id = 'units_button',
                                                options = [dict(label = 'Metric', value = 'metric'),
                                                           dict(label = 'US', value = 'US')],
                                                value = 'metric',
                                                style = dict(fontFamily = fontfamily,
                                                             fontSize = fontsize))],

                                style = dict(flex_direction = 'row-reverse')),

                       html.Div(dcc.Graph(id = 'main_graph',
                                          figure = dict(data = [],
                                                        layout = go.Layout(plot_bgcolor = black)),
                                          style = dict(height = 1000)))])



@app.callback(Output('main_graph', 'figure'),
              [Input('gravity_slider', 'value'),
               Input('units_button', 'value')])
def update_graph(density_value, unit):

    if unit == 'metric':
        kgtolb = 1
        ltogal = 1
        mass_unit = 'kg'
        volume_unit = 'L'
        q_unit = 'L'
        q_format = '.0f'
        m_max = m_max_m
        m_step = m_step_m
        a_max = a_max_m
        a_step = a_step_m
        q_min = q_min_m
        q_max = q_max_m
        q_step = q_step_m
    else:
        kgtolb = 2.20462
        ltogal = 0.264172
        mass_unit = 'lb'
        volume_unit = 'gal'
        q_unit = 'gal'
        q_format = '.1f'
        m_max = m_max_us
        m_step = m_step_us
        a_max = a_max_us
        a_step = a_step_us
        q_min = q_min_us
        q_max = q_max_us
        q_step = q_step_us


    m = np.linspace(m_min, m_max, N)
    a = np.linspace(a_min, a_max, N)
    MM, AA = np.meshgrid(m, a)

    QQ = AA + MM / (density_value * kgtolb / ltogal)
    SG = (AA*(a_gravity*kgtolb/ltogal)**2 + MM*(density_value*kgtolb/ltogal))/(AA*(a_gravity*kgtolb/ltogal) + MM)/kgtolb*ltogal
    PABV = (SG - 1) / 7.5 * 10

    QQ[PABV > pabv_max] = None
    SG[QQ > q_max] = None
    PABV[QQ > q_max] = None



    data = [go.Contour(x = a,
                       y = m,
                       z = z,
                       transpose = True,
                       name = f'{label} ({unit})',
                       zmin = z_min,
                       zmax = z_max + z_step,
                       contours_coloring = 'lines',
                       line_width = 2,
                       hovertemplate = f'{label} = ' + '%{z: ' + hoverformat +  '}' + f' {hoverunit}' + '<extra></extra>',

                       # hoverinfo = 'x+y+z+name',
                       # hovertext = None,

                       showscale = False,
                       showlegend = True,
                       colorscale = [[0, color], [1, color]],
                       ncontours = int(2 * (z_max - z_min) / z_step),
                       contours = dict(showlabels = True,
                                       labelformat = format,
                                       labelfont = dict(size = fontsize,
                                                        family = fontfamily)))

            for z, label, unit, hoverunit, z_min, z_max, z_step, color, format, hoverformat in zip([QQ, SG, PABV],
                                                                                                   [q_label, sg_label, pabv_label],
                                                                                                   [q_unit, sg_unit, '%'],
                                                                                                   [q_unit, sg_unit, pabv_unit],
                                                                                                   [q_min, sg_min, pabv_min],
                                                                                                   [q_max, sg_max, pabv_max],
                                                                                                   [q_step, sg_step, pabv_step],
                                                                                                   [yellow, blue, orange],
                                                                                                   [q_format, sg_format, pabv_format],
                                                                                                   [q_hoverformat, sg_hoverformat, pabv_hoverformat])]

    layout = go.Layout(plot_bgcolor = black,
                       hovermode = 'x') # you can try using 'x' or 'x unified'

    fig = go.Figure(data = data, layout = layout)

    fig.update_xaxes(title_text = f'Water\'s quantity ({volume_unit})',
                     linewidth = 1,
                     nticks = int(2 * (a_max - a_min) / a_step),
                     gridwidth = 0.5,
                     gridcolor = grey,
                     tickfont = dict(size = fontsize,
                                     family = fontfamily),
                     titlefont = dict(size = fontsize,
                                      family = fontfamily))

    fig.update_yaxes(title_text = f'Honey\'s quantity ({mass_unit})',
                     linewidth = 1,
                     nticks = int(2 * (m_max - m_min) / m_step),
                     gridwidth = 0.5,
                     gridcolor = grey,
                     tickfont = dict(size = fontsize,
                                     family = fontfamily),
                     titlefont = dict(size = fontsize,
                                      family = fontfamily))

    fig.update_layout(legend = dict(itemsizing = 'constant',
                                    font = dict(size = fontsize,
                                                family = fontfamily)),
                      hoverlabel = dict(font_size = fontsize,
                                        font_family = fontfamily))

    return fig



@app.callback(Output('gravity_value', 'children'),
              [Input('gravity_slider', 'value')])
def update_label(value):
    return f'{value} kg/L'



if __name__ == "__main__":
    app.run_server()