def oxford_comma(items):
    if len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        stringed_items = ", ".join(items[:-1])
        return f"{stringed_items}, and {items[-1]}"
