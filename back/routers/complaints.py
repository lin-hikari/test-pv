from back.schemas.complaints import ComplaintSchema, ComplaintList, ComplaintUserSchema, ComplaintUserList
from back.schemas.group_bys import *
from fastapi import APIRouter, HTTPException
from back.database.database import client
from http import HTTPStatus

router = APIRouter(prefix='/complaints', tags=['complaints'])

@router.get('/', response_model=ComplaintUserList)
def get_complaints():
    complaints = client.get_complaints()
    complaints.sort(key=lambda x: x['id'])
    return {'complaints': complaints}

@router.get('/{complaint_id}', response_model=ComplaintSchema)
def get_complaint(complaint_id: str):
    complaint = client.get_complaint(complaint_id)
    
    if complaint is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Complaint not found.")

    return complaint

# @router.get('/user/{user_id}', response_model=ComplaintList)
# def get_complaints_from_user(user_id: str):
#     # Implement your function here!

@router.get('/group/types', response_model=GroupByTypes)
def get_complaints_group_by_types():
    return client.group_by('type')

@router.get('/group/genders', response_model=GroupByGenders)
def get_complaints_group_by_genders():
    return client.group_by('user_gender')

@router.get('/group/age_group', response_model=GroupByAgeGroup)
def get_complaints_group_by_age_group():
    return client.group_by_age_group()

@router.get('/group/at_moment', response_model=GroupByMoment)
def get_complaints_group_by_moment():
    grouped_by_at_moment = client.group_by('at_moment')
    output = { str(key): value for key, value in grouped_by_at_moment.items() }
    return output

@router.get('/group/months', response_model=GroupByMonths)
def get_complaints_group_by_months():
    return client.group_by_month()

@router.get('/group/neighborhoods', response_model=list[GroupByNeighborhoods])
def get_complaints_group_by_neighborhoods():
    grouped_by_neighborhoods = client.group_by('neighborhood')
    output = [
        {'name': neighborhood, 'count': count }
        for neighborhood, count
        in grouped_by_neighborhoods.items()
    ]

    if len(output) == 0:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="No neighborhoods found.")

    return output