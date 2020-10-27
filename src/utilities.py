import io
import sys
from functools import wraps


def disable_print_statements_on_console(func):
    """
    The decorator avoid print statements to print messages on console.
    """

    @wraps(func)
    def wrap(*args, **kw):
        suppress_text = io.StringIO()
        sys.stdout = suppress_text
        result = func(*args, **kw)
        sys.stdout = sys.__stdout__
        return result

    return wrap
