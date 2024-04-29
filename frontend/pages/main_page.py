from flet import *
from utils.config import *


class MainPage(UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page


    def build(self):        
        # Create variables that can be manipulated on screen
        self.chatbox_screen = Column(
            width = 400,
            height = 530,
            controls = [] # Controls are added dynamically
            )
        self.inputText = TextField(
            height=50,
            multiline=True,
            autocorrect = True,
            hint_text="Enter Text", 
            bgcolor="#1d2637",
            border_radius = border_radius.all(30),   
        )

        # Return the whole page
        return Column(
            controls=[
                Container(
                    bgcolor='black',
                    height=app_height-20,
                    width=app_width,
                    border_radius = border_radius.all(app_border_radius),
                    padding = padding.only(left=10, right=10),

                    content = Column(
                        controls = [
                            Container(height = 6),
                           
                            Row(
                                alignment = MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    IconButton(icon=icons.MENU, icon_color=colors.WHITE),
                                    Row(
                                        controls = [
                                            IconButton(icon=icons.SEARCH, icon_color=colors.WHITE),
                                            IconButton(icon=icons.NOTIFICATIONS, icon_color=colors.WHITE),
                                        ], 
                                    )
                                ]
                            ),

                            self.chatbox_screen,

                            Row(
                                controls=[
                                    Container(padding=padding.only(top=20, bottom=20), content = (self.inputText)),
                                    IconButton(icon=icons.SEARCH, icon_color=colors.WHITE, on_click=lambda _:self.send_text_to_ai()),
                                ]
                            )
                        ]
                    )
                )
            ]
        )

    def send_text_to_ai(self) -> None:
        text = self.inputText.value
        self.chatbox_screen.controls.append(self.chat_bubble(text, "You"))
        print(len(self.chatbox_screen.controls))

        self.page.update()

    def drawer(self):
        drawer = NavigationDrawer(
            controls=[
                NavigationDrawerDestination(
                    icon=icons.ADD_TO_HOME_SCREEN_SHARP, label="Item 1"
                ),
                NavigationDrawerDestination(icon=icons.ADD_COMMENT, label="Item 2"),
            ],
        )

        return drawer

    # creates a new chat bubble widget
    def chat_bubble(self, text:str, user: str) -> Card:
        return Card(
            content=Container(
                content=Column(
                    [
                        ListTile(
                            leading=Icon(icons.ALBUM),
                            title=Text(user),
                            subtitle=Text(
                                text
                            ),
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )