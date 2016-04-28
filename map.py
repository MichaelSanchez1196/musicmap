import plotly.plotly as py
import plotly.tools as tls
import pandas as pd
import plotly.graph_objs as go
tls.set_credentials_file(username='algoodwin', api_key='fnqzr6li9g')
trc = dict(
    type = 'choropleth',
    #locations = ['AL', 'AK','AZ','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY'],
    locationmode ='USA-states',
    colorscale = ['greyscale'],
    z = [10,20,40])
lyt = dict(geo=dict(scope='usa'))
map = go.Figure(data=[trc],layout = lyt)
py.plot(map)
