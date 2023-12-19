def filter_by(
        attribute: str, min_value: int | None = None,
        max_value: int | None = None, value: int | str | None = None
) -> str:
    if value:
        if isinstance(value, str):
            return f"({attribute} = \"{value}\")"
        return f"({attribute} = {value})"
    return f"({attribute} BETWEEN {min_value} AND {max_value})"

def order_by(attribute: str) -> str:
    return f"ORDER BY {attribute} "

def interval(start: int, limit: int) -> str:
    return f"LIMIT {start}, {limit} "
