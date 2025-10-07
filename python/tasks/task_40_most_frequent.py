# task_40_most_frequent.py

def most_frequent(items: list) -> any:
    """
    Vrátí nejčastěji se vyskytující prvek v seznamu.
    """
    unique_values = []
    counters = []
    for element in items:
        if element in unique_values:
            n = unique_values.index(element)
            counters[n] = counters[n] + 1
        else:
            unique_values.append(element)
            counters.append(1)
    n = maximum(counters)
    return unique_values[n]

def maximum(counters):
    max_count = 0
    for count in counters:
        if count > max_count:
            max_count = count
            number = counters.index(count)
    return number