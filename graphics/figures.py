import plotly.express as px
import pandas as pd

df = pd.read_csv("./data/cidals_final.csv")
df_full = pd.read_csv("./data/cidals_full_view.csv")

value_counts = df["active_or_inactive"].value_counts()

value_counts = df["active_or_inactive"].value_counts()


def pie():
    colors = ["#5454b3", "#8CC589"]
    fig = px.pie(
        data_frame=df,
        values=value_counts,
        names=value_counts.index,
        title="Active vs. Inactive Distribution (Leishmania dataset)",
        color=value_counts.index,
        color_discrete_map={"active": colors[0], "inactive": colors[1]}
    )
    fig.update_layout(width=500,height=350)
    return fig

def bar():
    fig = px.bar(df_full, x='ID_test_type', title='Distribution of Enzymo Target (Leishmania dataset)', color_discrete_sequence =['green']*len(df), opacity=1)
    fig.update_layout(width=500,height=350,plot_bgcolor='white', paper_bgcolor='white')
    fig.update_xaxes(title = "")
    fig.update_yaxes(showgrid=True, gridcolor='lightgray')
    return fig