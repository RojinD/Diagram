import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import pandas as pd
import chart_studio.plotly as py  # we use this instead of plotly.plotly
# import plotly.express as px
# import chart_studio.tools as tls

# tls.set_credentials_file(username='RojinD', api_key='btnunbtez4')

data = dict(type='choropleth',
            locations=['AZ', 'CA', 'NY'],
            locationmode='USA-states',
            colorscale='Portland',  # colorscale can be equal to Jet or Greens
            text=['Arizona', 'Cali', 'New York'],
            z=[1.0, 2.0, 3.0],
            colorbar={'title': 'Colorbar Title Goes Here'})
print(data)

layout = dict(geo={'scope': 'usa'})
choromap = go.Figure(data=[data], layout=layout)
# iplot(choromap)

df = pd.read_csv(
    r'C:\Users\rojin\OneDrive\Desktop\Data Analyst\Projects\python\Py-DS-ML-Bootcamp-master (1)\Refactored_Py_DS_ML_Bootcamp-master\09-Geographical-Plotting\2011_US_AGRI_Exports.csv')  # ??
# df = pd.read_csv('2011_US_AGRI_Exports.csv')
print(df.head())
data = dict(type='choropleth', locations=df['code'], colorscale='ylorrd',
            locationmode='USA-states',
            z=df['total exports'],
            text=df['text'],
            marker=dict(line=dict(color='rgb(255,255,255)', width=2)),
            colorbar={'title': 'Millions USD'})  # colorscale='YIOrRd'
# https://plotly.com/python-api-reference/generated/plotly.graph_objects.layout.html#plotly.graph_objects.layout.Colorscale

layout = dict(title='2011 US Agriculture Exports by State', geo=dict(scope='usa', showlakes=True,
                                                                     lakecolor='rgb(85,173,240)'))
print(layout)
choromap2 = go.Figure(data=[data], layout=layout)
# iplot(choromap2)

# vedio numbert 64

df = pd.read_csv('2014_world_GDP')
print(df.head())

data = dict(type='choropleth',
            locations=df['CODE'],  z=df['GDP (BILLIONS)'],
            text=df['COUNTRY'],
            colorbar={'title': 'GDP in Billions USD'})

layout = dict(title='2014 Global GDP',
              geo=dict(showframe=False,
                       projection={'type': 'mercator'}
                       ))
print(df.columns)
choromap3 = go.Figure(data=[data], layout=layout)
iplot(choromap3)
# py.plot(choromap3, filename='interactive_plot', auto_open=True)
