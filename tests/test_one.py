def test_passing():
    assert (1, 2, 3) == (1, 2, 3)

def test_fail():
    assert 'test' != 'testing'
    assert 'test' in 'testing'

def test_not():
    a = 'test'
    b = 'testing'
    assert not a == b

def test_x_not_y():
    x = [ "a", "b", "c"]
    y = [1, 2, 3]
    assert 'x' != 'y'
    assert not 'x'=='y'

