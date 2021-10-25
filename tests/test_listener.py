from vehicle_listener.utils import parse, validate

def test_parse():
  assert {} == parse('invalid')
  assert {} == parse('123')
  assert {} == parse('{}')
  assert {'one': 1} == parse('{"one": 1}')

def test_validate():
  msg = {}
  assert not validate(msg)

  # Not all required keywords present
  msg['component'] = 'some text'
  msg['country'] = 'some text'
  assert not validate(msg)

  # Value type do not matches schema
  msg['description'] = 'some text'
  msg['model'] = 123
  assert not validate(msg)

  # All required keywords are present
  msg['model'] = 'some text'
  assert validate(msg)

  # Empty string do not care
  msg['model'] = ''
  assert validate(msg)
  assert msg['model'] == ''

  # Empty country replaced with USA
  msg['country'] = ''
  assert validate(msg)
  assert msg['country'] == 'USA'

  # Extra keywords do not care
  msg['extra'] = [1, 2, 3]
  assert validate(msg)
