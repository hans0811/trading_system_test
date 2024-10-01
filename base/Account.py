class AccountBase:

    def basic_info_avatar_input(self):
        return "//input[@type='file']"

    def basic_info_save_button(self):
        return "//span[text()='保存']/parent::button"


