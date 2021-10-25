from unittest import TestCase

from app.main import app
from fastapi.testclient import TestClient


class TestApp(TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_root_should_return_http_response_200(self):
        self.response = self.client.get("/")
        self.assertEqual(self.response.status_code, 200)

    def test_root_should_return_message_hello_world(self):
        self.response = self.client.get("/")
        self.assertEqual(self.response.json(), {"message": "Hello World"})

    def test_todo_list_size_should_be_equal_to_three(self):
        self.response = self.client.get("/a-fazer")
        self.assertEqual(len(self.response.json()), 4)

    def test_criar_novo_item_retorna_status_code_201(self):
        data = {
            "id": 2,
            "titulo": "escovar os dentes",
            "descrição": "escovar os dentes pela manhã",
            "status": "fazendo",
        }
        self.response = self.client.post("/a-fazer", json=data)
        self.assertEqual(self.response.status_code, 201)
