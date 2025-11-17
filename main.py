import calculator
import test_calculator

def main():
    print("Calculator Application")
    calc = calculator.Calculator()
    
    # Тестируем функционал
    test_calculator.test_calculator()
    
    # Демонстрация работы
    print(f"2 + 3 = {calc.add(2, 3)}")
    print(f"5 - 2 = {calc.subtract(5, 2)}")

if __name__ == "__main__":
    main()
