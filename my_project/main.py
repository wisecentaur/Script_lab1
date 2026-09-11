from lib import add, subtract, multiply, divide;

def main():
    """Main function to demonstrate work of lib module."""
    x = 20
    y = 2
    add_res = add(x, y)
    sub_res = subtract(x, y)
    mult_res = multiply(x, y)
    div_res = divide(x, y)
    print(f"Result of {x} + {y} = {add_res}")
    print(f"Result of {x} - {y} = {sub_res}")
    print(f"Result of {x} * {y} = {mult_res}")
    print(f"Result of {x} / {y} = {div_res}")

if __name__ == '__main__':
    main()