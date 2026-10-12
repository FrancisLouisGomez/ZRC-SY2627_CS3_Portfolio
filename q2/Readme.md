class PSHS_Galaxy:
    def __init__(self, planet, monster):
        self.planet = planet
        self.monster = monster

    def solar_system(self):
        print(f"{self.monster} is from planet {self.planet}")


class Nationality(PSHS_Galaxy):
    def __init__(self, planet, monster, language):
        super().__init__(planet, monster)
        self.language = language

    def display_info(self):
        return f"Origin: {self.planet} | Guardian: {self.monster} | Speaks: {self.language}"


class Earthling(Nationality):
    def __init__(self, planet, monster, language, country):
        super().__init__(planet, monster, language)
        self.country = country

    def introduce(self):
        return f"Hello! I am a human from {self.country} on planet {self.planet}."


class Cybertronian(Nationality):
    def __init__(self, planet, monster, language, faction):
        super().__init__(planet, monster, language)
        self.faction = faction

    def transform_and_roll_out(self):
        return f"Fighting as an {self.faction} in the language of {self.language}!"


class Alien(PSHS_Galaxy):
    def __init__(self, planet, monster, powers):
        super().__init__(planet, monster)
        self.powers = powers

    def use_power(self):
        return f"The alien from {self.planet} uses {self.powers}!"


class BountyHunter(Alien):
    def __init__(self, planet, monster, powers, target_bounty):
        super().__init__(planet, monster, powers)
        self.target_bounty = target_bounty

    def track_target(self):
        return f"Hunting down {self.target_bounty} using {self.powers}!"


class Symbiote(Alien):
    def __init__(self, planet, monster, powers, host_name):
        super().__init__(planet, monster, powers)
        self.host_name = host_name

    def bond(self):
        return f"We are bonding with {self.host_name} to double our {self.powers}!"