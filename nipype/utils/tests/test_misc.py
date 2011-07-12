# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
from nipype.testing import assert_equal, assert_true

from nipype.utils.misc import container_to_string, \
     getsource, create_function_from_source

def test_cont_to_str():
    # list
    x = ['a', 'b']
    yield assert_equal, container_to_string(x), 'a b'
    # tuple
    x = tuple(x)
    yield assert_equal, container_to_string(x), 'a b'
    # set
    x = set(x)
    y = container_to_string(x)
    yield assert_true, (y == 'a b') or (y == 'b a')
    # dict
    x = dict(a='a', b='b')
    y = container_to_string(x)
    yield assert_true, (y == 'a b') or (y == 'b a')
    # string
    yield assert_equal, container_to_string('foobar'), 'foobar'
    # int.  Integers are not the main intent of this function, but see
    # no reason why they shouldn't work.
    yield assert_equal, container_to_string(123), '123'

def _func1(x):
    return x**3

def test_func_to_str():

    def func1(x):
        return x**2

    # Should be ok with both functions!
    for f in _func1, func1:
        f_src = getsource(f)
        f_recreated = create_function_from_source(f_src)
        yield assert_equal, f(2.3), f_recreated(2.3)
