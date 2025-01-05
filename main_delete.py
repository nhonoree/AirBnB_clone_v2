#!/usr/bin/python3
""" Test delete feature for FileStorage """
from models.engine.file_storage import FileStorage
from models.state import State

# Initialize FileStorage
fs = FileStorage()

# Reload data
fs.reload()

# All States initially
all_states = fs.all(State)
print("Initial States count:", len(all_states))
for state_key in all_states:
    print(all_states[state_key])

# Create a new State
state_1 = State()
state_1.name = "California"
fs.new(state_1)
fs.save()

# Verify the addition
all_states = fs.all(State)
print("\nAfter adding California:", len(all_states))
for state_key in all_states:
    print(all_states[state_key])

# Add another State
state_2 = State()
state_2.name = "Nevada"
fs.new(state_2)
fs.save()

# Verify the addition
all_states = fs.all(State)
print("\nAfter adding Nevada:", len(all_states))
for state_key in all_states:
    print(all_states[state_key])

# Delete California
fs.delete(state_1)
fs.save()

# Verify deletion
all_states = fs.all(State)
print("\nAfter deleting California:", len(all_states))
for state_key in all_states:
    print(all_states[state_key])
