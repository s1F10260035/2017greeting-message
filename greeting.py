from datetime import datetime

def greet(name):
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'
    elif hour <= 17:
        message = 'Hello'
    else:
        message = 'Good evening'
    result = message + name + '-san!'
    print(result)


greet('Inoue')
