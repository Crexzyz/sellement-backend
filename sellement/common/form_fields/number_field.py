from common.form_fields.base_form_field import BaseFormField


class NumberField(BaseFormField):
    "A numerical field"
    min: int
    "The minimum value for the field"

    def __init__(self, value: int, name: str, label: str, order: int,
                 min: int, hidden: bool = False,
                 required: bool = True) -> None:
        super().__init__(value, name, label, order, hidden, required)
        self.type = "number"
        self.min = min
