from main import add, app


def test_add() -> None:
	assert add(2, 3) == 5


def test_health_endpoint() -> None:
	client = app.test_client()

	response = client.get("/health")

	assert response.status_code == 200
	assert response.get_json() == {"status": "ok"}
