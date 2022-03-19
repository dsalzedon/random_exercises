from typing import List, Dict

def group_dishes(food_list: List) -> List:


    recipes = create_recipes(food_list)

    my_ingredients = [ _ for _ in recipes]
    my_ingredients.sort()

    return [[ingredient, *recipes[ingredient]] for ingredient in my_ingredients]


def create_recipes(my_dishes: List) -> Dict:
    my_recipes = {}

    for recipe in my_dishes:
        dish = recipe[0]
        for ingredient in recipe:
            if ingredient != dish:
                try:
                    my_recipes[ingredient].append(dish)
                except KeyError:
                    my_recipes[ingredient] = [dish]

    for ingredient in my_recipes:
        my_recipes[ingredient].sort()

    return my_recipes


def main():

    platos = [
                ["Ensalada", "Tomate", "Pepino", "Ensalada", "Salsa"],
                ["Pizza", "Tomate", "Salchicha", "Salsa", "Masa"],
                ["Quesadilla", "Pollo", "Queso", "Salsa"],
                ["Sandwich", "Ensalada", "Pan", "Tomate", "Queso"]
    ]

    platos2 = [
                ["Pasta", "Salsa de tomate", "Cebollas", "Ajo"],
                ["Pollo al curry", "Pollo","Salsa de curry" ],
                ["Arroz frito", "Arroz", "Cebollas", "Nueces"],
                ["Ensalada","Espinacas", "Nueces"],
                ["Sándwich", "Queso", "Pan"],
                ["Quesadilla", "Pollo", "Queso"]
    ]

    print(group_dishes(platos2))

if __name__ == "__main__":
    main()
