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
        self.graph_inited = False


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


    def graph_init(self):
        if not self.graph_inited:
            self.graph_id = input("Enter graph id :: ")
            self.graph_name = input("Enter graph name :: ")
            self.graph_unit = input("Enter graph unit :: ")
            self.graph_type = input("Enter graph type :: ")
            self.graph_color = input("Enter graph color [shibafu (green),\n \
                                    momiji (red),\n sora (blue),\n \
                                    ichou (yellow),\n ajisai (purple)\n and kuro (black)] :: ")
            self.graph_inited = True
        

    def graph_create(self):
        self.graph_init()
        graph_params = {
            "id": self.graph_id,
            "name": self.graph_name,
            "unit": self.graph_unit,
            "type": self.graph_type,
            "color": self.graph_color
        }
        response = rq.post(url=f"{self.pixela_endpoint}/{self.username}/graphs", json=graph_params, headers=self.headers)

        if response.json()["isSuccess"]:
            print(f"~GRAPH CREATED SUCCESSFULLY~\n\tGRAPH WEBPAGE :: {self.pixela_endpoint}/{self.username}/graphs/{self.graph_id}.html")
        else:
            if response.json()["message"].startswith("Please retry this request."):
                print(f"~RETRYING REQUEST~\n\tERROR MESSAGE :: {response.json()['message']}")
                self.retry(self.graph_create)
            else:
                print(f"~GRAPH CREATION FAILED~\n\tERROR MESSAGE :: {response.json()['message']}")


    def graph_get_svg(self):
        self.graph_init()
        svg_params = {
            "appearance": "dark"
        }
        response = rq.get(url=f"{self.pixela_endpoint}/{self.username}/graphs/{self.graph_id}.svg", params=svg_params)

        if response.status_code == 200:
            svg_content = response.content

            with open(f"{self.graph_id}.svg", "wb") as file:
                file.write(svg_content)
        
            print(f"~GRAPH SVG CREATED SUCCESSFULLY~\n\tGRAPH SVG FILE :: {self.graph_id}.svg")


    def graph_delete(self):
        self.graph_init()

        response = rq.delete(url=f"{self.pixela_endpoint}/{self.username}/graphs/{self.graph_id}", headers=self.headers)

        if response.json()["isSuccess"]:
            print(f"~GRAPH DELETED SUCCESSFULLY~")
        else:
            if response.json()["message"].startswith("Please retry this request."):
                print(f"~RETRYING REQUEST~\n\tERROR MESSAGE :: {response.json()['message']}")
                self.retry(self.graph_create)
            else:
                print(f"~GRAPH DELETION FAILED~\n\tERROR MESSAGE :: {response.json()['message']}")


    def graph_get_stats(self):
        response = rq.get(url=f"{self.pixela_endpoint}/{self.username}/graphs/{self.graph_id}/stats")

        if response.status_code == 200:
            print(f"~GRAPH STATS SUCCESSFULLY FOUND~\n\tGRAPH STATS :: {response.json()}")
        else:
            print(f"~GRAPH STATS NOT FOUND~\n\tERROR MESSAGE :: {response.json()['message']}")



# class Graph():

#     def __init__(self):
#         self.graph_id = input("Enter graph id :: ")
#         self.graph_name = input("Enter graph name :: ")
#         self.graph_unit = input("Enter graph unit :: ")
#         self.graph_type = input("Enter graph type :: ")
#         self.graph_color = input("Enter graph color [shibafu (green),\n momiji (red),\n sora (blue),\n ichou (yellow),\n ajisai (purple)\n and kuro (black)] :: ")


#     def graph_create(self):
#         graph_params = {
#             "id": self.graph_id,
#             "name": self.graph_name,
#             "unit": self.graph_unit,
#             "type": self.graph_type,
#             "color": self.graph_color
#         }
#         response = rq.post(url=f"{self.pixela_endpoint}/{self.username}/graphs", json=graph_params, headers=self.headers)

#         if response.json()["isSuccess"]:
#             print(f"~GRAPH CREATED SUCCESSFULLY~\n\tGRAPH WEBPAGE :: https://pixe.la/@{self.username}/graphs/{self.graph_id}")
#         else:
#             if response.json()["message"].startswith("Please retry this request."):
#                 print(f"~RETRYING REQUEST~\n\tERROR MESSAGE :: {response.json()['message']}")
#                 self.retry(self.graph_create)
#             else:
#                 print(f"~GRAPH CREATION FAILED~\n\tERROR MESSAGE :: {response.json()['message']}")










if __name__ == "__main__":
    available_fns = {
        "1": "user_create",
        "2": "user_delete",
        "3": "graph_create",
        "4": "graph_get_svg",
        "5": "graph_get_stats", 
        "6": "graph_delete"
    }
    pixela = Pixela()
    # graph = Graph()
    print(f"~AVAILABLE FUNCTIONS~\n\t{available_fns}")
    while True:
        wanna = input("What wanna do user? :: ")
        if wanna == "exit":
            break
        elif wanna in ["fns", "show fns", "available fns", "get_fns"]:
            print(f"~AVAILABLE FUNCTIONS~\n\t{available_fns}")
        elif (fnc:=available_fns.get(wanna, "null"))!="null":
            getattr(pixela, fnc)()
        else:
            print("~INVALID INPUT~")