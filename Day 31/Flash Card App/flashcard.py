import pandas as pd
from random import randint, choice

_data = pd.read_csv("data/Chinese_to_spanish.csv")
df = pd.DataFrame(_data)


class Flashcard:
    def __init__(self, data_quantity):
        self.data_quantity = data_quantity
        self.data = df[0:self.data_quantity]
        self.right_cards = pd.DataFrame()

    def select_card(self):
        try:
            card_index = randint(0, len(self.data)-1)
        except ValueError:
            self.data = self.right_cards
            self.right_cards = pd.DataFrame()
            card_index = randint(0, len(self.data) - 1)
        except IndexError:
            self.data = self.right_cards
            self.right_cards = pd.DataFrame()
            card_index = randint(0, len(self.data) - 1)
        return self.data[["Simplified", "Pinyin", "G_Meaning"]].iloc[card_index]

    def remove_right_card(self, row):
        word_index = self.data[self.data["Simplified"] == row["Simplified"]].index
        self.right_cards = pd.concat([self.right_cards, self.data.iloc[word_index]], ignore_index=True)
        self.data = self.data.drop(word_index, inplace=False)
        self.data.reset_index(drop=True, inplace=True)
