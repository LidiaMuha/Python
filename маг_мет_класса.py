class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1

    def __add__(self, other):  # возвращается кортеж (можно и списком и словарём)
        return (f"{self.text} {other.text}", self.votes_qty + other.votes_qty)

    # Этот метод вызывается при использовании == на объекте
    def __eq__(self, other):
        return (self.text == other.text) and (self.votes_qty == other.votes_qty)


first_comment = Comment("Первый комментарий")
first_comment.upvote()
# print(first_comment.text, first_comment.votes_qty)
second_comment = Comment("Второй комментарий")
second_comment.upvote()
thirth_comment = Comment("Первый комментарий")
thirth_comment.upvote()
# print(first_comment.text, first_comment.votes_qty)

print(first_comment + second_comment)
print(first_comment == thirth_comment)
print(first_comment == second_comment)
