import pygame
import requests

API_KEY = "e3fc2f0f5ae589da1db7dfd1bfbb03f5"
CITY = "Нефтеюганск"  

params = {"q": CITY, "appid": API_KEY, "units": "metric", "lang": "ru"} 
response = requests.get("http://api.openweathermap.org/data/2.5/weather?", params=params)
weather_data = response.json()
temperature = weather_data["main"]["temp"]
weather_desc = weather_data["weather"][0]["description"]  
city_name = weather_data["name"]

pygame.init()
width = 400
height = 200
screen = pygame.display.set_mode((width, height))

# Шрифты
font_city = pygame.font.Font(None, 36)
font_temp = pygame.font.Font(None, 72)
font_weather = pygame.font.Font(None, 28)

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)

# Загружаю картинки
sun_img = pygame.image.load("asets/sun.png").convert_alpha()
rain_img = pygame.image.load("asets/rain.png").convert_alpha()
cloud_img = pygame.image.load("asets/cloyd.png").convert_alpha()
wind_img = pygame.image.load("asets/wind.png").convert_alpha()

# Масштабирую картинки
sun_img = pygame.transform.scale(sun_img, (150, 150))
rain_img = pygame.transform.scale(rain_img, (150, 150))
cloud_img = pygame.transform.scale(cloud_img, (150, 150))
wind_img = pygame.transform.scale(wind_img, (150, 150))

# Выбираю картинку по описанию
if weather_desc == "ясно":
    weather_image = sun_img
elif weather_desc == "дождь":
    weather_image = rain_img
elif "облачно" in weather_desc:
    weather_image = cloud_img
elif "ветер" in weather_desc:
    weather_image = wind_img
else:
    weather_image = None

city_text = font_city.render(city_name.upper(), True, black)  
if temperature > 20:
    temp_color = (255, 0, 0) # Крас
elif 0 <= temperature <= 20:
    temp_color = (255, 255, 0) # Жёлт
elif temperature < 0:
    temp_color = (0, 0, 255)   # Син
temp_text = font_temp.render(f"{temperature}°", True, temp_color)

# Рендер текста
city_text = font_city.render(city_name.upper(), True, black)  
temp_text = font_temp.render(f"{temperature}°", True, temp_color)
weather_text = font_weather.render(weather_desc, True, black)

# Размеры виджета
rect_width, rect_height = 380, 180
border_radius = 20

def wd_weather(x, y):
    # Рисую белый прямоугольник с закруглениями
    rect = pygame.Rect(x, y, rect_width, rect_height)
    pygame.draw.rect(screen, white, rect, border_radius=border_radius)

    city_x = x + 90
    city_y = y + 10

    icon_x_default = x + 1
    icon_y = y + 10

    temp_x = x + 170
    temp_y = y + 50

    weather_x = x + 135
    weather_y = temp_y + 60

    
    weather_text_width = weather_text.get_width()
    right_edge_weather = weather_x + weather_text_width
    right_edge_rect = x + rect_width

    icon_x = icon_x_default
    

    # Отрисовка
    screen.blit(city_text, (city_x, city_y))
    if weather_image:
        screen.blit(weather_image, (icon_x, icon_y))
    screen.blit(temp_text, (temp_x, temp_y))
    screen.blit(weather_text, (weather_x, weather_y))


# Основной цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)

    wd_weather(10, 10)

    pygame.display.flip()

pygame.quit()


 
