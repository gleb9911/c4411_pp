class BuildingError(Exception):
    def __str__(self):
      return f"With so much material the house cannot be built!"

