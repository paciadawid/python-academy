import math
from locust import HttpUser, TaskSet, task, constant
from locust import LoadTestShape



class WebsiteUser(HttpUser):
    wait_time = constant(0.5)
    host = "https://api.ipify.org"

    @task
    def get_root(self):
        self.client.get("/")



class CustomShape(LoadTestShape):
    stages = [
        {"duration": 10, "users": 1, "spawn_rate": 1},
        {"duration": 20, "users": 10, "spawn_rate": 2}
    ]


    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None