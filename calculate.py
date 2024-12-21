import circle
import square

figs = ["circle", "square"]
funcs = ["perimeter", "area"]
sizes = {}


def calc(fig, func, size):
    if fig not in figs:
        raise ValueError(f"Invalid figure: {fig}."
                         "Available figures are: {figs}")
    if func not in funcs:
        raise ValueError(f"Invalid function: {func}."
                         "Available functions are: {funcs}")
    if any(s < 0 for s in size):
        raise ValueError("Can't use negative values for figure dimensions.")
    if fig == "circle":
        if func == "perimeter":
            return circle.perimeter(size[0])
        elif func == "area":
            return circle.area(size[0])
    elif fig == "square":
        if func == "perimeter":
            return square.perimeter(size[0])
        elif func == "area":
            return square.area(size[0])
