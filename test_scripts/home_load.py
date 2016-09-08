import random
import time

import requests
from oct_turrets.base import BaseTransaction
from oct_turrets.tools import CustomTimer


class Transaction(BaseTransaction):
    def __init__(self, config):
        super(Transaction, self).__init__(config)
        self.url = config['base_url']

    def run(self):
        r = random.uniform(1, 3)
        time.sleep(r)
        with CustomTimer(self, 'home_page_load'):
            req = requests.get(self.url)
            assert req.status_code == 200
        time.sleep(r)

if __name__ == '__main__':
    trans = Transaction({"base_url": "http://localhost/wordpress/"})
    trans.run()
    print(trans.custom_timers)
