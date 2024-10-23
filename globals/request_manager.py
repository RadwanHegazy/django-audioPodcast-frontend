import requests
from dataclasses import dataclass

@dataclass
class Action :
    url:str
    data:dict=None
    headers:dict=None
    files=None

    def post (self) :
        self.req = requests.post(self.url,data=self.data,headers=self.headers,files=self.files)
        
    def get (self) :
        self.req = requests.get(self.url,data=self.data,headers=self.headers)

    @property
    def is_valid (self) : 
        return str(self.req.status_code).startswith('2')
    
    # @property
    def json_data (self) : 
        return self.req.json()

    