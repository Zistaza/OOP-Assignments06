class Bank:
    # Class variable
    bank_name = "Cairo Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder  # instance variable

    # Class method to change class variable
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name

    def show_bank_name(self):
        print(f"Bank Name: {self.bank_name}")

    def display(self):
        print(f"Account Holder: {self.account_holder}, Bank: {self.bank_name}")

# Create multiple instances
customer1 = Bank("Mahnoor")
customer2 = Bank("Alizey")

# Show initial bank name
customer1.show_bank_name()
customer2.show_bank_name()

# Change bank name using class method
Bank.change_bank_name("Safwa Bank")

# Show updated bank name for all instances
customer1.show_bank_name()
customer2.show_bank_name()

# Display full customer info
customer1.display()
customer2.display()