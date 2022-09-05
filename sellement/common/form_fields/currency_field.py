from common.form_fields.number_field import NumberField


class CurrencyField(NumberField):
    "A numerical field representing currency"
    symbol: str
    "The currency's symbol"

    def __init__(self, value: float, name: str, label: str, order: int,
                 min: int, symbol: str, hidden: bool = False,
                 required: bool = True) -> None:
        super().__init__(value, name, label, order, min, hidden, required)
        self.type = "currency"
        self.symbol = symbol
