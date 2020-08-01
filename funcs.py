def std_reverse(l):
    copy = l[:]
    copy.reverse()
    return copy


def std_sort(l):
    return sorted(l)


def std_find(l, value):
    return l.index(value)


def std_filter(fun, l):
    return list(filter(fun, l))


def std_map(fun, l):
    return list(map(fun, l))
