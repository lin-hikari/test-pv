from .db_exceptions import MonthNumberException
from datetime import datetime
import json
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

USERS_FILE_PATH = os.path.join(__location__, "mocked_users_data.json")
COMPLAINTS_FILE_PATH = os.path.join(__location__, "mocked_complaints_data.json")
DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

class Database:
    def __init__(self) -> None:
        self.users = []
        with open(USERS_FILE_PATH, 'r') as file:
            self.users = json.load(file)
        
        self.complaints = []
        with open(COMPLAINTS_FILE_PATH, 'r') as file:
            self.complaints = json.load(file)

    def _increment_count(self, d: dict, key: str):
        if key not in d:
            d[key] = 0
        d[key] += 1

    def _get_age(self, birthdate: datetime):
        """ Returns an age in years based on the birthdate and the current date. """
        today = datetime.today()
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1
        return age

    def _get_age_group(self, birthdate: datetime):
        """ Returns a string representing an age_group based on the birthdate. """
        age = self._get_age(birthdate)
        
        if age < 14:
            return "< 14"
        if age <= 18:
            return "14 - 18"
        if age <= 29:
            return "19 - 29"
        if age <= 39:
            return "30 - 39"
        if age <= 49:
            return "40 - 49"
        if age <= 59:
            return "50 - 59"
        return "> 60"
    
    def _get_date_elements(self, d: datetime):
        """ Returns day, month and year from a datetime object as int values. """
        return d.day, d.month, d.year
    
    def _translate_month_int_to_name(self, month_num: int):
        months = {
            1: "Jan",
            2: "Fev",
            3: "Mar",
            4: "Abr",
            5: "Mai",
            6: "Jun",
            7: "Jul",
            8: "Ago",
            9: "Set",
            10: "Out",
            11: "Nov",
            12: "Dez",
        }

        try:
            month_name = months[month_num]
        except:
            raise MonthNumberException("Month Number outside of range (1 .. 12).")

        return month_name

    def insert_complaint(self):
        pass

    def get_complaints(self):
        complaints_with_user_data = []
        users = { user['id']: user for user in self.users }
        
        for complaint in self.complaints:
            user_id = complaint['user_id']
            user = users[user_id]

            for key, value in user.items():
                complaint[f'user_{key}'] = value

            complaints_with_user_data.append(complaint)

        return complaints_with_user_data

    def get_complaint(self, _id: str = None):
        # TODO Implement a way to add the user data to the complaint,
        # using the fields "complaint.user_id" and "user.id".
        # Some functions won't work without this.
        # Hint: Pay attention to the schemas when returning!

        result = list(filter(lambda x: x['id'] == _id, self.complaints))
        if len(result) > 0:
            return result[0]
        return None
    
    def group_by(self, complaint_key: str):
        """ Groups the number of complaints by each value of given key. """
        grouped_data = {}
        complaints = self.get_complaints()
        for complaint in complaints:
            value = complaint[complaint_key]
            self._increment_count(grouped_data, value)

        return grouped_data
    
    def group_by_month(self):
        """ Groups the number of complaints by each month. """
        grouped_data = {}
        complaints = self.get_complaints()
        for complaint in complaints:
            date = datetime.strptime(complaint['date'], DATE_FORMAT)
            _, month, _ = self._get_date_elements(date)
            month_name = self._translate_month_int_to_name(month)
            self._increment_count(grouped_data, month_name)

        return grouped_data
    
    def group_by_age_group(self):
        """ Groups the number of complaints by age groups. """
        grouped_data = {}
        complaints = self.get_complaints()
        for complaint in complaints:
            user_birthdate = datetime.strptime(complaint['user_birthdate'], DATE_FORMAT)  
            age_group = self._get_age_group(user_birthdate) 
            self._increment_count(grouped_data, age_group)

        return grouped_data
    
    def update_complaint(self):
        pass

    def delete_complaint(self):
        pass

    def get_users(self):
        return self.users

    def get_user(self, _id: str = None):
        result = list(filter(lambda x: x['id'] == _id, self.users))
        if len(result) > 0:
            return result[0]
        return None
    
client = Database()