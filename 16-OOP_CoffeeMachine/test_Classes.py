
# import turtle

# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)

# my_screen = turtle.Screen()
# print(f"Screen Height: {my_screen.canvheight}")
# print(f"Screen Width: {my_screen.canvwidth}")
# my_screen.exitonclick()

# https://pypi.org/project/prettytable/
from prettytable import PrettyTable
table = PrettyTable()
# row by row
table.field_names = ["Pokemon Name", "Type"]
table.add_rows([
    ["Pikachu", "Electric"],
    ["Squirtle", "Water"],
    ["Charmander", "Fire"],
])
table.align = "l"
print(table)