from flet import *
from views import views_handler
from utils.config import *

def main(page: Page): 
    page.window_height = app_height
    page.window_width = app_width
    # page.window_title_bar_hidden = True
    # page.window_title_bar_buttons_hidden = True
    # page.window_frameless = True 
    page.bgcolor = colors.TRANSPARENT
    page.window_bgcolor = colors.TRANSPARENT
    page.expand = True     

    # Function to change the route when a view is clicked
    def route_change(route):
        page.views.clear
        page.views.append(
            views_handler(page)[page.route]
        )
        page.update()

    # Function to reverse the route when a view is clicked
    def reverse_route(route):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = reverse_route
    page.go('/')
    

app(target=main)