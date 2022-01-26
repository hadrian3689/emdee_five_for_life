import requests
import re
import hashlib

class Emdee():
    def __init__(self,url):
        self.url = url
        self.req_sites()
    def get_flag(self,post_req):
        flag = re.findall("<p align='center'>(.*)</p><center><form action=",post_req.text)
        print("The flag is: " + flag[0])

    def get_md5(self,req_site):
        string_to_encrypt = re.findall("<h3 align='center'>(.*)</h3><center><form",req_site.text)
        print("Our text to encrypt is: " + string_to_encrypt[0])

        md5_string = hashlib.md5(string_to_encrypt[0].encode()).hexdigest()
        print("The md5 hash to submit is: " + md5_string)

        return md5_string

    def req_sites(self):
        get_session = requests.Session()

        req_site = get_session.get(self.url)
        md5_string = self.get_md5(req_site)

        submit_data = {
                "hash":md5_string
                }

        post_req = get_session.post(self.url,data=submit_data)
        self.get_flag(post_req)

if __name__ == "__main__":
    url = "http://104.248.174.35:30652/" #Change IP and Port accordingly
    Emdee(url)