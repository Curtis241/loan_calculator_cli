import argparse

# https://www.bankofcanada.ca/rates/banking-and-financial-statistics/posted-interest-rates-offered-by-chartered-banks/

class LoanCalculator:
    """
    Loan calculator class
    """
    def __init__(self, principal: int, rate: float, period_count: int):
        self.__principal = principal
        self.__rate = rate
        self.__period_count = period_count

    def compound(self):
        """
        Calculate compound interest
        """
        return self.__principal * (1 + self.__rate) ** self.__period_count

    def simple(self):
        """
        Calculate compound interest
        """
        return (self.__principal * self.__rate * self.__period_count) + self.__principal


parser = argparse.ArgumentParser(description='Calculates the cost of a loan.')
parser.add_argument('--principal', action='store', type=int, required=True, help='Principal')
parser.add_argument('--rate', action='store', type=float, required=True, help='Rate')
parser.add_argument('--periods', action='store', type=int, required=True, help='Period count')

args = parser.parse_args()
print(args)
