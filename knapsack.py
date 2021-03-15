# i apologize for how hard this is to read without comments
# i just really like cryptic Python syntax!!
# i think at least all the variable names are easy to follow
# spacing/formatting brought to you by black

import json  # to read our parameters


def knapsack(items, totalItems, size, packedItems, totalPackedItems):
    # this function... honestly... just calls packing and returns its values to the proper variables
    # but I just did want this one to have the closest format possible to described in the homework
    # since, you know, I'm using Python and all
    packedSack = packing(items, totalItems, size)
    packedItems = packedSack.items
    totalPackedItems = len(packedItems)
    packedWeight = packedSack.size
    return packedWeight, packedItems, totalPackedItems


def packing(items, totalItems, size):
    # dynamically calculates optimal knapsack packing
    # returns an object that holds a list of items and its total weight
    # which should be as close to the target as possible

    # interesting line, generates an item*unit table
    # full of freshly constructed objects that hold a size integer and an item list
    # set to 0 and empty to initialize
    packingTable = [
        [type("", (object,), {"size": 0, "items": []}) for x in range(0, size + 1)]
        for x in range(0, totalItems + 1)
    ]

    # our main loop to fill out the table,
    # we go through our max possible items through our max possible size...
    # that's a totalItems*size runtime!
    for item in range(0, totalItems + 1):
        for unit in range(0, size + 1):
            # so, as a base case, if our current item or unit index is 0
            # we just make sure our spot at that point is empty
            if item == 0 or unit == 0:
                packingTable[item][unit].size = 0
                packingTable[item][unit].items = []
            # here's where the crucial stuff happens
            # if our current item is less than the current size
            elif items[item - 1] <= unit:
                # we check if it would be a better choice than the last item we added for this size
                if (
                    packingTable[item - 1][unit - items[item - 1]].size
                    + items[item - 1]
                    > packingTable[item - 1][unit].size
                ):
                    # if it is we update the size at this node
                    packingTable[item][unit].size = (
                        packingTable[item - 1][unit - items[item - 1]].size
                        + items[item - 1]
                    )
                    # and we copy our previous list, appending our new item
                    packingTable[item][unit].items = packingTable[item - 1][
                        unit - items[item - 1]
                    ].items + [items[item - 1]]
                # if our previous choice was better, we just copy it instead
                else:
                    packingTable[item][unit] = packingTable[item - 1][unit]
            # in any other case, we just copy the last item list we picked for this size.
            else:
                packingTable[item][unit] = packingTable[item - 1][unit]
    # by the end our final node should contain the best list for max size!
    return packingTable[totalItems][size]


# we get our parameters from knapsack.json
# we are expecting the json to contain a single object
# with elements size, containing an integer
# and items containing an integer array
getKnapsack = json.load(open("knapsack.json"))
# this is just the little drawing that shows up at the end...
# for flavor, you know!!
art = open("art.txt")
# here we're just unpacking (heh) the data we got from the json
size = getKnapsack["size"]
items = getKnapsack["items"]
totalItems = len(items)
# and here we initialize our final variables
packedItems = []
totalPackedItems = 0
packedWeight = 0
# which we then get by calling knapsack which returns the 3 values!!
packedWeight, packedItems, totalPackedItems = knapsack(
    items, totalItems, size, packedItems, totalPackedItems
)

# so all that's left is to print out everything
# i gave it... a videogame dialogue format??
print("your knapsack can carry a weight of ", size)
print(
    "your storage has ",
    totalItems,
    " items  with a total weight of ",
    sum(items),
    " and looks like this:",
)
print(items)
print("\nwe managed to pack this much weight: ", packedWeight)
print("and your inventory looks like this:")
print(packedItems)
print("holding ", totalPackedItems, " items")
for line in art: print(line.rstrip())
print("... did you need something else?")
print("...")
print("ah, I guess you want to see the program. sure, here you go: \n\n\n")
for line in open("knapsack.py"): print(line.rstrip())  # this is what you're reading now!!
