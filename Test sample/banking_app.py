class Account:
    """A bank account where some money can be stored and transferred"""

    def __init__(self):
        """Create an empty bank account"""
        self.__balance = 0  # private attribute

    @property
    def balance(self):
        """Get the account balance in Euros"""
        return self.__balance

    def transfer(self, other, amount):
        """Transfer amount from this account to other account"""
        self.__balance -= amount
        other.__balance += amount


# Create two accounts
a1 = Account()
a2 = Account()

# Transfer 100 Euros from a1 to a2
a1.transfer(a2, 100)
# This is the same as:
# Account.transfer(a1, a2, 100)

# Print the balances
print(f"Account 1 balance: {a1.balance}")  # -100
print(f"Account 2 balance: {a2.balance}")  # 100
