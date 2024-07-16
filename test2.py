import pytest
from main2 import get_random_cat_image

def test_get_random_cat_image_success(mocker):
    mock_get = mocker.patch('main2.requests.get')

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{
        "id": "MTY3ODQ4OQ",
        "url": "https://cdn2.thecatapi.com/images/MTY3ODQ4OQ.jpg"
    }]

    url = get_random_cat_image()

    assert url == "https://cdn2.thecatapi.com/images/MTY3ODQ4OQ.jpg"

def test_get_random_cat_image_failure(mocker):
    mock_get = mocker.patch('main2.requests.get')

    mock_get.return_value.status_code = 404

    url = get_random_cat_image()

    assert url is None

if __name__ == "__main__":
    pytest.main()
