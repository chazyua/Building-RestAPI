from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(('%Y-%m-%d %H:%M:%S:'))

# data to serve with API
PEOPLE = {
    'Yerep': {
        'fname': 'Art',
        'lname': 'Yerep',
        'timestamp': get_timestamp()
    },
    'Smirnova': {
        'fname': 'Sasha',
        'lname': 'Smirnova',
        'timestamp': get_timestamp()
    },
    'Willis': {
        'fname': 'Bruce',
        'lname': 'Willis',
        'timestamp': get_timestamp()
    }
} 

# create a handler for read (GET) people
def read():
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]