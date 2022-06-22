import argparse

# https://www.bankofcanada.ca/rates/banking-and-financial-statistics/posted-interest-rates-offered-by-chartered-banks/
# https://www.calculator.net/personal-loan-calculator.html


class LoanCalculator:
    """
    Loan calculator class
    """
    def __init__(self, principal: int, rate: float, period_count: int):
        self.principal = principal
        self.rate = rate
        self.period_count = period_count
        self.monthly_payment = 0
        self.total_payment = 0

    def calc_compound(self):
        """
        Calculate compound interest
        """
        self.total_payment = self.principal * (1 + self.rate) ** self.period_count
        self.monthly_payment = self.total_payment / self.period_count

    def calc_simple(self):
        """
        Calculate compound interest
        """
        self.total_payment = (self.principal * self.rate * self.period_count) + self.principal
        self.monthly_payment = self.total_payment / self.period_count


class ConsoleView:

    def __init__(self, calculator: LoanCalculator):
        self.__calculator = calculator

    def display(self, simple: bool = False, compound: bool = False):

        if simple is True:
            self.__calculator.calc_simple()

        if compound is True:
            self.__calculator.calc_compound()

        monthly_payment = self.__calculator.monthly_payment
        periods = self.__calculator.period_count
        total_payment = self.__calculator.total_payment

        print(f"Monthly payment: ${monthly_payment:.2f}")
        print(f"Total of {periods} Loan Payments: ${total_payment:.2f}")
        print(f"Total Interest: {None}")


def calculate_simple_interest(args):
    principal = args.principal
    rate = args.rate
    period_count = args.periods
    calculator = LoanCalculator(principal, rate, period_count)
    view = ConsoleView(calculator)
    view.display(simple=True)


def calculate_compound_interest(args):
    principal = args.principal
    rate = args.rate
    period_count = args.periods
    calculator = LoanCalculator(principal, rate, period_count)
    view = ConsoleView(calculator)
    view.display(compound=True)


def setup():
    principal_arg = argparse.ArgumentParser(add_help=False)
    principal_arg.add_argument('--principal', action='store', type=int, required=True, help='Principal')

    rate_arg = argparse.ArgumentParser(add_help=False)
    rate_arg.add_argument('--rate', action='store', type=float, required=True, help='Rate')

    periods_arg = argparse.ArgumentParser(add_help=False)
    periods_arg.add_argument('--periods', action='store', type=int, required=True, help='Period count')

    parent_parser = argparse.ArgumentParser(description='Calculates the cost of a loan')
    sub_parsers = parent_parser.add_subparsers()
    simple_sp = sub_parsers.add_parser("simple", parents=[principal_arg, rate_arg, periods_arg])
    simple_sp.set_defaults(func=calculate_simple_interest)

    compound_sp = sub_parsers.add_parser("compound", parents=[principal_arg, rate_arg, periods_arg])
    compound_sp.set_defaults(func=calculate_compound_interest)

    return parent_parser


if __name__ == "__main__":
    parser = setup()
    args = parser.parse_args()
    if "func" in args:
        args.func(args)

