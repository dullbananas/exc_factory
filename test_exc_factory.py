import pytest
from exc_factory import make_exception


def test_attrs():
	Foo = make_exception('Foo', ('a', 'b'))
	e = Foo('hotel', a='trivago')
	assert str(e) == 'hotel'
	assert e.a == 'trivago'
	assert e.b == None


def test_default_attrs():
	Foo = make_exception('Foo')
	e = Foo('hi')
	assert str(e) == 'hi'
	assert e.__dict__ == {}
