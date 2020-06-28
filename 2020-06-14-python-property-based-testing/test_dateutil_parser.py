from dateutil.parser import parse
from hypothesis import given
from hypothesis.strategies import text, datetimes


@given(text(),datetimes(),text())
def test_parse(before,date_and_time,after):
    input = before + str(date_and_time) + after
    output = parse(input)
    assert output == date_and_time
