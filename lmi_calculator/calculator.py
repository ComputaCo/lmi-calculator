import operator
from hooks import use_state
from lmi import component, app

@app
def calculator():
    """Calculator application."""

    visible_number, set_visible_number = use_state(0)
    stored_number, set_stored_number = use_state()
    operation, set_operation = use_state()

    def equals():
        op = operation
        input1 = stored_number
        input2 = visible_number
        if op and input1 and input2:
            result = op(input1, input2)
            set_visible_number(result)

    def binary_operation():
        if stored_number is None:
            set_stored_number(visible_number)
            set_visible_number(0)
        else:
            equals()

    def add():
        set_operation(operator.add)
        return binary_operation()

    def subtract():
        set_operation(operator.sub)
        return binary_operation()

    def multiply():
        set_operation(operator.mul)
        return binary_operation()

    def divide():
        set_operation(operator.truediv)
        return binary_operation()

    return [
        f"Number: {visible_number:.2e}",
        [
            add,
            subtract,
            multiply,
            divide,
        ],
        equals,
    ]
