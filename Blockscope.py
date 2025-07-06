game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    if game_level < 5:
        new_enemy = enemies[0]#the scope inside the if or for or while it not count as scope of a - 
        #- varable its based on function!
    print(new_enemy)


