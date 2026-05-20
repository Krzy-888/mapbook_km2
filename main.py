# definicja prostej struktury danych obejmujacej przykladowego uzytkownika

users = [
    {"name": "Artur", "location": "Łomża",
     "posts": ["Sprzedam mercedesa", "Kupie skrzynie biegow", "Ratunku co robić po wypadku?",
               "Kto dzisiaj idzie biegać?"]},
    {"name": "Daniel", "location": "Legionowo",
     "posts": ["Moj kod nie dziala, pomocy!"]},
    {"name": "Kamil", "location": "Ciechanów",
     "posts": ["Czy ktoś już zrobił sprawozdanie z PPyth?"]},

]


def read_users(users_data: list) -> None:
    for user in users_data:
        print(f"Twoj znajomy {user['name']} z miejscowości {user['location']} opublikował post {user['posts'][-1]}")


def add_user(users_data: list) -> None:
    users_data.append({"name": input("Podaj imie użytkownika: "), "location": input("Podaj swoją lokzalizację: "),
                       "posts": ["Dołączono do znajomych"]})


def remove_user(users_data: list) -> None:
    user_to_remove = input("Podaj imię znajomego do usunięcia: ")
    for user in users_data:
        if user["name"] == user_to_remove:
            users.remove(user)



def update_user(users_data: list) -> None:
    user_to_update = input("Podaj imię znajomego do update: ")
    for user in users_data:
        if user["name"] == user_to_update:
            user["name"] = input("Podaj nowę imię użytkownika: ")
            user["location"] = input("Podaj nową lokalizację: ")

def update_user_post(users_data: list) -> None:
    user_to_update = input("Podaj imię znajomego do update: ")
    for user in users_data:
        if user["name"] == user_to_update:
            user["posts"].append(input("Co słychać? "))



while True:
    print("==========MENU==========")
    print("0 - zakończ program")
    print("1 - wyświetl znajomych")
    print("2 - dodanie znajomego")
    print("3 - usuwanie znajomego")
    print("4 - update znajomego")
    print("5 - update postów")

    choice=input("Wybierz opcje w menu: ")
    print (f"Wybrano opcję {choice}")
    if choice == "0":
        break

    if choice == "1":
        read_users(users)
    if choice == "2":
        add_user(users)
    if choice == "3":
        remove_user(users)
    if choice == "4":
        update_user(users)
    if choice == "5":
        update_user_post(users)