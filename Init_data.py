import os
from access_otop import get_token


class InitData:
    access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2OTI0Nzc2ODQsImV4cCI6MTY5MjQ5MTQyNCwibmJmIjoxNjkyNDc3Njg0LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCazRTajBqbTRBWnJra21yRkJHUzM3SlkzaGdDTnNqRnpSd1NEZk1rQ0pjaGVwVnNXYWR1STJPaWxYbFg2TWx5M2N0T09ROXdFN01SNEV2QmNoQmN2WFUwRHJpTERoODFkd1g3QkNaZFIxVlRrendxbz0iLCJkaXNwbGF5X25hbWUiOiJSQVZJQ0hBTkRSQU4gR09QSU5BVEgiLCJvbXMiOiJLMSIsImhzbV9rZXkiOiJlM2IwNmI3NDVlZmUzZGRjNWQ3YzZjMTg3NDgxNDc0ZGIzOWM0NTg4MTZjNGZjMmIwODZhZTc0MiIsImZ5X2lkIjoiWFIzNjEwMSIsImFwcFR5cGUiOjEwMCwicG9hX2ZsYWciOiJOIn0.3F5okzNtMMs-alm3P0a-1OI7FiY0iliwYR7ZNsQMBnM"
    access_token = get_token()
    client_id = "LB65IDSEJH-100"
    log_path =os.path.join(os.path.expanduser("~"), "Downloads")
