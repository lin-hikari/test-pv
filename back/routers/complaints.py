from back.schemas.complaints import ComplaintSchema, ComplaintList, ComplaintUserSchema, ComplaintUserList
from back.schemas.group_bys import *
from fastapi import APIRouter, HTTPException
from back.database.database import client
from http import HTTPStatus
from datetime import datetime

router = APIRouter(prefix='/complaints', tags=['complaints'])

@router.get('/{from_date}{to_date}', response_model=ComplaintUserList)
def get_complaints(from_date: datetime, to_date: datetime):
    complaints = client.get_complaints(from_date, to_date)
    complaints.sort(key=lambda x: x['id'])
    return {'complaints': complaints}

@router.get('/{complaint_id}', response_model=ComplaintUserSchema)
def get_complaint(complaint_id: str):
    complaint_user = client.get_complaint(complaint_id)
    
    if complaint_user is None:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Complaint not found.")

    return complaint_user

@router.get('/user/{user_id}', response_model=ComplaintList)
def get_complaints_from_user(user_id: str):
    complaints = client.get_complaints_from_user(user_id)
    if(complaints == None):
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="User not found.")
    else:
        return complaints

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