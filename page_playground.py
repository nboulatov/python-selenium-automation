

class BasePage():

    def open(self):
        print('Opening...')


    def click(self):
        print('Clicking...')


    def verify_text(self):
        print('Verifying...')

class LoginPage(BasePage):
    def login(self, username, password):
        print(f'Logging in...{username}:{password}')

    def verify_text(self):
        print('Verifying LOGIN text...')


