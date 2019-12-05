from classes.game import Person, bcolors

magic = [{"name": "Fire", "cost": 10, "dmg":120},
         {"name": "Water", "cost": 5, "dmg":80},
         {"name": "Air", "cost": 7, "dmg":113}]


player = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS!" + bcolors.ENDC)

while running:
    print("=====================")
    player.choose_action()
    choice = input("Choose action:")

    if choice == '1':
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", str(dmg), "points of damage. Enemy HP: " + str(enemy.get_stats()["hp"]))
    elif choice == '2':
        player.choose_magic()
        magic_choice = input("Choose magic:")
        magic_dmg = player.generate_spell_damage(int(magic_choice) - 1)
        cost = int(player.get_spell(int(magic_choice) - 1)["cost"])
        player.reduce_mp(cost)
        enemy.take_damage(magic_dmg)                
        print("You cast " + player.get_spell(int(magic_choice) - 1)["name"] + " for", str(magic_dmg), "points of damage. Enemy HP: " + str(enemy.get_stats()["hp"]))
        print("Your MP: " + str(player.get_stats()["mp"]))

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacked for", str(enemy_dmg), "points of damage. Your HP: " + str(player.get_stats()["hp"]))

    if enemy.get_stats()["hp"] == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif player.get_stats()["hp"] == 0:
        print(bcolors.FAIL + "You lost battle!" + bcolors.ENDC)
        running = False
