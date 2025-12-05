from src.hnews_api import HackerNewsApis
def test_topstoriesapi_listof_ids():
      
    client=HackerNewsApis()
 
    # Call the top stories endpoint
    response=client.getting_top_stories()
    ids=response.json()
    
    # Basic response checks
    assert response.status_code==200
    assert isinstance(ids,list)
    assert len(ids)>0

    # Validate each item in the list is an integer ID
    assert all(isinstance(x,int) for x in ids )