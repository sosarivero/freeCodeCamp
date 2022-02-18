class Category:
    def __init__(self, name):
        # Creates a list that will hold the info about deposits and withdrawals.
        self.name = name
        self.ledger = list()

    # Returns current balance of the budget category by summing all ledgers.
    def get_balance(self):
        return sum(ledger["amount"] for ledger in self.ledger)

    # Used in the withdraw and transfer functions to make sure the category has enough balance to perform the operations.
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

    def deposit(self, amount, description=""):
        # Creates a dictionary to hold the info about deposits.
        deposit_info = dict()
        # Converts the amount to float for calculations.
        deposit_info["amount"] = float(amount)
        deposit_info["description"] = description
        self.ledger.append(deposit_info)

    # Same procedure as deposits.
    def withdraw(self, amount, description=""):
        # Returns False if there is not enough in the category's budget to withdraw.
        if self.check_funds(amount) is False:
            return False

        withdrawal_info = dict()
        # Converts the amount to negative because it is a withdrawal.
        withdrawal_info["amount"] = float(amount) * -1
        withdrawal_info["description"] = description
        self.ledger.append(withdrawal_info)
        return True

    def transfer(self, amount, destination):
        # Do a withdrawal from the origin budget and set informative description.
        if self.check_funds(amount) is False:
            return False

        self.withdraw(amount, f"Transfer to {destination.name}")
        destination.deposit(amount, f"Transfer from {self.name}")
        return True

    def __str__(self):
        lines = ""
        first_line = self.name
        # Title line centered around asterisks.
        lines += first_line.center(30, '*') + '\n'
        for i in range(len(self.ledger)):
            # All ledger descriptions in a vertical list, limited to the 23 first characters.
            ledger_description = self.ledger[i]["description"][:23]
            # Formats the amount as a float with two decimals in order to display it.
            amount = "{:.2f}".format(self.ledger[i]["amount"])
            # Right aligns the amount.
            ledger_amount = amount[:7].rjust(
                30 - len(ledger_description)) + "\n"
            lines += ledger_description + ledger_amount
            i += 1

        total_line = f"Total: {self.get_balance()}"
        lines += total_line
        return lines

        # TODO:
        # def create_spend_chart(categories):


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food.get_balance())
print(food.get_balance())
print(clothing.get_balance())

print(food)
print(clothing)
