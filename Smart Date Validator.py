import re
def check_date_validity(date_text):
    data_regex=re.compile(r'''^
    ([0-3]\d)   #day
    /
    ([0-1]\d)   #month
    /
    ([1-2]\d{3})   #year
    $''',re.VERBOSE)
    match=data_regex.search(date_text)
    if not match:
        return False
    day=int(match.group(1))
    month=int(match.group(2))
    year=int(match.group(3))
    if month>12 or month<1:
        return False
    if month in [4,6,9,11]:
        Max_Day=30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            Max_Day=29
        else:
            Max_Day=28
    else:
        Max_Day=31
    if 1<=day<=Max_Day:
        return True
    else:
        return False
test_cases = ["29/02/2024", "31/04/2022", "15/13/2020"]
for date in test_cases:
    if check_date_validity(date):
        print('the date: ' +date+ ' is right')
    else:
        print('the date: ' +date+ ' is wrong')


