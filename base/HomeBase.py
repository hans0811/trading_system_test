class HomeBase:
    def wallet_switch(self):
        return "//span[contains(@class,'switch')]"

    def logo(self):
        return "//div[contains(text(), '二手')"

    def welcome(self):
        return "//span[starts-with(text(), '歡迎您回來')]"

    def show_date(self):
        return "//div[text()='我的日曆']/following-sibling::div"

    def home_user_avatar(self):
        return "//span[contains(text(), '歡淫您回來')]/parent::div/preceding-sibling::div//img"

    def home_user_avatar_2(self):
        return"//span[text()='我的地址']/ancestor::div[@class='first_card']/div[contains(@class,'avatar')]//img"

