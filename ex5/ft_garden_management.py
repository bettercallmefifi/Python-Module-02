class GardenError(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class PlantError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)


class WaterError(GardenError):
    def __init__(self, message: str):
        super().__init__(message)


class GardenManager:
    def __init__(self, name: str):
        if not name:
            raise GardenError("Garden name cannot be empty!")
        self.name: str = name
        self.plants: list[str] = []

    def add_plant(self, plant_name: str) -> None:
        try:
            if not plant_name:
                raise PlantError("Plant name connot be empty!")
            self.plants.append(plant_name)
            print(f"Added {plant_name} successfully")
        except PlantError as error:
            print(f"Error adding plant: {error}")

    def water_plant(self) -> None:
        print()
        print("Watering plants...")
        try:
            print("Opening watering system")
            if not self.plants:
                raise WaterError("No plants to water")

            for plant in self.plants:
                print(f"Watering {plant} - success")

        except WaterError as error:
            print(f"Caught GardenError: {error}")

        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(
            self,
            plant_name: str,
            water_level: int,
            sunlight_hours: int) -> None:
        if not plant_name:
            raise PlantError("Plant name cannot be empty!")

        if water_level < 1:
            raise PlantError(
                f"Water level {water_level} is too low (min 1)")
        if water_level > 10:
            raise PlantError(
                f" Water level {water_level} is too high (max 10)")

        if sunlight_hours < 2:
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too low (min 2)")
        if sunlight_hours > 12:
            raise PlantError(
                f"Sunlight hours {sunlight_hours} is too high (max 12)")

        print(
            f"{plant_name}: healthy "
            f"(water: {water_level}, sun: {sunlight_hours})"
            )


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    print()

    garden = GardenManager("My own Garden")
    print("Adding plants to garden...")

    garden.add_plant("tomato")
    garden.add_plant("lettuce")
    garden.add_plant("")

    garden.water_plant()

    print()
    print("Checking plant health...")
    try:
        garden.check_plant_health("tomato", 5, 8)
        garden.check_plant_health("lettuce", 15, 6)
    except PlantError as error:
        print(f"Error checking lettuce: {error}")

    print()
    print("Testing error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except WaterError as error:
        print(f"caught GardenError: {error}")
        print("System recovered and continuing...")

    print()
    print("Garden management system test complete")


test_garden_management()
