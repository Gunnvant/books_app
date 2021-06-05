import sys 
import os 
import pytest 

path_app = os.path.join(os.getcwd(),"../")
sys.path.append(path_app)

from app import create_app 

@pytest.fixture
def client():
    '''
    Guidance on creating contexts and fixtures
    for a Flask app can be found here:
    https://stackoverflow.com/questions/17375340/testing-code-that-requires-a-flask-app-or-request-context
    '''
    app = create_app()
    with app.test_client() as client:
        with app.app_context():
            yield client


def test_healthy_endpoint(client):
    '''
    Get the application going
    test if the server is alive
    '''
    resp = client.get("/apiv1/status")
    assert resp.status_code == 200

def test_get_list_names(client):
    '''
    Test the list_names endpoint
    '''
    response = client.get("/apiv1/listnames")
    assert response.status_code == 200
    assert response.json['success'] == True

## Todo find a way to test 500 response

def test_list(client):
    '''
    Tests the response when a listname 
    is passed
    '''
    response = client.get("/apiv1/lists",query_string={'list': 'combined-print-and-e-book-fiction'})
    assert response.status_code == 200
    assert response.json['success'] == True 

def test_list_good_parameters(client):
    '''
    Tests the response with valid query parameters
    '''
    query_string = {'list': 'combined-print-and-e-book-fiction',
                    "bestsellers_date":"2016-04-25",
                    "published_date":"2014-04-26"}
    response = client.get("/apiv1/lists",query_string=query_string)
    assert response.status_code == 200

def test_list_no_list_name(client):
    '''
    Don't pass the list query parameter
    '''
    response = client.get("/apiv1/lists")
    assert response.status_code == 404

def test_list_bad_date(client):
    '''
    Pass malformed date
    '''
    query_string = {"bestsellers_date":"25-05-1989"}
    response =  client.get("/apiv1/lists",query_string=query_string)
    assert response.status_code == 404


def test_overview(client):
    '''
    Test the overview endpoint
    '''
    response = client.get("/apiv1/overview")
    assert response.status_code == 200 

def test_overview_good_date(client):
    '''
    Test with properly formatted date
    '''
    query_string = {"published_date":"2016-05-26"}
    response = client.get("/apiv1/overview",query_string=query_string)
    assert response.status_code == 200

def test_overview_bad_date(client):
    '''
    Test with malformed date
    '''
    query_string = {"published_date":"26-05-2016"}
    response = client.get("/apiv1/overview",query_string=query_string)
    assert response.status_code == 404

def test_history(client):
    '''
    Simple test on success
    '''
    response = client.get("/apiv1/history")
    assert response.status_code == 200

def test_reviews(client):
    '''
    Send atleast one query parameter
    '''
    query_string = {"title":'Alice in wonderland'}
    response = client.get("/apiv1/reviews",query_string=query_string)
    assert response.status_code == 200

def test_reviews_no_parameter(client):
    '''
    Send no query parameter, test for failure
    '''
    response = client.get("/apiv1/reviews")
    assert response.status_code == 404