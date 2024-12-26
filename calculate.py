import circle
import square


figs = {'circle': circle, 'square': square}
funcs = ['perimeter', 'area']
sizes = {}


def calc(fig, func, size):
    if not (fig in figs):
        raise ValueError(f"Invalid figure: {fig}. "
                         "Available figures are: ['circle', 'square']")
    if not (func in funcs):
        raise ValueError(f"Invalid function: {func}. "
                         "Available functions are: ['perimeter', 'area']")
    if not all(s >= 0 for s in size):
        raise ValueError("Can't use negative values for figure dimensions.")
    result = eval(f"{fig}.{func}(*{size})")
    return result


if __name__ == "__main__":
    func = ""
    fig = ""
    size = list()

    while fig not in figs:
        fig = input(f"Enter figure name, avaliable are {figs}:\n")

    while func not in funcs:
        func = input(f"Enter function name, avaliable are {funcs}:\n")

    while len(size) != sizes.get(f"{func}-{fig}", 1):
        size = list(
            map(
                int,
                input(
                    "Input figure sizes separated "
                    "by space, 1 for circle and square\n"
                ).split(" "),
            )
        )

    calc(fig, func, size)
