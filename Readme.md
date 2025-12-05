**HackerNews API Acceptance Tests**

This project contains a small collection of acceptance tests written against the public Hacker News API. The goal was to automate a few real user flows using the /topstories and /item endpoints, and validate that the API behaves as expected when retrieving the current top story and its first comment.

All tests are written in Python, using requests for HTTP calls and pytest as the test runner.

**What the Tests Cover**
1. Retrieving Top Stories

Calls the /topstories endpoint

Confirms the API returns a successful response

Verifies that the payload is a non-empty list of integer IDs

2. Getting Details of the Current Top Story

Takes the first ID from the top stories list

Retrieves the story details using /item/{id}

Checks for required fields such as id, type, title, time, and by

Ensures the item is classified as a "story"

3. Retrieving the First Comment on the Top Story

Uses the same top story and checks whether it has any comments (kids)

If comments exist, fetches the first comment

Validates that the returned item is a "comment"

Ensures the comment belongs to the correct story via its parent field

Checks for typical comment fields (by, time, etc.)

**Bonus: Exploring /maxitem**

I also included an extra test around the /maxitem endpoint to explore API behavior for the latest created item. This wasn’t required, but it helped me understand the API a bit more.
The test is only validated when the latest item happens to be a comment.

# Project Structure
hackernews-api-test/
│
├── src/
│   └── hnews_api.py        # simple wrapper around the API endpoints
│
├── tests/
│   ├── test_topstoriesapi.py
│   ├── test_storydetailsapi.py
│   ├── test_first_commentapi.py
│   └── test_current_itemapi.py   # optional exploratory test
│
├── requirements.txt
└── README.md
$$

Setup Instructions
$$
1. Create a Virtual Environment
python -m venv venv

2. Activate It (Windows)
venv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt
****
Running the Tests****

To run all tests:

pytest -v


To generate a simple HTML test report:

pytest --html=report.html --self-contained-html

Notes

Hacker News data changes constantly, so the tests skip cases where the top story has no comments or when certain fields are missing.

The goal of the project is to validate realistic flows, not to enforce strict schemas on every item type.

The /maxitem test was added only as an exploratory step and is not part of the required acceptance criteria.