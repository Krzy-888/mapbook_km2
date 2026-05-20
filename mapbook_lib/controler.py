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
            users_data.remove(user)



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