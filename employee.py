"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import abc

class ConstCommission:
    def __init__(self, amount) -> None:
        self.description = f"bonus commission of {amount}"
        self.amount = amount

class ContractCommission:
    def __init__(self, no_of_contract, contract_value) -> None:
        self.description = f"commission for {no_of_contract} contract(s) at {contract_value}/contract"
        self.amount = contract_value * no_of_contract

class Employee:
    def __init__(self, name, commission):
        self.name = name
        self.commission = commission

    def get_pay(self):
        return self.get_base_pay() + (self.commission.amount if self.commission else 0)

    def __str__(self):
        return f"{self.name} works on a {self.get_contract_description()}" + \
            (f" and receives a {self.commission.description}" if self.commission else "") + \
                f". Their total pay is {self.get_pay()}."

class HourlyEmployee(Employee):
    def __init__(self, name, hours, rate, commission=None):
        super().__init__(name, commission)
        self.hours = hours
        self.rate = rate

    def get_contract_description(self):
        return f"contract of {self.hours} hours at {self.rate}/hour"

    def get_base_pay(self):
        return self.hours * self.rate
    
class SalaryEmployee(Employee):
    def __init__(self, name, salary, commission=None):
        super().__init__(name, commission)
        self.salary = salary

    def get_contract_description(self):
        return f"monthly salary of {self.salary}"
    
    def get_base_pay(self):
        return self.salary


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee("Billie", 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = HourlyEmployee("Charlie", 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee("Renee", 3000, ContractCommission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = HourlyEmployee("Jan", 150, 25, ContractCommission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee("Robbie", 2000, ConstCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = HourlyEmployee("Ariel", 120, 30, ConstCommission(600))

