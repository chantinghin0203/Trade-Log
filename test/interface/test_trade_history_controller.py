from fastapi.testclient import TestClient

from server import app

test_client = TestClient(app)


def test_get_xrp_usdt_log():
    response = test_client.get("/api/v1/xrp-usdt?start_time=1582509911141&end_time=1582509911141")
    assert response.status_code == 200
    assert response.json() == [{"timestamp": 1582509911141, "price": 0.2812, "quantity": 57.164, "side": 1}]
