"""
Alignment context manager for FieldPy.

"""

from fieldpy import engine


class AlignContext:
    """
    Context manager for alignment in FieldPy.
    This context manager is used to align the state of the engine with the
    current context. It should be used in the following way:
    with AlignContext("context_name"):
        # do something
        pass

    """
    def __init__(self, name: str):
        self.name = name

    def __enter__(self):
        engine.enter(self.name)
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        engine.exit()
