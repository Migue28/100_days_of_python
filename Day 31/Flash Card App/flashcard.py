import pandas as pd
from random import randint, choice

data = pd.read_csv("data/Chinese_to_spanish.csv")
df = pd.DataFrame(data)


class Flashcard:
    def __init__(self):
        self.card_index = randint(0, 5)
        self.wrong_cards = []
        self.wrong_card_index = 1

    def select_card(self):
        return df[["Simplified", "Pinyin", "G_Meaning"]].iloc[self.card_index]


flash = Flashcard()
flash.card_with_loc()
