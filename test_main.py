from main import count_by_three, count_down

def test_count_by_three():
    assert count_by_three(1,10) == "1 4 7 10 "
    assert count_by_three(12,20) == "12 15 18 "

def test_count_down():
    assert count_down(10) == "10 9 8 7 6 5 4 3 2 1 "
    assert count_down(5) == "5 4 3 2 1 "
