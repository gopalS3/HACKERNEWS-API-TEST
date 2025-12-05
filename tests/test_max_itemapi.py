from src.hnews_api import HackerNewsApis

def test_max_itemapi_validations():
    client = HackerNewsApis()

    # step 1: get current max id
    max_response = client.getting_max_item()
    current_id = max_response.json()

    # step 2: get item details for that id
    item_response = client.getting_items(current_id)
    current_item = item_response.json()

    # basic checks
    assert max_response.status_code == 200
    assert item_response.status_code == 200

    # id should match the current ID
    assert current_item["id"] == current_id

    # required fields check
    assert "type" in current_item
    assert "time" in current_item
    assert isinstance(current_item["time"], int)

    # type-specific checks
    if current_item["type"] == "story":
        assert "title" in current_item
        assert "by" in current_item
        assert isinstance(current_item["title"], str)

    elif current_item["type"] == "comment":
        assert "parent" in current_item
        assert "by" in current_item
        assert isinstance(current_item["parent"], int)

    elif current_item["type"] == "job":
        assert "title" in current_item
        assert isinstance(current_item["title"], str)

    elif current_item["type"] == "poll":
        assert "parts" in current_item
        assert isinstance(current_item["parts"], list)

    elif current_item["type"] == "pollopt":
        assert "poll" in current_item
        assert isinstance(current_item["poll"], int)

   
    if "kids" in current_item:
        assert isinstance(current_item["kids"], list)