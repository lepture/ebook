import datetime


def xmldatetime(value):
    if not value:
        return ''
    assert isinstance(value, datetime.datetime)
    return value.strftime("%Y-%m-%dT%H:%M:%SZ")


def utf8(value):
    if isinstance(value, (bytes, type(None), str)):
        return value
    if isinstance(value, int):
        return str(value)
    assert isinstance(value, unicode)
    return value.encode('utf-8')
