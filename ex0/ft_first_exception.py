def check_temperature(temperature: str) -> int:
    try:
        value: str = int(temperature)
    except ValueError:
        raise ValueError(f"'{temperature}' is not a valide number")

    if value < 0:
        raise ValueError(f"{value}°C is too cold for plants (min 0°C)")
    elif value > 40:
        raise ValueError(f"{value}°C is too hot for plants (max 40°C)")

    return value


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===\n")

    tests = ["25", "abc", "100", "-50"]

    for test in tests:
        print(f"Testing temperature: {test}")
        try:
            result = check_temperature(test)
            print(f"Temperature {result}°C is perfect for plants!")
        except ValueError as error:
            print(f"Error: {error}")
        print()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
