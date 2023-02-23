import math
from locust import HttpUser, TaskSet, task, constant
from locust import LoadTestShape
import random

class UserTasks(TaskSet):
    @task
    def get_root(self):
        self.client.get("/")


class WebsiteUser(HttpUser):
    wait_time = constant(0.5)
    tasks = [UserTasks]


class DoubleWave(LoadTestShape):
    """
    A shape to imitate some specific user behaviour. In this example, midday
    and evening meal times. First peak of users appear at time_limit/3 and
    second peak appears at 2*time_limit/3
    Settings:
        min_users -- minimum users
        peak_one_users -- users in first peak
        peak_two_users -- users in second peak
        time_limit -- total length of test
    """

    stages = [
        {"duration": 6, "users": 10, "spawn_rate": 10},
        {"duration": 10, "users": 50, "spawn_rate": 10},
        {"duration": 18, "users": 100, "spawn_rate": 10},
        {"duration": 22, "users": 30, "spawn_rate": 10},
        {"duration": 30, "users": 10, "spawn_rate": 10},
        {"duration": 40, "users": 1, "spawn_rate": 1},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None