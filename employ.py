class Employee:


    employee_name= "michael D"
    employee_age= 25
    employee_address= "chitwon"
    employe_salary= 3245.7



    def display_information(self):
        print("Employee name ", self.employee_name)
        print("Employee age:", self.employee_age)
        print("Employee address:", self.employee_address)
        print("Employee salary:", self.employe_salary)


    def increase_salary(self):
        amount= int(input("by what amount do you want to increase salary:")) 
        self.employe_salary= self.employe_salary+amount
        print("salary after increment:", self.employe_salary)   