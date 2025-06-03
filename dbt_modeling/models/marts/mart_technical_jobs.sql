with
    fct_job_ads as (select * from {{ ref('fct_job_ads') }}),
    dim_job_details as (select * from {{ ref('dim_job_details') }}),
    dim_occupation as (select * from {{ ref('dim_occupation') }})

select 
    jd.headline,
    f.vacancies,
    f.relevance,
    o.occupation,
    o.occupation_group,
    o.occupation_field,
    f.application_deadline,
    jd.description,
    jd.description_html,
    jd.duration, 
    jd.salary_type,
    jd.salary_description,
    jd.working_hours_type
from fct_job_ads f
left join dim_job_details jd on f.job_details_id = jd.job_details_id
left join dim_occupation o on f.occupation_id = o.occupation_id
