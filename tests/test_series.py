from math_series.series import fibonacci,lucas,sum_series

"""
0
1
7
invalid data type 
"""
def test_fib_for_zero():
    actual=fibonacci(0)
    expected=0
    assert actual==expected

def test_fib_for_one():
    actual=fibonacci(1)
    expected=1
    assert actual==expected    

def test_fib_for_seven():
    actual=fibonacci(7)
    expected=13
    assert actual==expected
    
def test_fib_for_data_ytype():
    actual=fibonacci('r') 
    expected='Invalid Input'
    assert actual==expected

"""
0
1
7
invalid data type 
"""
def test_lucas_for_zero():
    actual=lucas(0)
    expected=2
    assert actual==expected

def test_lucas_for_one():
    actual=lucas(1)
    expected=1
    assert actual==expected    

def test_lucas_for_seven():
    actual=lucas(7)
    expected=29
    assert actual==expected
    
def test_lucas_for_data_type():
    actual=lucas('r') 
    expected='Invalid Input'
    assert actual==expected


"""
0
1
5
invalid data type 
"""
def test_sum_series_for_zero_fib():
    actual=sum_series(0)
    expected=0
    assert actual==expected

def test_sum_series_for_one_fib():
    actual=sum_series(1)
    expected=1
    assert actual==expected

def test_sum_series_for_five_fib():
    actual=sum_series(5)
    expected=5
    assert actual==expected


def test_sum_series_for_zero_lucas():
    actual=sum_series(0,2,1)
    expected=2
    assert actual==expected


def test_sum_series_for_one_lucas():
    actual=sum_series(1)
    expected=1
    assert actual==expected


def test_sum_series_for_five_lucas():
    actual=sum_series(5,2,1)
    expected=11
    assert actual==expected

def test_sum_series_for_data_type():
    actual=sum_series('r') 
    expected='Invalid Input'
    assert actual==expected

def test_sum_series_for_value1_data_type():
    actual=sum_series(1,'r',0) 
    expected='Invalid Input'
    assert actual==expected

def test_sum_series_for_value2_data_type():
    actual=sum_series(1,2,'r') 
    expected='Invalid Input'
    assert actual==expected
