################### Scope ####################

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"Enemies inside function: {enemies}")

# increase_enemies()
# print(f"Enemies outside function: {enemies}")



############ Local Scope #################
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)

# Global Scope #################

# player_health = 10

# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# drink_potion()

# There is no block scope

# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]
# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)

# Modifying Global Scope

enemies = 1

def increase_enemies():
    global enemies
    # enemies += 1
    print(f"Enemies inside function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"Enemies outside function: {enemies}")

# Global constant 

PI = 3.14159