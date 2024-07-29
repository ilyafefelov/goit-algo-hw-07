class CommentNode:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0):
        indent = " " * (level * 4)
        if self.is_deleted:
            print(f"{indent}Цей коментар було видалено.")
        else:
            print(f"{indent}{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(level + 1)

# Приклад використання
root_comment = CommentNode("Яка чудова книга!", "Бодя")
reply1 = CommentNode("Книга повне розчарування :(", "Андрій")
reply2 = CommentNode("Що в ній чудового?", "Марина")

# Додаємо відповіді до кореневого коментаря
root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

# Test CommentNodes
reply1_1 = CommentNode("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply2_1 = CommentNode("Мені теж цікаво.", "Іван")
reply2.add_reply(reply2_1)

reply1_1_1 = CommentNode("Цілком згоден!", "Петро")
reply1_1.add_reply(reply1_1_1)

reply2_1_1 = CommentNode("Можливо, у тебе є інша думка?", "Олег")
reply2_1.add_reply(reply2_1_1)

reply1.remove_reply()

# Test
root_comment.display()
