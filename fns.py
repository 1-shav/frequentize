import requests as rq
from datetime import datetime

class Pixela():

    def __init__(self):
        self.username = input("Enter your username :: ")
        self.token = input("Enter your token :: ")
        self.graph_id = "testual1"
        self.pixela_endpoint = "https://pixe.la/v1/users"
        self.headers = {
            "X-USER-TOKEN": self.token
        }


    def retry(self, function):
            function()


    def user_create(self):
        user_params = {
            "token": self.token,
            "username": self.username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }
        response = rq.post(url=self.pixela_endpoint, json=user_params)
        
        if response.json()["isSuccess"]:
            print(f"~USER CREATED SUCCESSFULLY~\n\tUSER WEBPAGE :: https://pixe.la/@{self.username}")
        else:
            if response.json()["message"].startswith("Please retry this request."):
                print(f"~RETRYING REQUEST~\n\tERROR MESSAGE :: {response.json()['message']}")
                self.retry(self.user_create)
            else:
                print(f"~USER CREATION FAILED~\n\tERROR MESSAGE :: {response.json()['message']}")

    
    def user_delete(self):
        response = rq.delete(url=f"{self.pixela_endpoint}/{self.username}", headers=self.headers)

        if response.json()["isSuccess"]:
            print(f"~USER DELETED SUCCESSFULLY~")
        else:
            if response.json()["message"].startswith("Please retry this request."):
                print(f"~RETRYING REQUEST~\n\tERROR MESSAGE :: {response.json()['message']}")
                self.retry(self.user_delete)
            else:
                print(f"~USER DELETION FAILED~\n\tERROR MESSAGE :: {response.json()['message']}")






if __name__ == "__main__":
    available_fns = {
        "1": "user_create",
        "2": "user_delete"
    }
    pixela = Pixela()
    print(f"~AVAILABLE FUNCTIONS~\n\t{available_fns}")
    while True:
        wanna = input("What wanna do user? :: ")
        if wanna == "exit":
            break
        elif (fnc:=available_fns.get(wanna, "null"))!="null":
            getattr(pixela, fnc)()
        else:
            print("~INVALID INPUT~")