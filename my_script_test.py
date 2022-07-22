

from my_script import enlarge

def test_enlarge():
    assert enlarge(9) == 900
    assert enlarge(3) == 30
    assert enlarge(13) == "OOPS"
    

# need to use underscore for testing