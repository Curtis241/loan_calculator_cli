import argparse

# https://www.bankofcanada.ca/rates/banking-and-financial-statistics/posted-interest-rates-offered-by-chartered-banks/
# https://www.calculator.net/personal-loan-calculator.html

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

def calculate_simple_interest(args):
    principal = args.principal
    rate = args.rate
    period_count = args.periods
    calculator = LoanCalculator(principal, rate, period_count)
    print(calculator.simple())

def calculate_compound_interest(args):
    principal = args.principal
    rate = args.rate
    period_count = args.periods
    calculator = LoanCalculator(principal, rate, period_count)
    print(calculator.compound())

def setup():
    parser = argparse.ArgumentParser(description='Calculates the cost of a loan')
    sub_parsers = parser.add_subparsers()
    simple_sp = sub_parsers.add_parser("simple")
    simple_sp.add_argument('--principal', action='store', type=int, required=True, help='Principal')
    simple_sp.add_argument('--rate', action='store', type=float, required=True, help='Rate')
    simple_sp.add_argument('--periods', action='store', type=int, required=True, help='Period count')
    simple_sp.set_defaults(func=calculate_simple_interest)

    compound_sp = sub_parsers.add_parser("compound")
    compound_sp.add_argument('--principal', action='store', type=int, required=True, help='Principal')
    compound_sp.add_argument('--rate', action='store', type=float, required=True, help='Rate')
    compound_sp.add_argument('--periods', action='store', type=int, required=True, help='Period count')
    compound_sp.set_defaults(func=calculate_compound_interest)

    return parser

if __name__ == "__main__":
    parser = setup()
    args = parser.parse_args()
    if "func" in args:
        args.func(args)

