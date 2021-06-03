import requests
import re


class BookReviews:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.nytimes.com/svc/books/v3"

    def _validate_date(self, date_string):
        date_pattern = re.compile(r"^\d{4}-\d{2}-d{2}$")
        if re.match(date_pattern, date_string):
            return date_string
        else:
            raise Exception("Date string is not valid")

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
        offset: integer
                must be a multiple of 20
                Sets the starting point of the result set (0, 20, ...). Used to paginate
                thru books if list has more than 20. Defaults to 0. The num_results field
                indicates how many books are in the list.

        Sample response:
                        {
                "status": "OK",
                "copyright": "Copyright (c) 2019 The New York Times Company.  All Rights Reserved.",
                "num_results": 1,
                "last_modified": "2016-03-11T13:09:01-05:00",
                "results": [
                    {
                    "list_name": "Hardcover Fiction",
                    "display_name": "Hardcover Fiction",
                    "bestsellers_date": "2016-03-05",
                    "published_date": "2016-03-20",
                    "rank": 5,
                    "rank_last_week": 2,
                    "weeks_on_list": 2,
                    "asterisk": 0,
                    "dagger": 0,
                    "amazon_product_url": "http://www.amazon.com/Girls-Guide-Moving-On-Novel-ebook/dp/B00ZNE17B4?tag=thenewyorktim-20",
                    "isbns": [
                        {
                        "isbn10": "0553391925",
                        "isbn13": "9780553391923"
                        }
                    ],
                    "book_details": [
                        {
                        "title": "A GIRL'S GUIDE TO MOVING ON",
                        "description": "A mother and her daughter-in-law both leave unhappy marriages and take up with new men.",
                        "contributor": "by Debbie Macomber",
                        "author": "Debbie Macomber",
                        "contributor_note": "",
                        "price": 0,
                        "age_group": "",
                        "publisher": "Ballantine",
                        "primary_isbn13": "9780553391923",
                        "primary_isbn10": "0553391925"
                        }
                    ],
                    "reviews": [
                        {
                        "book_review_link": "",
                        "first_chapter_link": "",
                        "sunday_review_link": "",
                        "article_chapter_link": ""
                        }
                    ]
                    }
                ]
                }
        """
        slug = "/lists.json"
        url = self.base_url + slug
        params = {"api-key": self.api_key}
        if kwargs.get("list") is None:
            raise Exception("List parameter should be provided")
        params["list"] = kwargs["list"]
        if "bestsellers-date" in kwargs:
            params["bestsellers-date"] = self._validate_date(kwargs["bestsellers-date"])
        if "published-date" in kwargs:
            params["published-date"] = self._validate_date(kwargs["published-date"])

        if "offset" in kwargs:
            params["offset"] = kwargs["offset"]
        resp = requests.get(url, params=params)

        return resp.json()

    def get_overview(self, **kwargs):
        """
        Hits the /lists/overview.json

        Parameters:

        published_date: string
                        matches ^\d{4}-\d{2}-\d{2}$

                        YYYY-MM-DD

                        The best-seller list publication date. You do not have to specify the exact date the list was published. The service will search forward (into the future) for the closest publication date to the date you specify. For example, a request for lists/overview/2013-05-22 will retrieve the list that was published on 05-26.

                        If you do not include a published date, the current week's best sellers lists will be returned.

        Sample response:

            {
                "status": "OK",
                "copyright": "Copyright (c) 2019 The New York Times Company.  All Rights Reserved.",
                "num_results": 210,
                "results": {
                    "bestsellers_date": "2016-03-05",
                    "published_date": "2016-03-20",
                    "lists": [
                    {
                        "list_id": 704,
                        "list_name": "Combined Print and E-Book Fiction",
                        "display_name": "Combined Print & E-Book Fiction",
                        "updated": "WEEKLY",
                        "list_image": "http://du.ec2.nytimes.com.s3.amazonaws.com/prd/books/9780399175954.jpg",
                        "books": [
                        {
                            "age_group": "",
                            "author": "Clive Cussler and Justin Scott",
                            "contributor": "by Clive Cussler and Justin Scott",
                            "contributor_note": "",
                            "created_date": "2016-03-10 12:00:22",
                            "description": "In the ninth book in this series, set in 1906, the New York detective Isaac Bell contends with a crime boss passing as a respectable businessman and a tycoon’s plot against President Theodore Roosevelt.",
                            "price": 0,
                            "primary_isbn13": "9780698406421",
                            "primary_isbn10": "0698406427",
                            "publisher": "Putnam",
                            "rank": 1,
                            "title": "THE GANGSTER",
                            "updated_date": "2016-03-10 17:00:21"
                        }
                        ]
                    }
                    ]
                }
            }

        """
        slug = "/lists/overview.json"
        url = self.base_url + slug
        params = {"api-key": self.api_key}
        if "published_date" in kwargs:
            params["published_date"] = self._validate_date(kwargs["published_date"])
        resp = requests.get(url, params=params)
        return resp.json()

    def best_sellers_history(self, **kwargs):
        """
        Hits the /lists/best-sellers/history.json

        Parameters:

        age-group: Target age group (string)

        author: The author of the best seller. The author field does not include additional contributors.
                When searching the author field, you can specify any combination of first, middle and last names.
                When sort-by is set to author, the results will be sorted by author's first name.

        contributor: The author of the best seller, as well as other contributors such as the illustrator
                    (to search or sort by author name only, use author instead).When searching,
                    you can specify any combination of first, middle and last names of any of the contributors.
                    When sort-by is set to contributor, the results will be sorted by the first name of the first contributor listed.

        isbn: International Standard Book Number, 10 or 13 digits. A best seller may have both 10-digit and 13-digit ISBNs,
            and may have multiple ISBNs of each type. To search on multiple ISBNs, separate the ISBNs with semicolons (example: 9780446579933;0061374229).

        offset: must be a multiple of 20. Sets the starting point of the result set (0, 20, ...). Used to paginate thru results if there are more than 20.
                Defaults to 0. The num_results field indicates how many results there are total.

        price: The publisher's list price of the best seller, including decimal point

        publisher: The standardized name of the publisher

        title: The title of the best seller. When searching, you can specify a portion of a title or a full title.

        Sample response:
        {
            "status": "OK",
            "copyright": "Copyright (c) 2019 The New York Times Company.  All Rights Reserved.",
            "num_results": 28970,
            "results": [
                {
                "title": "#GIRLBOSS",
                "description": "An online fashion retailer traces her path to success.",
                "contributor": "by Sophia Amoruso",
                "author": "Sophia Amoruso",
                "contributor_note": "",
                "price": 0,
                "age_group": "",
                "publisher": "Portfolio/Penguin/Putnam",
                "isbns": [
                    {
                    "isbn10": "039916927X",
                    "isbn13": "9780399169274"
                    }
                ],
                "ranks_history": [
                    {
                    "primary_isbn10": "1591847931",
                    "primary_isbn13": "9781591847939",
                    "rank": 8,
                    "list_name": "Business Books",
                    "display_name": "Business",
                    "published_date": "2016-03-13",
                    "bestsellers_date": "2016-02-27",
                    "weeks_on_list": 0,
                    "ranks_last_week": null,
                    "asterisk": 0,
                    "dagger": 0
                    }
                ],
                "reviews": [
                    {
                    "book_review_link": "",
                    "first_chapter_link": "",
                    "sunday_review_link": "",
                    "article_chapter_link": ""
                    }
                ]
                }
            ]
            }
        """
        slug = "/lists/best-selllers/history.json"
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
        """ """
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
            raise Exception(
                "Must provide either author, title or isbn as one of the parameters"
            )
        resp = requests.get(url, params=params)
        return resp.json()
