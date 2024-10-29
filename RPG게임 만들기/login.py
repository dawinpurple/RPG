def load_user(username,password):
    with open('login.txt','r') as file:
        for line in file:
            user,pwd=line.strip().split(',')
            if user == username and pwd == password:
                return True
    return False


def add_user(username,password):
    with open('login.txt','r') as file:
        for line in file:
            user,pwd=line.strip().split(',')
            if user == username:
                return False
    with open('login.txt','a') as file:
        file.write(f"{username},{password}\n")

    return True
