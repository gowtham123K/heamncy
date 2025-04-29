from add import add, sub
def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0

def test_sub():
    assert sub(6,3)==3
    assert sub(6,4)==2