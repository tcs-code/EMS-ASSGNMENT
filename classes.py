from flask import Flask, render_template, request

app = Flask(__name__)

class Employee:
    employee_ids = set()
    
    def __init__(self, employee_id, name, department):
        if employee_id in Employee.employee_ids:
            raise ValueError("Employee ID must be unique")
        self.employee_id = employee_id
        self.name = name
        self.department = department
        Employee.employee_ids.add(employee_id)
    
    def display_employee(self):
        return f"ID: {self.employee_id}, Name: {self.name}, Department: {self.department}"

employees = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        try:
            employee_id = int(request.form['employee_id'])
            name = request.form['name']
            department = request.form['department']
            
            if not employee_id or not name or not department:
                return "Missing parameters! Please provide employee_id, name, and department."
            
            employee = Employee(employee_id, name, department)
            employees[employee_id] = employee
            return f"Employee Added: {employee.display_employee()}"
        except ValueError as e:
            return str(e)
        except Exception as e:
            return "Error: " + str(e)
    return render_template('add_employee.html')

if __name__ == '__main__':
    app.run(debug=True)
