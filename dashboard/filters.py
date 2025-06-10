from connect_data_warehouse import query_dwh
import streamlit as st
import pandas as pd


def occupation_field_dropdown():
    occupation_fields = query_dwh(
        """
        SELECT DISTINCT occupation_field FROM marts.mart_technical_jobs
    """
    )

    occupation_field = st.selectbox("Välj ett yrkesområde", occupation_fields)
    return occupation_field


def occupations_group_dropdown(occupation_field):
    occupation_groups = query_dwh(
        f"""
        SELECT DISTINCT occupation
        FROM marts.mart_technical_jobs
        WHERE occupation_field = '{occupation_field}'
    """
    )

    occupation_group = st.selectbox("Välj en yrkesgrupp", occupation_groups)
    return occupation_group


def job_filter(occupation_group):
    job_ads = query_dwh(
        f"""
        SELECT 
            headline, description_html, application_deadline
        FROM
            marts.mart_technical_jobs
        WHERE 
            occupation = '{occupation_group}'
        """
    )

    job_ad_headline = st.selectbox("Välj en jobbannons", job_ads["headline"])
    job_ad = job_ads.query("headline == @job_ad_headline")

    st.markdown(f"### {job_ad['headline'].values[0]}")
    st.markdown(
        f"Deadline för ansökan {job_ad['application_deadline'].dt.strftime('%Y-%m-%d').values[0]}"
    )

    st.markdown(job_ad["description_html"].values[0], unsafe_allow_html=True)