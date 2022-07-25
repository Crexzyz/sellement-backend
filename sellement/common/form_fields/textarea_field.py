from common.form_fields.text_field import TextField


class TextareaField(TextField):
    "A text field with multiple rows"
    rows: int
    "How many rows to show in a single textarea"

    def __init__(self, value: str, name: str, label: str, order: int,
                 maxLength: int, rows: int, hidden: bool = False,
                 required: bool = True) -> None:
        super().__init__(value, name, label, order, maxLength, hidden,
                         required)
        self.type = "textarea"
        self.rows = rows
