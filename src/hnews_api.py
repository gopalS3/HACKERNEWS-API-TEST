import requests

#common prefix for all api end points before using it
Bottom_URL="https://hacker-news.firebaseio.com/v0"

class HackerNewsApis:
    # Store the base URL so it can be reused for other API calls
    def __init__(self, bottom_url:str=Bottom_URL):
        self.bottom_url=bottom_url

        """
        Fetches the list of top story IDs from the /topstories endpoint.
        Returns the raw response object.
        """
    def getting_top_stories(self):
        Stories_url=f"{self.bottom_url}/topstories.json"
        return requests.get(Stories_url)
    
        """
        Retrieves the full details for a given item ID (story, comment, job, etc.).
        The API returns a JSON object describing the item.
        """
        
    def getting_items(self,item_number:int):
        items_url=f"{self.bottom_url}/item/{item_number}.json"
        return requests.get(items_url)
    
        """
        Gets the maximum item ID created on HackerNews.
        
        """
    def getting_max_item(self):
        maxurl = f"{self.bottom_url}/maxitem.json"
        return requests.get(maxurl)
