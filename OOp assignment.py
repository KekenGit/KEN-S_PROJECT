# =========================================
# INTERACTIVE BANKING APPLICATION
# =========================================

class InsufficientFundsError(Exception):
    """
    Custom exception raised when the account balance
    is not enough for withdrawal.
    """

    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        self.shortage = amount - balance

        super().__init__(
            f"Insufficient funds! Balance: {balance}, "
            f"Withdrawal Amount: {amount}"
        )

    def deficit(self):
        """
        Returns how much more money is needed.
        """
        return self.shortage


def withdraw(balance, amount):
    """
    Withdraws money from the account.
    Raises InsufficientFundsError if balance is too low.
    """

    if amount > balance:
        raise InsufficientFundsError(balance, amount)

    balance -= amount
    return balance


print("=== BANKING APPLICATION ===")

try:
    # User input
    current_balance = float(input("Enter your current balance: "))
    withdraw_amount = float(input("Enter withdrawal amount: "))

    # Attempt withdrawal
    new_balance = withdraw(current_balance, withdraw_amount)

    print("\nWithdrawal successful!")
    print("Remaining Balance:", new_balance)

except InsufficientFundsError as error:
    print("\nError:", error)
    print("Additional money needed:", error.deficit())

except ValueError:
    print("\nInvalid input! Please enter numbers only.")


# =========================================
# INTERACTIVE ONLINE QUIZ APPLICATION
# =========================================

class InvalidAnswerTypeError(Exception):
    """
    Raised when the answer is not a number.
    """
    pass


class ScoreOutOfRangeError(Exception):
    """
    Raised when the score is outside the valid range.
    """
    pass


def validate_score(score):
    """
    Validates quiz scores.
    Valid scores must be numbers from 0 to 100.
    """

    if score < 0 or score > 100:
        raise ScoreOutOfRangeError(
            "Score must be between 0 and 100."
        )

    return "Valid Score"


print("\n=== ONLINE QUIZ APPLICATION ===")

try:
    # User input
    user_score = float(input("Enter your quiz score (0-100): "))

    # Validate score
    result = validate_score(user_score)

    print("Result:", result)

except ValueError:
    raise InvalidAnswerTypeError(
        "Score must be a numeric value."
    )

except InvalidAnswerTypeError as error:
    print("Error:", error)

except ScoreOutOfRangeError as error:
    print("Error:", error)


# =========================================
# JUSTIFICATION
# =========================================

print("\n=== JUSTIFICATION ===")

print(
    "Custom exceptions are better than built-in exceptions "
    "because they make errors easier to understand and manage. "
    "They provide specific meanings for application problems, "
    "such as invalid quiz scores or insufficient bank funds. "
    "This improves code readability, debugging, and maintenance."
)
