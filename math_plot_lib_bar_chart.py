"""
https://www.geeksforgeeks.org/graph-plotting-in-python-set-1/
"""

"""
https://pythonspot.com/matplotlib-bar-chart/
"""
import matplotlib.pyplot as plt
from io import BytesIO
import base64

# x-coordinates of left sides of bars
left = [1, 2, 3, 4, 5]

# heights of bars
height = [10, 24, 36, 40, 5]

# labels for bars
tick_label = ['one', 'two', 'three', 'four', 'five']

# plotting a bar chart
plt.bar(left, height, tick_label=tick_label,
        width=0.8, color=['red', 'green'])

# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My bar chart!')

# function to show the plot
# plt.show()
# plt.savefig('bar_chart.png')

# Following code adapted from
# https://stackoverflow.com/questions/48717794/matplotlib-embed-figures-in-auto-generated-html
tmpfile = BytesIO()
plt.savefig(tmpfile, format='png')
encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

html = '<html><head><meta charset="utf-8" /></head><body><div>' \
       + '<img src=\'data:image/png;base64,{}\'>'.format(encoded) \
       + '</div></body></html>'

with open('test.html', 'w') as f:
    f.write(html)
