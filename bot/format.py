from pyrogram.types import InlineKeyboardButton

class Format:
    def __init__(self):
        self.but = []


    def tu_button(self, qwer: list):
        self.but.append(InlineKeyboardButton(text=qwer[0], url=qwer[1]))


    def call_button(self, qwer: list):
        self.but.append(InlineKeyboardButton(text=qwer[0], callback_data=qwer[1]))


    def build_(self, nos: int):
        return [self.but[l:l+nos] for l in range(0, len(self.but), nos)]
