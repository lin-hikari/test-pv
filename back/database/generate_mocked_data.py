from datetime import datetime, timedelta
from time import sleep
import random
import json
import bson

START_DATE = datetime(2024, 3, 1, 0, 0, 0)
END_DATE = datetime(2024, 6, 30, 23, 59, 59)
BIRTH_START_DATE = datetime(1980, 1, 1, 0, 0, 0)
BIRTH_END_DATE = datetime(2010, 12, 31, 23, 59, 59)

TYPES = [
    "GROPING",
    "STALKING",
    "UNWANTED_PHOTOS",
    "UNWANTED_COMMENTS",
    "THREATENING",
    "FLASHING",
]

NEIGHBORHOODS = [
    "Taquacara",
    "Sé",
    "República",
    "Liberdade",
    "Braz",
    "Boa Vista",
    "Madalena",
    "Boa Viagem",
    "Água Fria",
    "Aflitos",
]

def random_from_list(l: list):
    index = random.randint(0, len(l)-1)
    return l[index]

def random_datetime(start_date, end_date):
    delta = end_date - start_date
    random_seconds = random.randint(0, int(delta.total_seconds()))
    random_datetime = start_date + timedelta(seconds=random_seconds)
    
    # Generate random milliseconds
    random_milliseconds = random.randint(0, 999)
    random_datetime = random_datetime.replace(microsecond=random_milliseconds * 1000)
    
    # Return formatted datetime string
    return random_datetime.strftime('%Y-%m-%dT%H:%M:%S')

print()

user_number = 100
complaint_per_user = 3

def generate_new_user(user_num: int):
    user_num_str = str(user_num)
    while len(user_num_str) < 4:
        user_num_str = "0" + user_num_str
    
    return {
        'id': str(bson.ObjectId()),
        'name': f"User {user_num}",
        'email': f"user_{user_num}@mail.com",
        'phone_number': "8191234" + user_num_str,
        'birthdate': random_datetime(BIRTH_START_DATE, BIRTH_END_DATE),
        'gender': random_from_list(['CIS_MALE', 'CIS_FEMALE', 'TRANS_MALE', 'TRANS_FEMALE', 'OTHER']),
        'ethnicity': random_from_list(['BLACK', 'BROWN', 'WHITE', 'WHITE', 'OTHER']),
        'created_at': datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        'updated_at': datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
    }

def generate_new_complaint(complaint_num: int, user_id: str):
    return {
        'id': str(bson.ObjectId()),
        'user_id': user_id,
        'date': random_datetime(START_DATE, END_DATE),
        'at_moment': random_from_list([True, False]),
        'type': random_from_list(TYPES),
        'neighborhood': random_from_list(NEIGHBORHOODS),
        'description': f"This is as description of the report #{complaint_num} for the user {user_id}.",
        'situation': random_from_list(['VICTIM', 'WITNESS']),
        'created_at': datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
        'updated_at': datetime.now().strftime('%Y-%m-%dT%H:%M:%S'),
    }

users = []
complaints = []

for n in range(user_number):
    new_user = generate_new_user(n)
    users.append(new_user)
    print(f"Appended user {new_user['id']}.")
    sleep(3)
    
    for c in range (complaint_per_user):
        new_complaint = generate_new_complaint(c, new_user['id'])
        complaints.append(new_complaint)
        print(f"Appended complaint {new_complaint['id']}.")
        sleep(1)
    
# Store data
users_file_path = "./mocked_users_data.json"
complaints_file_path = "./mocked_complaints_data.json"

with open(users_file_path, 'w') as file:
    json.dump(users, file)

with open(complaints_file_path, 'w') as file:
    json.dump(complaints, file)
