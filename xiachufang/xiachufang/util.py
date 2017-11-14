import random

base_url = 'http://www.xiachufang.com'
domains = [
    'xiachufang.com',
    'www.xiachufang.com',
    'm.xiachufang.com'
]


user_agents = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'
]


def rand_ua():
    return random.choice(user_agents)
