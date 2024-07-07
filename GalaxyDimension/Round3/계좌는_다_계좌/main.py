class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def withdraw(self, amount):
        """돈을 출금한다"""
        self.balance -= amount
    
    def deposit(self, amount):
        """돈을 입금한다"""
        self.balance += amount
    
    def __str__(self):
        """자유 입출금 계좌의 정보를 문자열로 리턴한다."""
        return "{}님의 계좌 예치금은 {}원입니다".format(self.name, self.balance)

class CheckingAccount(BankAccount):
    """자유 입출금 계좌 클래스"""
    def __init__(self, name, balance, max_spending):
        self.max_spending = max_spending
        super().__init__(name, balance)
    
    def use_check_card(self, amount):
        """한 회 사용 한도 초과 이하인 금액을 체크 카드 결제 시 예치금을 줄인다"""
        if amount <= self.max_spending:
            self.balance -= amount
        else:
            print("{}님의 체크 카드는 한 회 {} 초과 사용 불가능합니다".format(self.name, self.max_spending))

class SavingsAccount(BankAccount):
    """저축 계좌 클래스"""
    def __init__(self, name, balance, interest_rate):
        self.interest_rate = interest_rate
        super().__init__(name, balance)
    
    def add_interest(self):
        """이자를 더한다"""
        self.balance *= (1+self.interest_rate)

bank_account_1 = CheckingAccount("성태호", 100000, 10000)
bank_account_2 = SavingsAccount("강영훈", 20000, 0.05)

bank_account_1.withdraw(1000)
bank_account_1.deposit(1000)
bank_account_1.use_check_card(2000)

bank_account_2.withdraw(1000)
bank_account_2.deposit(1000)
bank_account_2.add_interest()

print(bank_account_1)
print(bank_account_2)

print(CheckingAccount.mro())
print(SavingsAccount.mro())