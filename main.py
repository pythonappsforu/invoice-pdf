import pandas as pd
from receipt import Receipt


df = pd.read_csv("articles.csv", dtype={"id": str})
class Article:
    def __init__(self, article_id):
        self.id = article_id
        self.name = df.loc[df['id'] == self.id, 'name'].squeeze()
        self.price = df.loc[df['id'] == self.id, 'price'].squeeze()

    def available(self):
        in_stock = df.loc[df['id'] == self.id, 'in stock'].squeeze()
        return in_stock



print(df)
article_ID = input("Choose an article to buy: ")
article = Article(article_id=article_ID)
if article.available():
    receipt = Receipt(article)
    receipt.generate_pdf()
else:
    print("No such article in stock.")


