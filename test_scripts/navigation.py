import time

from selenium import webdriver
from oct_turrets.base import BaseTransaction


class Transaction(BaseTransaction):

    def __init__(self, config):
        super(Transaction, self).__init__(config)
        self.base_url = config['base_url']
        self.user = config['user']
        self.pwd = config['pwd']
        self.driver = None

    def setup(self):
        self.driver = webdriver.Firefox()

    def run(self):
        self.driver.get(self.base_url)
        time.sleep(1)
        link = self.driver.find_element_by_css_selector('h2.entry-title > a')
        if link:
            link.click()
        assert("Bonjour" in self.driver.title)
        time.sleep(2)
        search = self.driver.find_element_by_css_selector('.search-field')
        search.send_keys("bonjour")
        time.sleep(2)
        self.driver.find_element_by_css_selector(".search-submit").click()
        time.sleep(1)
        assert("Bonjour tout le monde" in self.driver.page_source)
        time.sleep(1)
        self.driver.get(self.base_url + "/wp-login.php")
        login = self.driver.find_element_by_id("user_login")
        pwd = self.driver.find_element_by_id("user_pass")
        login.send_keys(self.user)
        pwd.send_keys(self.pwd)
        self.driver.find_element_by_id("wp-submit").click()
        time.sleep(2)

    def tear_down(self):
        self.driver.close()


if __name__ == "__main__":
    trans = Transaction({
        "base_url": "http://localhost/wordpress",
        "user": "root",
        "pwd": "root"
    })
    trans.setup()
    trans.run()
    trans.tear_down()
