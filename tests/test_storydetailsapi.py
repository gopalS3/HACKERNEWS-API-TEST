from src.hnews_api import HackerNewsApis

def test_storydetailsapi_details_of_first_story():
    client=HackerNewsApis()
    topstory_ids_response = client.getting_top_stories()
    topstory_ids = topstory_ids_response.json()

    # pick the current ID
    currentop_story_id = topstory_ids[0]

    # get story details
    story_response = client.getting_items(currentop_story_id)
    story = story_response.json()

    # validations
    assert story_response.status_code == 200
    assert story["id"] == currentop_story_id
    assert story["type"] == "story"
    assert "title" in story
    assert "by" in story
    assert "time" in story