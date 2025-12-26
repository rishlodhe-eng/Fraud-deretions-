from locust import HttpUser, task, between

class User(HttpUser):
    wait_time = between(1, 2)

    @task
    def test_api(self):
        self.client.post("/transactions/validate", json={
            "transaction_id": "TXN001",
            "amount": 100
        })
