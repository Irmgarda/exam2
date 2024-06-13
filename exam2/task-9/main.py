# Class: Country
# Objective: Enhance the `Country` class to include an attribute `is_big` and a method to compare population density with another country.
# Details:
# - The `is_big` attribute should be set to True if either of the following criteria are met:
#   - The population is greater than 250 million.
#   - The area is larger than 3 million square km.
# - The class should also include a method `compare_pd` that compares the population density of the country with another country object.
# - The `compare_pd` method should return a string in the following format: "{country} has a {smaller / larger} population density than {other_country}".
# - Population density is calculated as the population divided by the area.

class Country:
    def __init__(self, name: str, population: int, area: float):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self._check_is_big()

    def _check_is_big(self) -> bool:
       #The `is_big` attribute should be set to True if either of the following criteria are met:
        return self.population > 250_000_000 or self.area > 3_000_000

    def compare_pd(self, other_country) -> str:
        self_density = self.population / self.area
        other_density = other_country.population / other_country.area
        #Compares the population density of the country with another country object.
        if self_density > other_density:
            comparison = "larger"
        elif self_density < other_density:
            comparison = "smaller"
        else:
            comparison = "the same"

        return f"{self.name} has a {comparison} population density than {other_country.name}"

# Examples:
australia = Country("Australia", 23545500, 7692024)
andorra = Country("Andorra", 76098, 468)

print(australia.is_big)  # Expected: True
print(andorra.is_big)  # Expected: False
print(andorra.compare_pd(australia))  # Expected: "Andorra has a larger population density than Australia"
