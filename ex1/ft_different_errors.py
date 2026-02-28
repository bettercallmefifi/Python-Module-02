def garden_operations() -> None:
    """Test handling of individual error types."""
    try:
        print("Testing ValueError...")
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    print()

    try:
        print("Testing ZeroDivisionError...")
        10 / 0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    print()

    try:
        print("Testing FileNotFoundError...")
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt")
    print()

    try:
        print("Testing KeyError...")
        plant = {"Appel": 1}
        print(plant["missing_plant"])
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'")
    print()


def test_errors_type() -> None:
    print("=== Garden Error Types Demo ===")
    print()
    garden_operations()

    print("Testing multiple errors together...")

    try:
        int("hello")
        10 / 0
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")
    print()

    print("All error types tested successfully")


if __name__ == "__main__":
    test_errors_type()
