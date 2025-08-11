# Any given day is only ever reimbursed once, even if multiple projects are on the same day.
# Projects that are contiguous or overlap, with no gap between the end of one and the start of the next, are considered a sequence of projects and should be treated similar to a single project.
# First day and last day of a project (or sequence of projects) are travel days.
# Any day in the middle of a project (or sequence of projects) is considered a full day.
# If there is a gap between projects, those gap days are not reimbursed and the days on either side of that gap are travel days.
# A travel day is reimbursed at a rate of 45 dollars per day in a low cost city.
# A travel day is reimbursed at a rate of 55 dollars per day in a high cost city.
# A full day is reimbursed at a rate of 75 dollars per day in a low cost city.
# A full day is reimbursed at a rate of 85 dollars per day in a high cost city.
# Given the following sets of projects, provide code that will calculate the reimbursement for each.

# Set 1:
#   Project 1: Low Cost City Start Date: 10/1/24 End Date: 10/4/24

# Set 2:
#   Project 1: Low Cost City Start Date: 10/1/24 End Date: 10/1/24
#   Project 2: High Cost City Start Date: 10/2/24 End Date: 10/6/24
#   Project 3: Low Cost City Start Date: 10/6/24 End Date: 10/9/24

# Set 3:
#   Project 1: Low Cost City Start Date: 9/30/24 End Date: 10/3/24
#   Project 2: High Cost City Start Date: 10/5/24 End Date: 10/7/24
#   Project 3: High Cost City Start Date: 10/8/24 End Date: 10/8/24

# Set 4:
#   Project 1: Low Cost City Start Date: 10/1/24 End Date: 10/1/24
#   Project 2: Low Cost City Start Date: 10/1/24 End Date: 10/1/24
#   Project 3: High Cost City Start Date: 10/2/24 End Date: 10/3/24
#   Project 4: High Cost City Start Date: 10/2/24 End Date: 10/6/24

from datetime import date

TRAVEL_REIMBURSEMENT_LOW = 45
TRAVEL_REIMBURSEMENT_HIGH = 55
FULL_REIMBURSEMENT_LOW = 75
FULL_REIMBURSEMENT_HIGH = 85

LOW_COST_CITY = 0
HIGH_COST_CITY = 1

SET_1 = [
    {'city_cost': LOW_COST_CITY, 'start_date': date(2024, 10, 1), 'end_date': date(2024, 10, 4)}
]

SET_2 = [
    {'city_cost': LOW_COST_CITY, 'start_date': date(2024, 10, 1), 'end_date': date(2024, 10, 1)},
    {'city_cost': HIGH_COST_CITY, 'start_date': date(2024, 10, 2), 'end_date': date(2024, 10, 6)},
    {'city_cost': LOW_COST_CITY, 'start_date': date(2024, 10, 6), 'end_date': date(2024, 10, 9)}
]

SET_3 = [
    {'city_cost': LOW_COST_CITY, 'start_date': date(2024, 9, 30), 'end_date': date(2024, 10, 3)},
    {'city_cost': HIGH_COST_CITY, 'start_date': date(2024, 10, 5), 'end_date': date(2024, 10, 7)},
    {'city_cost': HIGH_COST_CITY, 'start_date': date(2024, 10, 8), 'end_date': date(2024, 10, 8)}
]

SET_4 = [
    {'city_cost': LOW_COST_CITY, 'start_date': date(2024, 10, 1), 'end_date': date(2024, 10, 1)},
    {'city_cost': LOW_COST_CITY, 'start_date': date(2024, 10, 1), 'end_date': date(2024, 10, 1)},
    {'city_cost': HIGH_COST_CITY, 'start_date': date(2024, 10, 2), 'end_date': date(2024, 10, 3)},
    {'city_cost': HIGH_COST_CITY, 'start_date': date(2024, 10, 2), 'end_date': date(2024, 10, 6)}
]

TRAVEL = 0
FULL = 1

REIMBURSEMENT_RATES = {
    TRAVEL: {
        LOW_COST_CITY: TRAVEL_REIMBURSEMENT_LOW,
        HIGH_COST_CITY: TRAVEL_REIMBURSEMENT_HIGH
    },
    FULL: {
        LOW_COST_CITY: FULL_REIMBURSEMENT_LOW,
        HIGH_COST_CITY: FULL_REIMBURSEMENT_HIGH
    }
}

def calculate_day_reimbursement(day_type, city_cost):
    if day_type not in REIMBURSEMENT_RATES:
        raise ValueError("Invalid day type")
    if city_cost not in REIMBURSEMENT_RATES[day_type]:
        raise ValueError("Invalid city cost")
    return REIMBURSEMENT_RATES[day_type][city_cost]

assert calculate_day_reimbursement(TRAVEL, LOW_COST_CITY) == TRAVEL_REIMBURSEMENT_LOW
assert calculate_day_reimbursement(TRAVEL, HIGH_COST_CITY) == TRAVEL_REIMBURSEMENT_HIGH
assert calculate_day_reimbursement(FULL, LOW_COST_CITY) == FULL_REIMBURSEMENT_LOW
assert calculate_day_reimbursement(FULL, HIGH_COST_CITY) == FULL_REIMBURSEMENT_HIGH

print('day reimbursement rates are correct!')

def calculate_reimbursement(projects_array):
    total_reimbursement = 0
    day_type = None
    current_day = None

    for project in projects_array:
        if current_day is None:
            current_day = project['start_date']
        if day_type is None:
            day_type = TRAVEL
        total_reimbursement += calculate_day_reimbursement(day_type, project['city_cost'])
    
    return total_reimbursement

assert calculate_reimbursement(SET_1) == 240
assert calculate_reimbursement(SET_2) == 665
assert calculate_reimbursement(SET_3) == 520
assert calculate_reimbursement(SET_4) == 440

print("All tests passed!")