
class LoginBase:

    def login_input(self, input_placeholder):
        return "//input[@placeholder='" + input_placeholder + "']"

    def login_button(self, button_name):
        return "//span[text()='" + button_name + "']/parent::button"


if __name__ == '__main__':
    print(LoginBase().login_input('用户名'))
    print(LoginBase().login_button('密码'))

