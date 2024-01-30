from locust import HttpUser, between, task
import random

class myUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://localhost"

    @task
    def myTask(self):
        n = random.randint(1, 10)
        k = random.randint(1, 10)
        self.client.get("/api/", params={"n": n, "k": k})