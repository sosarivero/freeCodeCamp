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


def create_spend_chart(categories):
    # Creates a list to hold the category names to be exctracted from the objects.
    # TODO: There might be a more sensible way to do this. (Maybe dictionaries?)
    names = list()

    # Create a list to hold the total of all withdrawals from each of the categories.
    total_spending = list()

    # Calculate the total spending from each category.
    for category in categories:
        # Converts the objects __str__(self) outputs into strings to manipulate.
        string = str(category).split()
        # Saves the category name.
        name = string[0].replace("*", "")
        names.append(name)

        # Creates a list to hold the withdrawals before scanning for them in a loop.
        withdrawals = 0
        for word in string:
            # Use try with float() to scan for numbers.
            try:
                word = float(word)
                # Needs to be below 0 to just get withdrawals.
                if word < 0:
                    # Converts to int to round them down, and use abs() to convert them into positive.
                    word = int(abs(word))
                    withdrawals += word
            except:
                continue
        # Append the sum of the withdrawals to the total_spending list.
        total_spending.append(withdrawals)

    percentages = list()

    # Append the percentages (format: 10% 100%)
    for category in total_spending:
        percentages.append((category / sum(total_spending) * 100))

    # Creates chart string with the title.
    output_chart = "Percentage spent by category\n"

    # Range starting at 100, stopping at below 0, and with -10 steps.
    for i in range(100, -10, -10):
        # Outputs the percentage by converting the range of the loop to an integer.
        # Right aligned by three characters.
        output_chart += str(i).rjust(3) + "|"
        for percent in percentages:
            # Outputs an 'o' if the percentage matches or is higher than the interval.
            if percent >= i:
                output_chart += " o "
            # Else, it's an empty space.
            else:
                output_chart += "   "
        # End of the line when all percentages are input.
        output_chart += " \n"

    # The X-axis needs to overflow by two - after the last category.
    # Two additional new lines at the end before starting to output the category names vertically.
    output_chart += "    " + ("-"*(len(categories)*3)) + "-\n"

    # Get the length of the longest category name.
    longest_name = len(max(names, key=len))

    for i in range(longest_name):
        # Adds five spaces per line for initial alignment.
        output_chart += " "*5
        for name in names:
            try:
                output_chart += name[i] + " "*2
            # Skips if the name has already been input completely.
            except:
                output_chart += " "*3
        output_chart += "\n"

    # Strips the very last \n to make the test module happy.
    output_chart = output_chart.rstrip("\n")
    return output_chart
