class VacuumEnvironment:
    def __init__(self):
        # Initialize squares A and B to be either 'Clean' or 'Dirty'
        self.locations = {
            "A": "clean",
            "B": "dirty"
        }

    def is_dirty(self, location):
        # Return True if the specified location is Dirty
        return self.locations[location] == "dirty"

    def clean(self, location):
        # Clean the dirt from the specified location
        self.locations[location] = "clean"

    def status(self):
        # Print the current status of the environment
        for location in self.locations:
            status = self.locations[location]
            print(f"Location {location} is {status}")

class VacuumAgent:
    def __init__(self, environment):
        # The agent is initialized within an environment
        # The vacuum agent starts at location A
        self.environment = environment
        self.location = "A"

    def move_right(self):
        # Move the agent to the right (from A to B)
        self.location = "B"

    def move_left(self):
        # Move the agent to the left (from B to A)
        self.location = "A"

    def suck(self):
        # If the current location is dirty, suck the dirt
        if self.environment.is_dirty(self.location):
            self.environment.clean(self.location)
            print(f"Cleaning location {self.location}")

    def perceive_and_act(self):

        # The agent perceives its environment and takes action
        if self.environment.is_dirty(self.location):
            print(f"Location {self.location} is dirty.")
            self.suck()
        else:
            print(f"Location {self.location} is clean.")
        
        # Decide to move to the other square if it's at A, otherwise it's at B and should move to A
        if self.location == "A":
            self.move_right()
        else:
            self.move_left()
        
        # The environment status printed after each action
        self.environment.status()

# Creating the environment and the agent
environment = VacuumEnvironment()
agent = VacuumAgent(environment)

# Running the agent's behavior for a few iterations
for _ in range(5):
    agent.perceive_and_act()
    print("---")
