"""
Tham chiếu Assignment 1: lớp tài khoản ngân hàng (nạp/rút/số dư).
"""

from __future__ import annotations


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self._balance = float(balance)

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Số tiền nạp phải > 0")
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Số tiền rút phải > 0")
        if amount > self._balance:
            raise ValueError("Không đủ số dư")
        self._balance -= amount

    def __str__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self._balance:.2f})"


if __name__ == "__main__":
    acc = BankAccount("An", 100)
    acc.deposit(50)
    acc.withdraw(30)
    print(acc)
