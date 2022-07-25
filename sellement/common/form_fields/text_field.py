from common.form_fields.base_form_field import BaseFormField


class TextField(BaseFormField):
    "A simple text field"
    maxLength: int
    "The max length of the field"

    def __init__(self, value: str, name: str, label: str, order: int,
                 maxLength: int, hidden: bool = False,
                 required: bool = True) -> None:
        super().__init__(value, name, label, order, hidden, required)
        self.type = "text"
        self.maxLength = maxLength
