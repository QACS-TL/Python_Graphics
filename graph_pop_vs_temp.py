import pandas as pd
import plotly.express as px

df = pd.read_csv(r'C:\labs\capitals_with_header.txt')

fig = px.line(df, x = 'pop', y = 'temp', title='Population vs Temperature')
fig.show()
