import os

ENV = os.getenv("ENV", "QA")

ENVIRONMENTS = {
    "QA": {
        "UI_BASE_URL": "https://the-internet.herokuapp.com",
        "API_BASE_URL": "https://reqres.in/api"
    },
    "UAT": {
        "UI_BASE_URL": "https://the-internet.herokuapp.com",
        "API_BASE_URL": "https://reqres.in/api"
    }
}

UI_BASE_URL = ENVIRONMENTS[ENV]["UI_BASE_URL"]
API_BASE_URL = ENVIRONMENTS[ENV]["API_BASE_URL"]