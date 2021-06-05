import pytest
import sys
import os
import json 

package_path = os.path.join(os.getcwd(),"../")
sys.path.append(package_path)
from app.views.utils import BookReviews, ListParamAbsent, InvalidDate, AtleastOneParam

@pytest.fixture
def bkr():
    config = open("../config.json","r",encoding="utf-8").read()
    config = json.loads(config)
    api_key = config['api_key']
    bkr = BookReviews(api_key=api_key)
    return bkr

def test_list_names(bkr):
    list_names = bkr.get_list_names()
    assert list_names['status'] == "OK"
    assert list_names['num_results']>0

def test_get_list(bkr):
    list_name = bkr.get_list(list="combined-print-and-e-book-fiction")
    assert list_name['status'] == 'OK'
    assert list_name['num_results']>0

def test_get_list_exception_no_list_name(bkr):
    with pytest.raises(ListParamAbsent):
        bkr.get_list(lst = "combined-print-and-e-book-fiction")

def test_get_list_exception_invalid_bestseller_date(bkr):
    with pytest.raises(InvalidDate):
        bkr.get_list(list="combined-print-and-e-book-fiction",bestsellers_date="26-05-1989")

def test_get_list_exception_invalid_published_date(bkr):
    with pytest.raises(InvalidDate):
        bkr.get_list(list="combined-print-and-e-book-fiction",published_date="26-05-1989")

def test_get_overview(bkr):
    overview = bkr.get_overview()
    assert overview['status'] == "OK"
    assert "results" in overview
    assert overview["num_results"]>0

def test_get_overview_bad_date_exception(bkr):
    with pytest.raises(InvalidDate):
        bkr.get_overview(published_date="26-05-1989")

def test_get_overview_good_date(bkr):
    overview = bkr.get_overview(published_date = "2016-03-05")
    assert overview['status'] == "OK"
    assert "results" in overview
    assert overview["num_results"]>0

def test_get_reviews(bkr):
    reviews = bkr.get_reviews(author = "John Grisham")
    assert reviews['status'] == "OK"
    assert reviews['num_results']>0
    assert "results" in reviews

def test_get_reviews_exception(bkr):
    with pytest.raises(AtleastOneParam):
        bkr.get_reviews()