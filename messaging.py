class Message:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

class MessagingSystem:
    def __init__(self):
        self.users = set()
        self.messages = []

    def register_user(self, username):
        if username not in self.users:
            self.users.add(username)
            print(f"User '{username}' registered.")
        else:
            print(f"User '{username}' already exists.")

    def send_message(self, sender, receiver, content):
        if sender in self.users and receiver in self.users:
            msg = Message(sender, receiver, content)
            self.messages.append(msg)
            print(f"Message sent from '{sender}' to '{receiver}'.")
        else:
            print("Both users must be registered.")

    def read_messages(self, username):
        user_messages = [msg for msg in self.messages if msg.receiver == username]
        if user_messages:
            print(f"Messages for {username}:")
            for msg in user_messages:
                print(f"From {msg.sender}: {msg.content}")
        else:
            print(f"No messages for {username}.")

system = MessagingSystem()
system.register_user("Alice")
system.register_user("Bob")
system.send_message("Alice", "Bob", "Hello Bob!")
system.read_messages("Bob")
