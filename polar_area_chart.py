import plotly.graph_objects as go
import plotly.express as px

r=[1, 2, 3, 4, 5, 6,7,8,9,10,11]
labels = ["Illness", "Relocation", "Commute", "Career Change", "Type of Work","Pay","Career Advancement","Workload",
          "Lack of Recognition","Conflict with Others","Training"]
num_slices = len(r)
theta = [(i+0.5) * 360 / num_slices for i in range(num_slices)]
width = [360 / num_slices for _ in range(num_slices)]
color_seq = px.colors.qualitative.Vivid
color_indices = range(0, len(color_seq), len(color_seq) // 11 )
colors = [color_seq[i] for i in color_indices]

barpolar_plots = [go.Barpolar(r=[r], theta=[t], width=[w], name=n, marker_color=[c],hovertemplate=n)
for r, t, w, n, c in zip(r, theta, width, labels, colors)]

fig = go.Figure(barpolar_plots)

fig.update_layout(
    template=None,
    title="Attrition factors and their Impact ability",
        polar = dict(
        radialaxis = dict(showgrid=False,showline=False,range=[0, 11], showticklabels=False, ticks=''),
        angularaxis = dict(showgrid=False,showline=False,showticklabels=False, ticks='')
        
    )
)
fig.show()

