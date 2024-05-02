import pickle

# Є словник з друзями, де ключ – людина, а значення –
# список друзів. Користувач вводить імена двох людей,
# які є друзями, повторює це певну кількість разів,
# після чого дані зберігаються у файл.
# Завантажте дані назад та виведіть на екран.

def add_friend(ammount):
    friends = {}
    for i in range(ammount):
        friend = input(f"Input {i+1}st friends name: ")
        friends[friend] = []
        num = int(input(f"How many friends do you want to add to {friend}: "))
        for j in range(num):
            friend_from_group = input(f"Input {j + 1}th friend from {friend}: ")
            friends[friend].append(friend_from_group)
    # print(friends)

    with open("friends_data.pickle", "wb") as file:
        pickle.dump(friends, file)

def load_data(file_name):
    with open(file_name, "rb") as file:
        read_data = pickle.load(file)
    print(f"Loaded data: {read_data}")


add_friend(3)
load_data("friends_data.pickle")
