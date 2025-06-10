import streamlit as st 
from connect_data_warehouse import query_dwh
from charts import top_occupation_group
from filters import occupation_field_dropdown, occupations_group_dropdown, job_filter

def main():
    st.markdown("# Dashboard av jobbdata")

    st.markdown(
        "Denna dashboard är byggd från en data pipeline med hjälp av moderna data stacken"
    )

    st.dataframe(query_dwh())

    st.markdown("## Analys på olika yrkesgrupper för de tekniska yrkena")
    st.markdown(
        "Nedan är ett par analyser för de tekiska yrkena. Datan"
        "kommer från arbetsförmedlingens API"
    )

    top_occupation_group()

    occupation_field = occupation_field_dropdown()
    occupation_group = occupations_group_dropdown(occupation_field)

    job_filter(occupation_group)

if __name__ == '__main__':
    main()