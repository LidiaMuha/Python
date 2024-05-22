class Comment:
    def __init__(self, text, initial_votes_qty=0):
        self.text = text
        self.votes_qty = initial_votes_qty

    def upvote(self, qty):
        self.votes_qty += qty


first_comment = Comment("Первый комментарий", 10)

# создан объект, у которого есть СОБСТВЕННЫЕ артрибуты text и votes_qty

print(first_comment.text)
print(first_comment.votes_qty)

first_comment.upvote(5)

print(first_comment.votes_qty)
