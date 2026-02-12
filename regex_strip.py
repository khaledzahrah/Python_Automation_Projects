import re
def regex_strip(text , chars=None):
    if chars is None:
        return re.sub(r'^\s+|\s+$', '', text)
    else:
        safe_chars = re.escape(chars)
        pattern = f'^[{safe_chars}]+|[{safe_chars}]+$'
        return re.sub(pattern, '', text)
#EXAMPLE
print(f"{regex_strip(' -------+++-Hello World---__++    ' , ' +_-')}")