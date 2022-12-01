def add(x, y):
    """Add Function"""
    print("check")
    return x + y

def capital_case(x):
    return x.capitalize()

#--------- Test cases --------------

def test_capital_case():
    assert capital_case('arock') == 'Arock'

def test_capital_case2():
    assert capital_case('winS') == 'Wins'

def test_check_add():
    assert add(5, 7) == 12