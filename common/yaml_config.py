import yaml

from common.tools import get_project_path, sep

path = "/Users/hans/Desktop/code/python/automation/imooc_pytest/trading_system_test/config/environment.yaml"

class GetConf:
    def __init__(self):
        with open(get_project_path() + sep(["config", "environment.yaml"], add_sep_before=True),
                  "r",
                  encoding="utf-8") as env_file:
            self.env = yaml.load(env_file, Loader=yaml.FullLoader)
            # print(self.env)
            # print(env_file.read())

    def get_username_password(self, user):
        return self.env["user"][user]["username"], self.env["user"][user]["password"]

    def get_url(self):
        return self.env["url"]



if __name__ == '__main__':
    GetConf()

    print(GetConf().get_username_password("test001"))
    print(GetConf().get_url())
    print()
