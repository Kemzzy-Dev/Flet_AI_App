from flet import *
from utils.config import *

class Welcome(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return Column(
            controls=[
                Container(
                    height=app_height-20,
                    width=app_width,
                    bgcolor='blue',
                    border_radius = border_radius.all(app_border_radius),

                    content=Column(
                        spacing = 10,
                        controls = [
                            Container(
                                padding = padding.all(0),
                                bgcolor = colors.WHITE,
                                margin = margin.only(bottom=0),
                                content = (Image('../images/welcome_logo.svg'))
                            ),
                            Row(
                                alignment = MainAxisAlignment.CENTER,
                                controls=[
                                    Text('Welcome to Summarize',color="black", size=20),
                                ]
                            ),
                            Row(
                                alignment = MainAxisAlignment.CENTER,
                                controls = [
                                    ElevatedButton(
                                        "Continue",
                                        on_click = lambda _:self.page.go("/app")
                                    ),
                                ]
                            ),

                        ]
                    ) 
                )
            ]   
        )