data_entries = ['userId','jobTitle','firstName','lastName','employeeCode','region','phoneNumber','emailAddress']

def modify_data(data, request):
    for entry in data_entries:
        if request.form[entry] == None: return False
    data['Employees'].append({})
    for entry in data_entries:
        data['Employees'][-1][entry] = request.form[entry]
    return True