from lib.loan_calculator import LoanCalculator


class ConsoleView:

    def __init__(self, calculator: LoanCalculator):
        self.__calculator = calculator

    def display(self):

        monthly_payment = self.__calculator.get_monthly_payment()
        periods = self.__calculator.get_period_count()
        total_payment = self.__calculator.get_total_payment()
        total_interest = self.__calculator.get_total_interest()

        print(f"Monthly payment: ${monthly_payment:.2f}")
        print(f"Total of {periods} Loan Payments: ${total_payment:.2f}")
        print(f"Total Interest: ${total_interest:.2f}")

        return self
