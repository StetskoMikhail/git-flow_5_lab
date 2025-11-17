import calculator

def test_calculator():
    calc = calculator.Calculator()
    assert calc.add(2, 3) == 5
    assert calc.subtract(5, 2) == 3
    print("All tests passed!")

if __name__ == "__main__":
    test_calculator()
