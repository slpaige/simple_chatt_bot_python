pasta = "tomato, basil, garlic, salt, pasta, olive oil"
apple_pie = "apple, sugar, salt, cinnamon, flour, egg, butter"
ratatouille = "aubergine, carrot, onion, tomato, garlic, olive oil, pepper, salt"
chocolate_cake = "chocolate, sugar, salt, flour, coffee, butter"
omelette = "egg, milk, bacon, tomato, salt, pepper"

food_check = input()

if food_check in pasta:
    print("pasta time!")

if food_check in apple_pie:
    print("apple pie time!")

if food_check in ratatouille:
    print("ratatouille time!")

if food_check in chocolate_cake:
    print("chocolate cake time!")

if food_check in omelette:
    print("omelette time!")
