def deep_flatten(xs):
    flat_list = []
    [flat_list.extend(deep_flatten(x)) for x in xs] if isinstance(xs, list) else flat_list.append(xs)
    return flat_list

deep_flatten([1, [2], [[3, [1], 4], 5]]) 
>>> [1, 2, 3, 1, 4, 5]
