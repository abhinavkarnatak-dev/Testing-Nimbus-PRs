"""A small example of the Single Responsibility Principle (SRP)."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Order:
    """Store the data for one order."""

    item: str
    unit_price: float
    quantity: int


class OrderTotalCalculator:
    """Calculate an order total."""

    @staticmethod
    def calculate(order: Order) -> float:
        return order.unit_price * order.quantity


class ReceiptPrinter:
    """Format and print an order receipt."""

    @staticmethod
    def print_receipt(order: Order, total: float) -> None:
        print(f"{order.quantity} x {order.item}: ${total:.2f}")


def main() -> None:
    order = Order(item="Notebook", unit_price=4.50, quantity=3)
    total = OrderTotalCalculator.calculate(order)
    ReceiptPrinter.print_receipt(order, total)


if __name__ == "__main__":
    main()
