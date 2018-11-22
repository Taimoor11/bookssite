from django.template import Library
register = Library()


def rows(thelist, n):

    try:
        n = int(n)
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]
    list_len = len(thelist)
    split = list_len // n

    if list_len % n != 0:
        split += 1
    return [thelist[split * i:split * (i + 1)] for i in range(n)]


def rows_distributed(thelist, n):
    try:
        n = int(n)
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]
    list_len = len(thelist)
    split = list_len // n

    remainder = list_len % n
    offset = 0
    rows = []
    for i in range(n):
        if remainder:
            start, end = (split + 1) * i, (split + 1) * (i + 1)
        else:
            start, end = split * i + offset, split * (i + 1) + offset
        rows.append(thelist[start:end])
        if remainder:
            remainder -= 1
            offset += 1
    return rows


def columns(thelist, n):
    try:
        n = int(n)
        thelist = list(thelist)
    except (ValueError, TypeError):
        return [thelist]
    list_len = len(thelist)
    split = list_len // n
    if list_len % n != 0:
        split += 1
    return [thelist[i::split] for i in range(split)]


register.filter(rows)
register.filter(rows_distributed)
register.filter(columns)


def _test():
    import doctest
    doctest.testmod()


if __name__ == "__main__":
    _test()