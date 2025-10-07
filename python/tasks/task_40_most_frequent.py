# task_40_most_frequent.py

def most_frequent(items: list) -> any:
    """
    Vrátí nejčastěji se vyskytující prvek v seznamu.
    """
    new_list = []
    counter = []
    for element in items:
        if element in new_list:
            n = new_list.index(element)
            counter[n] = counter[n] + 1
        else:
            new_list.append(element)
            counter.append(1)
    n = maximum(counter)
    return new_list[n]


def maximum(counter):
    max = 0
    for i in counter:
        if i > max:
            max = i
            number = counter.index(i)
    return number
