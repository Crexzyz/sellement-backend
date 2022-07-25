import json
from typing import Any


class BaseFormField():
    "Contains base attributes that a frontend should show"
    value: Any
    "The value that should be displayed in the field"
    name: str
    "The unique name used to reference the field's data"
    label: str
    "The label that describes the field"
    type: str
    "The input type (text, number, currency, select, etc)"
    order: int
    "The order in terms of other fields"
    hidden: bool
    "Whether or not this field should be hidden"
    required: bool
    "Whether or not this field is required"

    def __init__(self, value: Any, name: str, label: str, order: int,
                 hidden: bool = False, required: bool = True) -> None:
        self.value = value
        self.name = name
        self.label = label
        self.type = "base"
        self.order = order
        self.hidden = hidden
        self.required = required

    def toDict(self) -> dict:
        "Returns the field's values in a dict"
        return self.__dict__
