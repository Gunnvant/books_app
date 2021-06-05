import requests
from datetime import datetime

class ListParamAbsent(Exception):
    pass

class InvalidDate(Exception):
    pass

class AtleastOneParam(Exception):
    pass

class BookReviews:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.nytimes.com/svc/books/v3"

    def _validate_date(self, date_string):
        try:
            datetime.strptime(date_string,"%Y-%m-%d")
            return date_string
        except:
            raise InvalidDate("Date string is not valid")

    def get_list_names(self):
        """
        Implements the /lists/names.json endpoint of the official api
        This can be used to get the lists hosted on the api
        """
        slug = "/lists/names.json"
        url = self.base_url + slug
        params = {"api-key": self.api_key}
        resp = requests.get(url, params=params)
        return resp.json()

    def get_list(self, **kwargs):
        """
        Implements the /lists.json endpoint of the official api. This can be used fetch data about a particular list
        obtained by hitting the /lists/names.json endpoint.

        Parameters:
        
        list: one of the values in list_name_encoded, when /lists/names.json is hit
        
        bestsellers-date: Should be in YYYY-MM-DD format
        
        published-date: Should be in YYYY-MM-DD format
        
        offset: must be a multiple of 20
                Sets the starting point of the result set (0, 20, ...). Used to paginate
                thru books if list has more than 20. Defaults to 0. The num_results field
                indicates how many books are in the list.                     
        """
        slug = "/lists.json"
        url = self.base_url + slug
        params = {"api-key": self.api_key}
        if kwargs.get("list") is None:
            raise ListParamAbsent("List parameter should be provided")
        params["list"] = kwargs["list"]
        if "bestsellers_date" in kwargs:
            params["bestsellers-date"] = self._validate_date(kwargs["bestsellers_date"])
        if "published_date" in kwargs:
            params["published-date"] = self._validate_date(kwargs["published_date"])

        if "offset" in kwargs:
            params["offset"] = kwargs["offset"]
        resp = requests.get(url, params=params)

        return resp.json()

    def get_overview(self, **kwargs):
        """
        Hits the /lists/overview.json

        Parameters:

        published_date:  YYYY-MM-DD
                        The best-seller list publication date. You do not have to specify the exact date the list was published. 
                        The service will search forward (into the future) for the closest publication date to the date you specify. 
                        For example, a request for lists/overview/2013-05-22 will retrieve the list that was published on 05-26.
                        If you do not include a published date, the current week's best sellers lists will be returned.

        """
        slug = "/lists/overview.json"
        url = self.base_url + slug
        params = {"api-key": self.api_key}
        if "published_date" in kwargs:
            params["published-date"] = self._validate_date(kwargs["published_date"])
        resp = requests.get(url, params=params)
        return resp.json()

    def best_sellers_history(self, **kwargs):
        """
        Hits the /lists/best-sellers/history.json

        Parameters:

        age-group: Target age group (string)

        author: The author of the best seller. 
                The author field does not include additional contributors.
                When searching the author field, you can specify any combination of first, middle and last names.
                When sort-by is set to author, the results will be sorted by author's first name.

        contributor: The author of the best seller, as well as other contributors such as the illustrator
                    (to search or sort by author name only, use author instead).
                    When searching, you can specify any combination of first, middle and last names of any of the contributors.
                    When sort-by is set to contributor, the results will be sorted by the first name of the first contributor listed.

        isbn: International Standard Book Number, 10 or 13 digits. 
              A best seller may have both 10-digit and 13-digit ISBNs, and may have multiple ISBNs of each type. 
              To search on multiple ISBNs, separate the ISBNs with semicolons (example: 9780446579933;0061374229).

        offset: must be a multiple of 20. 
                Sets the starting point of the result set (0, 20, ...). 
                Used to paginate thru results if there are more than 20.
                Defaults to 0. The num_results field indicates how many results there are total.

        price: The publisher's list price of the best seller, including decimal point

        publisher: The standardized name of the publisher

        title: The title of the best seller. 
               When searching, you can specify a portion of a title or a full title.

        """
        slug = "/lists/best-sellers/history.json"
        url = self.base_url + slug
        params = {"api-key": self.api_key}
        options = [
            "age-group",
            "author",
            "contributor",
            "isbn",
            "offset",
            "price",
            "publisher",
            "title",
        ]
        for option in options:
            if option in kwargs:
                params[option] = kwargs[option]
        resp = requests.get(url, params=params)
        return resp.json()

    def get_reviews(self, **kwargs):
        """ 
        Hits /reviews.json endpoint

        Parameters:

        isbn: ISBN number
        title: Book title
        author: Author name
        """
        slug = "/reviews.json"
        url = self.base_url + slug
        params = {"api-key": self.api_key}
        options = ["isbn", "title", "author"]
        cnt = 0
        for option in options:
            if option in kwargs:
                cnt += 1
                params[option] = kwargs[option]
        if cnt == 0:
            raise AtleastOneParam(
                "Must provide either author, title or isbn as one of the parameters"
            )
        resp = requests.get(url, params=params)
        return resp.json()
