class Comment:

    def __add__(self, other: "Comment") -> dict:
        return {
            'merged_text': f'{self.text} {other.text}',
            'total_votes': self.votes + other.votes
        }

    def __eq__(self, other: "Comment") -> bool:
        return (
            id(self) == id(other)) or (
            self.text == other.text and
            self.votes == other.votes)

    def __init__(self, text: str, votes: int = 0):
        self.text = text
        self.votes = votes

    def __str__(self) -> str:
        return f'Comment object at {hex(id(self))} {self.__dict__}'

    def upvote(self, votes_to_add: int):
        self.votes += votes_to_add


# Создаём комментарии.

comment_1 = Comment('Первый комментарий.', 1)
comment_2 = Comment('Второй комментарий.', 2)

print(comment_1)
print(comment_2)

# Добавляем голоса.

comment_1.upvote(3)
comment_2.upvote(4)

print(comment_1)
print(comment_2)

# Тестируем объединение.

print()
print('comment_1 + comment_2:', comment_1 + comment_2)

# Тестируем проверку на равенство.

comment_3 = Comment('Первый комментарий.', 4)
comment_4 = Comment('Второй комментарий.', 6)

print()
print(comment_1)
print(comment_2)
print(comment_3)
print(comment_4)

comments = {
    'comment_1': comment_1,
    'comment_2': comment_2,
    'comment_3': comment_3,
    'comment_4': comment_4
}

for k1, v1 in comments.items():
    print()
    for k2, v2 in comments.items():
        print(f'{k1} == {k2}:', v1 == v2)
