"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Return a non-negative quantity, raising ValueError for negative values."""
    quantity = int(value.strip())
    if quantity < 0:
        raise ValueError("Quantity must not be negative")
    return quantity
