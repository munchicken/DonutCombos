""" DonutCombos - Utility app to create code for multi-donuts-mod """

"""
lists
"""
icings = [ 'none', 'strawberry', 'chocolate', 'blueberry', 'vanilla' ]
sprinkles = [ 'none', 'green', 'blue', 'red', 'yellow', 'orange', 'rainbow' ]
fillings = [ 'none', 'strawberry', 'chocolate', 'vanilla', 'cookieDough', 'brownieBatter' ]
item1 = []
item2 = []
lang = []
recipe = []

"""
create item1 list
"""
for icing in icings:
    for sprinkle in sprinkles:
        for filling in fillings:
            item1.append( 'public static ItemFood ' + icing + sprinkle.capitalize() + filling.capitalize() + 'Donut;' )


"""
create item2 list
"""

"""
create lang list
"""

"""
create recipe list
"""

"""
output lists for copy/paste
"""
print ('ModItems: \n')
for item in item1:
    print (item)
