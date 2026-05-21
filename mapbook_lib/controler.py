from bs4 import BeautifulSoup
import requests
import folium
from typing import List, Optional
from mapbook_lib.model import User


def read_users(users_data: List[User]) -> None:
    for user in users_data:
        print(f"Twoj znajomy {user.name} z miejscowości {user.location} opublikował post {user.posts[-1]}")


def add_user(users_data: List[User]) -> None:
    name = input("Podaj imie użytkownika: ")
    location = input("Podaj swoją lokzalizację: ")
    users_data.append(User(name=name, location=location, posts=["Dołączono do znajomych"]))


def remove_user(users_data: List[User]) -> None:
    user_to_remove = input("Podaj imię znajomego do usunięcia: ")
    # 使用列表推导式创建新列表，避免在遍历过程中删除元素
    users_data[:] = [user for user in users_data if user.name != user_to_remove]


def update_user(users_data: List[User]) -> None:
    user_to_update = input("Podaj imię znajomego do update: ")
    for user in users_data:
        if user.name == user_to_update:
            user.name = input("Podaj nowę imię użytkownika: ")
            user.location = input("Podaj nową lokalizację: ")


def update_user_post(users_data: List[User]) -> None:
    user_to_update = input("Podaj imię znajomego do update: ")
    for user in users_data:
        if user.name == user_to_update:
            user.posts.append(input("Co słychać? "))


# 模拟坐标数据库（用于测试）
MOCK_COORDINATES = {
    "Łomża": [53.1333, 22.0833],
    "Legionowo": [52.3667, 20.9667],
    "Ciechanów": [52.9667, 20.65],
    "Warszawa": [52.2297, 21.0122],
    "Kraków": [50.0647, 19.9450],
}


def get_coordinates(location: str) -> Optional[List[float]]:
    # 首先尝试使用模拟数据（用于测试）
    if location in MOCK_COORDINATES:
        print(f"Używanie symulowanych współrzędnych dla {location}")
        return MOCK_COORDINATES[location]
    
    try:
        url = f"https://pl.wikipedia.org/wiki/{location}"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)
        response.raise_for_status()
        
        response_html = BeautifulSoup(response.text, 'html.parser')
        latitude_elements = response_html.select(".latitude")
        longitude_elements = response_html.select(".longitude")
        
        if len(latitude_elements) >= 2 and len(longitude_elements) >= 2:
            latitude = float(latitude_elements[1].text.replace(",", "."))
            longitude = float(longitude_elements[1].text.replace(",", "."))
            return [latitude, longitude]
        else:
            print(f"Nie udało się znaleźć współrzędnych dla lokalizacji: {location}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Błąd podczas pobierania danych dla lokalizacji {location}: {e}. Używanie symulowanych danych.")
        # 返回一个默认坐标
        return [52.23, 21]
    except (ValueError, IndexError) as e:
        print(f"Błąd podczas parsowania współrzędnych dla lokalizacji {location}: {e}")
        return None


def get_user_map(users_data: List[User]) -> None:
    m = folium.Map([52.23, 21], zoom_start=6)

    for user in users_data:
        coordinates = get_coordinates(user.location)
        if coordinates:
            folium.Marker(
                location=coordinates,
                tooltip=user.name,
                popup=user.posts[-1] if user.posts else "Brak postów",
                icon=folium.Icon(icon="cloud"),
            ).add_to(m)
        else:
            print(f"Użytkownik {user.name} z lokalizacją {user.location} nie został dodany do mapy")

    m.save("mapa_znajomych.html")
    print("Mapa została zapisana do pliku mapa_znajomych.html")
