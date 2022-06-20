#!/usr/bin/python3
def safe_function(fct, *args):
    pass
for cls in [safe_function, fct]:
    try:
        raise cls()
    except safe_function:
        return result
    except fct:
        return result
    else:
        return None
