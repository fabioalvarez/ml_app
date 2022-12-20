from locust import User, HttpUser, task, between, constant


class APIUser(HttpUser):
    wait_time = between(1,5)

    # Put your stress tests here.
    # See https://docs.locust.io/en/stable/writing-a-locustfile.html for help.
    # TODO

    @task
    def test_index(self):
        print("Testing index")
        self.client.get("/")

    @task(2)
    def test_predict(self):
        print("Testing Predict")
        with open("dog.jpeg", "rb") as image:
            self.client.post("/predict", files={"file":image})