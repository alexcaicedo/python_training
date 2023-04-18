import os

class PersonAccount:
    this_file_path = os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(this_file_path)
    PROJECT_DIR = os.path.dirname(BASE_DIR)
    
    def __init__(self, firstname: str, lastname: str, incomes: list, expenses: list):
        self._firstname = firstname
        self._lastname = lastname
        self._incomes = incomes
        self._expenses = expenses
        self._balance = sum(incomes) - sum(expenses)
        with open(f'{self.PROJECT_DIR}/statement_files/{self._firstname}_{self._lastname}_statement.txt', 'w') as f:
            f.write(f'*** Bank Account Statement ***\n\n')
            f.write(f'Firstname: {self._firstname}\n')
            f.write(f'Lastname: {self._lastname}\n')
            f.write(f'Total Income: ${sum(self._incomes)}\n')
            f.write(f'Total Expenses: (${sum(self._expenses)})\n')
            f.write(f'Balance: ${self._balance}\n\n')
            f.write('* Recent movements *\n')

    def addIncome(self, amount):
        if amount <= 0:
            return
        self._balance += amount
        with open(f'{self.PROJECT_DIR}/statement_files/{self._firstname}_{self._lastname}_statement.txt', 'a') as f:
            f.write(f'Income: ${amount}\n')
            f.write(f'Balance: ${self._balance}\n\n')
    
    def addExpense(self, amount):
        if self._balance < amount or amount < 0:
            return
        self._balance -= amount
        with open(f'{self.PROJECT_DIR}/statement_files/{self._firstname}_{self._lastname}_statement.txt', 'a') as f:
            f.write(f'Expense: (${amount})\n')
            f.write(f'Balance: ${self._balance}\n\n')
    
    def accountInfo(self):
        with open(f'{self.PROJECT_DIR}/statement_files/{self._firstname}_{self._lastname}_statement.txt', 'r') as f:
            statement = f.read()
        
        return statement