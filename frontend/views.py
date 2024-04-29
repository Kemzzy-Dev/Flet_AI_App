from flet import *
from pages.welcome_page import Welcome
from pages.main_page import MainPage

def views_handler(page: Page) -> View:
    return {
        '/':View(
            route='/',
            controls=[
                Welcome(page)
            ]
        ),
        '/app':View(
            route='/app',
            controls=[
                MainPage(page)
            ]
        )
    }