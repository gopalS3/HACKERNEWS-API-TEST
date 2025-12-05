from src.hnews_api import HackerNewsApis
import pytest
def test_current_item_commentapi():
    client = HackerNewsApis()

    # get current max item id
    max_response = client.getting_max_item()
    current_id = max_response.json()

    # get the details for this item
    comment_response = client.getting_items(current_id)
    comment = comment_response.json()

    # if current item is not a comment, skip this test
    if comment["type"] != "comment":
        pytest.skip(f"Current item is type '{comment['type']}', not a comment")

    # if it IS a comment, validate everything
    assert comment_response.status_code == 200
    assert comment["id"] == current_id
    assert "parent" in comment
    assert isinstance(comment["parent"], int)
    assert "time" in comment
    assert "by" in comment

    # now validate the parent exists
    parent_response = client.getting_items(comment["parent"])
    assert parent_response.status_code == 200

def test_first_commentapi_validations():
    client = HackerNewsApis()

    # get top stories
    top_ids_response = client.getting_top_stories()
    top_ids = top_ids_response.json()

    # pick first story id
    first_story_id = top_ids[0]

    # get story details
    story_response = client.getting_items(first_story_id)
    story = story_response.json()

    if "type" not in story:
        pytest.skip("Current item missing 'type' field")

    # if story has no comments, skip
    if "kids" not in story:
        pytest.skip("Story has no comments to validate")

    # get first comment id
    first_comment_id = story["kids"][0]

    # get comment details
    comment_response = client.getting_items(first_comment_id)
    comment = comment_response.json()

    # validations
    assert comment_response.status_code == 200
    assert comment["id"] == first_comment_id
    assert comment["type"] == "comment"
    assert comment["parent"] == first_story_id
    assert "time" in comment
    assert "by" in comment
    assert isinstance(comment["parent"], int)
    