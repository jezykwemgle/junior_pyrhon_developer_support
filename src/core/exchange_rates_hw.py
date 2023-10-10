import datetime
import json
import os

import requests
from django.http import JsonResponse
from pydantic import BaseModel, Field

API_KEY = "HDKIKI6WAC2J677G"
BASE_URL = "https://www.alphavantage.co"


class AlphavantageCurrencyExchangeRatesRequest(BaseModel):
    currency_from: str
    currency_to: str


class AlphavantageCurrencyExchangeRatesResults(BaseModel):
    currency_from: str = Field(alias="1. From_Currency Code")
    currency_to: str = Field(alias="3. To_Currency Code")
    rate: float = Field(alias="5. Exchange Rate")


class AlphavantageCurrencyExchangeRatesResponse(BaseModel):
    results: AlphavantageCurrencyExchangeRatesResults = Field(
        alias="Realtime Currency Exchange Rate"
    )


def fetch_currency_exchange_rates(
    schema: AlphavantageCurrencyExchangeRatesRequest,
) -> AlphavantageCurrencyExchangeRatesResponse:
    """This function claims the currency exchange rate information
    from the external service: Alphavantage.
    """

    payload: str = (
        "/query?function=CURRENCY_EXCHANGE_RATE&"
        f"from_currency={schema.currency_from.upper()}&"
        f"to_currency={schema.currency_to.upper()}&"
        f"apikey={API_KEY}"
    )
    url: str = "".join([BASE_URL, payload])

    raw_response: requests.Response = requests.get(url)
    response = AlphavantageCurrencyExchangeRatesResponse(**raw_response.json())

    return response


def save_history(response, time):
    if os.path.exists("history.json"):
        with open("history.json", "r") as history_file:
            history = json.load(history_file)
            history[str(time)] = response

        with open("history.json", "w") as history_file:
            json.dump(history, history_file, indent=4)
    else:
        history = {}
        with open("history.json", "w") as history_file:
            json.dump(history, history_file, indent=4)


def exchange_rate(request):  # endpoint (take request - return response)
    currency_from = request.GET.get("currency_from", "USD")
    currency_to = request.GET.get("currency_to", "UAH")
    content: AlphavantageCurrencyExchangeRatesResponse = (
        fetch_currency_exchange_rates(
            AlphavantageCurrencyExchangeRatesRequest(
                currency_from=currency_from, currency_to=currency_to
            )
        )
    )
    headers: dict = {
        "Access-Control-Allow-Origin": "*",
    }
    save_history(content.model_dump(), datetime.datetime.now())
    return JsonResponse(data=content.model_dump(), headers=headers)


def exchange_rate_history(request):
    headers: dict = {
        "Access-Control-Allow-Origin": "*",
    }
    if os.path.exists("history.json"):
        with open("history.json", "r") as file:
            data = json.load(file)
        return JsonResponse(data=data, headers=headers)
    else:
        data = {}
        return JsonResponse(data=data, headers=headers)
