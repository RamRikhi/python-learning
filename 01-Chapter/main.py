from datetime import datetime

def send_greeting(name):
    current_time = datetime.now()
    current_time = current_time.hour
    if current_time <= 12:
        print("Good morning " + name)
        print(current_time)
    elif current_time <= 16:
        print("Good afternoon " + name)
    elif current_time <= 23:
        print("Good evening " + name)
    else:
        print("Good night " + name)

if __name__ == '__main__':
    send_greeting('Rikhi')