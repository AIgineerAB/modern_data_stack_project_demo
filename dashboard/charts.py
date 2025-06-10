import plotly.express as px
from connect_data_warehouse import query_dwh
import streamlit as st


def top_occupation_group():
    df = query_dwh(
        """
        SELECT occupation_group, SUM(vacancies) AS total_vacancies
        FROM marts.mart_technical_jobs
        GROUP BY occupation_group
        ORDER BY total_vacancies DESC
    """
    ).head(15)

    fig = px.bar(df, x="total_vacancies", y="occupation_group")

    fig.update_layout(
        title=dict(text="Topp 15 yrkesgrupperna för tekniska yrken", font={"size": 24}),
        xaxis = dict(title="# POSITIONER"),
        yaxis = dict(title="YRKESGRUPP", autorange = "reversed"),

    )

    st.plotly_chart(fig)
