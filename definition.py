import pandas


class Definition:

    def __init__(self, term):
        self.term = term

    def get(self):
        df = pandas.read_csv("data.csv")
        result = tuple(df.loc[df['word'] == self.term]['definition'])
        return result


if __name__ == "--main__":
    acid_rain = Definition(term="acid rain")
    print(acid_rain.get())
