from locust import HttpUser, between, task


class HelloWorldUser(HttpUser):
    wait_time = between(0.5, 2)
    host = "https://api.ipify.org"

    @task(4)
    def get_ip_json(self):
        params = {"format": "json"}
        self.client.get("/", params=params)

    @task(1)
    def get_ip_text(self):
        params = {"format": "text"}
        self.client.get("/", params=params)
