from datetime import datetime

def datetime2str(datetime_obj: datetime):
    format_str = "%Y-%m-%d"

    if hasattr(datetime_obj, 'hour') and hasattr(datetime_obj, 'minute') and hasattr(datetime_obj, 'second'):
        format_str += " %H:%M:%S"

    return datetime_obj.strftime(format_str)

def str2datetime(datetime_str: str) -> datetime:
    format_elements = ["%Y", "%m", "%d", "%H", "%M", "%S"]
    format_str = " ".join([scale for scale in format_elements if scale[1:] in datetime_str])

    return datetime.strptime(datetime_str, format_str)
