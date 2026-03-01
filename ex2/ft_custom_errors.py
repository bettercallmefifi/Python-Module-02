class GardenError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str) -> None:
        super().__init__(message)


def test_plant_error() -> None:
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print("Caught PlantError:", error)


def test_water_error() -> None:
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print("Caught WaterError:", error)


def test_garden_error() -> None:
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as error:
        print("Caught a garden error:", error)

    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as error:
        print("Caught a garden error:", error)


def test_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===")
    print()

    print("Testing PlantError...")
    test_plant_error()
    print()

    print("Testing WaterError...")
    test_water_error()
    print()

    print("Testing catching all garden errors...")
    test_garden_error()
    print()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
