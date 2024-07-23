def register_user():
    x=input("register user:")
    return x
user1=register_user()
user2=register_user()
chat={
    user1:[],
    user2:[]
}
def sending_message():
    print(f'{user1}:Type "s" to send a message(if no write "d"):')
    x=input()
    if x =="s":
        print(f"message from {user1} to {user2}:")
        message=input()
        print(f'{user2}:You received a message')
        chat[user1] += ["s"]
        chat[user2] += ["r"]
        return message
    elif x=="d":
        print(f'{user2}:Type "s" to send a message(if no write "d"):')
        y=input()
        if y =="s":
            print(f"message from {user2} to {user1}:")
            message=input()
            print(f'{user1}:You received a message')
            chat[user2] += ["s"]
            chat[user1] += ["r"]
            return message
        elif y=="d":
            print("")
    else:
        print("please try again")
    return message
message=sending_message()
chat[user1] += [message]
chat[user2] += [message]
class ChatSystem:
    def view_user_messages(self, username):
            if username in self.view_user_messages:
                self.view_user_messages[username].view_messages()
            else:
                print(f"User '{username}' is not registered.")
