import pytest
from exc_factory import make_exception


def test_attrs():
	Foo = make_exception('Foo', ('a', 'b'))
	e = Foo('hotel', a='trivago')
	assert str(e) == 'hotel'
	assert e.a == 'trivago'
	assert e.b == None
