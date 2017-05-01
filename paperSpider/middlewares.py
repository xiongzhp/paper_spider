# encoding=utf-8
import random
from user_agents import agents
import json

class UserAgentMiddleware(object):
    """ 换User-Agent """

    def process_request(self, request, spider):
        agent = random.choice(agents)
        request.headers["User-Agent"] = agent

class CookiesMiddleware(object):
    """ 换Cookie """
    cookie = {
        'rack.session':'BAh7CEkiCWNzcmYGOgZFRkkiJWViZTgyMDJiMjY0YWE2Y2U4ODgwZmE4N2Ix%0ANzE4NjcxBjsARkkiDXRyYWNraW5nBjsARnsHSSIUSFRUUF9VU0VSX0FHRU5U%0ABjsAVEkiLTc2OTRhOTVkYWU5M2NlZjBlM2FiZTAyNGU2MmU3YTE0YzdjMzhm%0AYzcGOwBGSSIZSFRUUF9BQ0NFUFRfTEFOR1VBR0UGOwBUSSItMmZjZjhlZTZm%0ANjA2MTEwNDM2ZjZlNzFkMjg2NzI4NzkyMmI3ZjhiMQY7AEZJIg9zZXNzaW9u%0AX2lkBjsAVEkiRTU4MDg1OGE0NTg0MzliYzJiYzRkYjQyNmI3NzI2MDAzZWZj%0AYmZhMTM4MjY3NTZhMzg5NmRjNzU4NTMyM2JiYmYGOwBG%0A--708454813f22a8a28949e4748cfc1274d2486ddf',
        'ajs_user_id':'null',
        'ajs_group_id':'null',
        'ajs_anonymous_id':'%2282cb594c-0350-4b9b-ad0e-bbabde64ca23%22',
        'mp_8b2ab50fd2e6ba68e73033ac10f46969_mixpanel':'%7B%22distinct_id%22%3A%20%2215bbd9eaac2349-04127adb6acb4e-39687804-fa000-15bbd9eaac33ba%22%2C%22mp_lib%22%3A%20%22Segment%3A%20web%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D',
            }
    # def process_request(self, request, spider):
    #     bs = ''
    #     for i in range(32):
    #         bs += chr(random.randint(97, 122))
    #     _cookie = json.dumps(self.cookie) % bs
    #     request.cookies = json.loads(_cookie)
