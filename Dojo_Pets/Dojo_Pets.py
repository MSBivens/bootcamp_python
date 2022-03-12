# Use modules to serparate out the classes into different files

from modules.pet import Pet
from modules.ninja import Ninja

# Make an instance of the a Ninja and assign them an instance of a pet to the pet attribute

the_treats = ['bone', 'bacon_bits', 'meatball']
the_food = ['kibble', 'hamburger']

drover = Pet("drover", "dog", "chase shadows", "woof")
mike = Ninja("mike", "bivens", drover, the_treats, the_food)

# Have the Ninja feed, walk, and bathe their pet
mike.feed()
mike.walk()
mike.bathe()