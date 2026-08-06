import alchemy

air = alchemy.elements.create_air()

print(air)

try:
    print(alchemy.elements.create_earth())
except ValueError as error:
    print(error)
    
