import argparse

from lib.console_view import ConsoleView
from lib.loan_calculator import SimpleInterestCalculator, CompoundInterestCalculator


# https://www.bankofcanada.ca/rates/banking-and-financial-statistics/posted-interest-rates-offered-by-chartered-banks/
# https://www.calculator.net/personal-loan-calculator.html


def calculate_simple_interest(args):
    calculator = SimpleInterestCalculator(args.principal, args.rate, args.periods)
    ConsoleView(calculator).display()


def calculate_compound_interest(args):
    calculator = CompoundInterestCalculator(args.principal, args.rate, args.periods)
    ConsoleView(calculator).display()


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

