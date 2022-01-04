import pytest
from main import helloworld

def test_file1_method1():
	x=5
	y=6
	assert x == y,"FAIL"

def test_file1_method2():
	x=5
	y=6
	assert x+1 == y,"test failed" 

def test_helloworld():
    assert helloworld() == 'hello World'

def test_list_fail():
    assert [1,2,3] == [1,5,6], 'unequal lists'

def test_list():
    assert [1,2,3] == [1,2,3], 'unequal lists'

def test_tuple_not_list():
    assert (1,2,3) == [1,2,3]

def test_dog_cat():
    assert 'dog' == 'cat'
    
def test_5_eq_6():
    assert '5' == '6'

def test_0_eq_None():
    assert 0 == None
