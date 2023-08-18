import calendar

def findingLast_saturday(input_value):
    month = int(input_value[0:2])
    year = int(input_value[2:6])
    month_End = calendar.monthrange(year, month)[1]
    
    
    saturdays = []

    for day in range(month_End, 0, -1):
        if calendar.weekday(year, month, day) == calendar.SATURDAY:
            saturdays.append(day)
            return f"Last Saturday: {saturdays[0]}th \nTotal Saturdays: {len(saturdays)}"
        
given_date = "062023"
final_Result = findingLast_saturday(given_date)

print(final_Result)