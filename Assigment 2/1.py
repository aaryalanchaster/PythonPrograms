#constructor and destructor

class demo:
    def __init__(self):
        print('constructor')

    def __del__(self):
        print('destructor')


obj = demo()
