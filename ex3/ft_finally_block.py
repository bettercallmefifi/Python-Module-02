def water_plants(plant_group: list[str]) -> None:
    try:
        print("Opening watering system")
        for plant in plant_group:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"watering {plant}")
    except ValueError as error:
        print(f"Error: {error}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    print("=== Garden Watering System ===")
    print()

    print("Testing normal watering...")
    plant1 = ["tomato", "lettuce", "carrots"]
    water_plants(plant1)
    print("Watering completed successfully!")
    print()

    print("Testing with error...")
    plant2 = ["tomato", None, "carrots"]
    water_plants(plant2)
    print()

    print("Cleanup always happens, even with errors")


if __name__ == "__main__":
    test_watering_system()
