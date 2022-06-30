from abc import abstractmethod


class LoanCalculator:

    def __init__(self, principal: int, rate: float, period_count: int):
        self._principal = principal
        self._rate = rate
        self._period_count = period_count

    def get_period_count(self):
        return self._period_count

    def get_monthly_payment(self):
        return self.get_total_payment() / self._period_count

    def get_total_interest(self):
        return self.get_total_payment() - self._principal

    @abstractmethod
    def get_total_payment(self): pass


class SimpleInterestCalculator(LoanCalculator):

    def __init__(self, principal: int, rate: float, period_count: int):
        super().__init__(principal, rate, period_count)

    def get_total_payment(self):
        return (self._principal * self._rate * self._period_count) + self._principal


class CompoundInterestCalculator(LoanCalculator):

    def __init__(self, principal: int, rate: float, period_count: int):
        super().__init__(principal, rate, period_count)

    def get_total_payment(self):
        return self._principal * (1 + self._rate) ** self._period_count
