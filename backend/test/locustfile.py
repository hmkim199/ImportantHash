from locust import HttpUser, between, task


class WebsiteTestUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def my_task(self):
        body = {"youtube_slug": "aL0XXc1yGPs"}  # AnL39b9vFRw
        self.client.post("/api/videos/", json=body)
