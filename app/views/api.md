### Docs for the python wrapper of nyt books api

The main class is `BookReviews()`. Below is the signature and expected response

```python
get_list_names()
```
Implements the /lists/names.json endpoint of the official api. This can be used to get the lists hosted on the api.

Sample Response:

```json

{
  "status": "OK",
  "copyright": "Copyright (c) 2019 The New York Times Company.  All Rights Reserved.",
  "num_results": 53,
  "results": [
    {
      "list_name": "Combined Print and E-Book Fiction",
      "display_name": "Combined Print & E-Book Fiction",
      "list_name_encoded": "combined-print-and-e-book-fiction",
      "oldest_published_date": "2011-02-13",
      "newest_published_date": "2016-03-20",
      "updated": "WEEKLY"
    }
  ]
}

```

```python
get_list()
```
Implements the /lists.json endpoint of the official api. This can be used fetch data about a particular list obtained by hitting the /lists/names.json endpoint.

Sample Response

```json
  
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

```

```python
get_overview()
```

Hits the /lists/overview.json

Sample Response

```json
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
```

```python
    best_sellers_history()
```
Hits the /lists/best-sellers/history.json

Sample Response

```json
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
```

```python
  get_reviews()
```

Hits /reviews.json endpoint

Sample response 

```json
{
  "status": "OK",
  "copyright": "Copyright (c) 2019 The New York Times Company.  All Rights Reserved.",
  "num_results": 2,
  "results": [
    {
      "url": "http://www.nytimes.com/2011/11/10/books/1q84-by-haruki-murakami-review.html",
      "publication_dt": "2011-11-10",
      "byline": "JANET MASLIN",
      "book_title": "1Q84",
      "book_author": "Haruki Murakami",
      "summary": "In “1Q84,” the Japanese novelist Haruki Murakami writes about characters in a Tokyo with two moons.",
      "isbn13": [
        "9780307476463"
      ]
    }
  ]
}
```