def my_abs(a: float) -> float:
    if a > 0:
        result = a
    else:
        result = -a
    return result


def my_sum(value_list: list) -> int:
    result: int = 0

    for value in value_list:
        result += value
    return result
