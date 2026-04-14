 """Lab 18.3 - API Integration: Connecting to External Services with Error Handling.

Single-file version containing all five tasks:
1. Public Transport Route Fare API
2. Currency Exchange Rates
3. GitHub Repository Info Fetcher
4. News Headlines Aggregator
5. COVID-19 Statistics API Integration
"""

from __future__ import annotations

import os
import sys
import time
from typing import Any, Dict, Iterable, Optional

try:
    import requests
except ModuleNotFoundError:
    print("Missing module: requests")
    print("Install it with: python -m pip install requests")
    print(f"Current interpreter: {sys.executable}")
    raise


class APIError(Exception):
    """Raised when an API request fails in a controlled way."""


def request_json(
    url: str,
    *,
    params: Optional[Dict[str, Any]] = None,
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 15,
    retries: int = 1,
    retry_delay: int = 2,
    accepted_statuses: Optional[set[int]] = None,
) -> Any:
    """Send a GET request and return parsed JSON with retry handling."""
    accepted = accepted_statuses or {200}
    last_error: Optional[Exception] = None

    for attempt in range(retries + 1):
        try:
            response = requests.get(url, params=params, headers=headers, timeout=timeout)
        except requests.exceptions.Timeout:
            last_error = APIError("The request timed out. Please try again later.")
        except requests.exceptions.RequestException as exc:
            last_error = APIError(f"Network error: {exc}")
        else:
            if response.status_code in accepted:
                try:
                    return response.json()
                except ValueError as exc:
                    raise APIError("The API returned invalid JSON.") from exc

            if response.status_code == 429:
                retry_after = response.headers.get("Retry-After")
                wait_seconds = int(retry_after) if retry_after and retry_after.isdigit() else retry_delay
                last_error = APIError(
                    f"Rate limit exceeded. Retry after approximately {wait_seconds} seconds."
                )
                if attempt < retries:
                    time.sleep(wait_seconds)
                    continue
                raise last_error

            if response.status_code == 404:
                last_error = APIError("Requested resource was not found.")
            elif response.status_code == 401:
                last_error = APIError("Unauthorized request. Check the API key or token.")
            elif 500 <= response.status_code < 600:
                last_error = APIError(
                    f"Server error {response.status_code}. The external service may be down."
                )
            else:
                last_error = APIError(f"Unexpected API response: HTTP {response.status_code}.")

        if attempt < retries:
            time.sleep(retry_delay)

    if last_error is None:
        raise APIError("The request failed for an unknown reason.")
    raise last_error


def print_divider(title: str) -> None:
    print(f"\n{'=' * 12} {title} {'=' * 12}")


def task1_public_transport() -> None:
    """Task 1 - Public Transport Route Fare API."""
    stations_url = "https://subwayinfo.nyc/api/stations"
    trip_url = "https://subwayinfo.nyc/api/trip"
    base_fare = 2.90

    def resolve_station(station_name: str) -> Dict[str, Any]:
        payload = request_json(
            stations_url,
            params={"query": station_name, "limit": 10},
            timeout=15,
            retries=1,
        )
        if not isinstance(payload, list) or not payload:
            raise APIError(f"Invalid station name: {station_name}")

        exact_match = next(
            (item for item in payload if item["name"].lower() == station_name.lower()),
            None,
        )
        return exact_match or payload[0]

    print("Task 1 - Public Transport Route Fare API")
    source = input("Enter source station: ").strip()
    destination = input("Enter destination station: ").strip()

    try:
        if not source or not destination:
            raise ValueError("Source and destination station names cannot be empty.")
        if source.lower() == destination.lower():
            raise ValueError("Source and destination stations must be different.")

        source_station = resolve_station(source)
        destination_station = resolve_station(destination)
        trip = request_json(
            trip_url,
            params={
                "origin_station_id": source_station["id"],
                "destination_station_id": destination_station["id"],
            },
            timeout=20,
            retries=1,
        )

        if "segments" not in trip:
            raise APIError("Trip details were not available in the API response.")

        print_divider("Transport Fare Details")
        print(f"Source Station      : {source_station['name']} ({source_station['id']})")
        print(f"Destination Station : {destination_station['name']} ({destination_station['id']})")
        print(f"Estimated Time      : {trip.get('estimatedMinutes', 'N/A')} minutes")
        print(f"Total Stops         : {trip.get('totalStops', 'N/A')}")
        print(f"Transfers           : {trip.get('numTransfers', 'N/A')}")
        print(f"Fare                : ${base_fare:.2f}")
        print("\nRoute Segments:")
        for index, segment in enumerate(trip.get("segments", []), start=1):
            print(
                f"{index}. {segment['fromStationName']} -> {segment['toStationName']} | "
                f"Line {segment['line']} | Stops: {segment['numStops']}"
            )

        print(
            "\nNote: The route is fetched live from the API, and the fare shown "
            "uses the standard NYC subway base fare."
        )
    except ValueError as exc:
        print(f"Input Error: {exc}")
    except APIError as exc:
        print(f"API Error: {exc}")


def task2_currency_exchange() -> None:
    """Task 2 - Currency Exchange Rates."""
    exchange_url = "https://api.frankfurter.dev/v1/latest"
    supported_targets = {"USD", "EUR", "GBP"}

    def validate_amount(raw_amount: str) -> float:
        try:
            amount = float(raw_amount)
        except ValueError as exc:
            raise ValueError("Amount must be a valid number.") from exc
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        return amount

    def validate_currency_codes(codes: Iterable[str]) -> list[str]:
        cleaned = [code.strip().upper() for code in codes if code.strip()]
        if not cleaned:
            raise ValueError("Please provide at least one target currency code.")
        invalid = [code for code in cleaned if code not in supported_targets]
        if invalid:
            raise ValueError(
                f"Unsupported currency code(s): {', '.join(invalid)}. "
                f"Use only: {', '.join(sorted(supported_targets))}."
            )
        return cleaned

    print("Task 2 - Currency Exchange Rates")
    raw_amount = input("Enter amount in INR: ").strip()
    raw_codes = input("Enter target currencies (default: USD, EUR, GBP): ").strip()

    try:
        amount = validate_amount(raw_amount)
        target_codes = (
            validate_currency_codes(raw_codes.split(",")) if raw_codes else ["USD", "EUR", "GBP"]
        )
        payload = request_json(
            exchange_url,
            params={"base": "INR", "symbols": ",".join(target_codes)},
            timeout=15,
            retries=1,
        )
        rates = payload.get("rates")
        if not isinstance(rates, dict):
            raise APIError("Exchange rates were missing from the API response.")

        print_divider("Currency Conversion")
        print(f"{'Base Amount (INR)':<20}{'Target Currency':<18}{'Converted Amount':<18}")
        print("-" * 56)
        for code in target_codes:
            converted = amount * float(rates[code])
            print(f"{amount:<20.2f}{code:<18}{converted:<18.4f}")
    except ValueError as exc:
        print(f"Input Error: {exc}")
    except APIError as exc:
        print(f"API Error: {exc}")


def task3_github_repo() -> None:
    """Task 3 - GitHub Repository Info Fetcher."""
    github_api_url = "https://api.github.com/repos/{owner}/{repo}"

    print("Task 3 - GitHub Repository Info Fetcher")
    repo_input = input("Enter repository (owner/repo): ").strip()

    try:
        parts = [part.strip() for part in repo_input.split("/") if part.strip()]
        if len(parts) != 2:
            raise ValueError("Enter the repository in owner/repo format, for example python/cpython.")

        owner, repo = parts
        token = os.getenv("GITHUB_TOKEN", "").strip()
        headers = {"Accept": "application/vnd.github+json"}
        if token:
            headers["Authorization"] = f"Bearer {token}"

        data = request_json(
            github_api_url.format(owner=owner, repo=repo),
            headers=headers,
            timeout=15,
            retries=1,
        )

        print_divider("GitHub Repository Details")
        print(f"Repository Name : {data.get('full_name', 'N/A')}")
        print(f"Description     : {data.get('description') or 'No description provided.'}")
        print(f"Stars           : {data.get('stargazers_count', 'N/A')}")
        print(f"Forks           : {data.get('forks_count', 'N/A')}")
        print(f"Open Issues     : {data.get('open_issues_count', 'N/A')}")
        print(f"Primary Language: {data.get('language', 'N/A')}")
        print(f"Repository URL  : {data.get('html_url', 'N/A')}")
    except ValueError as exc:
        print(f"Input Error: {exc}")
    except APIError as exc:
        message = str(exc).lower()
        if "not found" in message:
            print("API Error: Repository not found (404). Check the owner/repository name.")
        elif "rate limit" in message:
            print("API Error: GitHub rate limit exceeded. Try again later or set GITHUB_TOKEN.")
        else:
            print(f"API Error: {exc}")


def task4_news_headlines() -> None:
    """Task 4 - News Headlines Aggregator."""
    news_url = "https://newsapi.org/v2/top-headlines"
    valid_categories = {"sports", "technology", "health"}

    print("Task 4 - News Headlines Aggregator")
    category = input("Enter category (sports/technology/health): ").strip().lower()

    try:
        if category not in valid_categories:
            raise ValueError(
                f"Invalid category. Choose one of: {', '.join(sorted(valid_categories))}."
            )

        api_key = os.getenv("NEWSAPI_KEY", "").strip()
        if not api_key:
            raise APIError("Missing API key. Set the NEWSAPI_KEY environment variable.")

        payload = request_json(
            news_url,
            params={
                "category": category,
                "language": "en",
                "pageSize": 5,
                "apiKey": api_key,
            },
            timeout=15,
            retries=2,
            retry_delay=3,
        )
        if payload.get("status") != "ok":
            raise APIError(payload.get("message", "News API returned an unexpected response."))

        articles = payload.get("articles")
        if not isinstance(articles, list):
            raise APIError("Articles were missing from the API response.")

        print_divider(f"Top 5 {category.title()} Headlines")
        if not articles:
            print("No headlines were returned for this category.")
            return

        for index, article in enumerate(articles[:5], start=1):
            title = article.get("title") or "Untitled headline"
            source_name = article.get("source", {}).get("name", "Unknown source")
            print(f"{index}. {title} ({source_name})")
    except ValueError as exc:
        print(f"Input Error: {exc}")
    except APIError as exc:
        print(f"API Error: {exc}")


def task5_covid_stats() -> None:
    """Task 5 - COVID-19 Statistics API Integration."""
    covid_url = "https://disease.sh/v3/covid-19/countries/{country}"

    print("Task 5 - COVID-19 Statistics API Integration")
    country = input("Enter country name: ").strip()

    try:
        if not country:
            raise ValueError("Country name cannot be empty.")

        data = request_json(
            covid_url.format(country=country),
            params={"strict": "true"},
            timeout=15,
            retries=2,
            retry_delay=4,
        )
        required_keys = {"cases", "deaths", "recovered", "active", "country"}
        if not required_keys.issubset(data):
            raise APIError("The COVID API response did not include all expected statistics.")

        print_divider("COVID-19 Statistics")
        print(f"Country            : {data['country']}")
        print(f"Total Cases        : {data['cases']:,}")
        print(f"Total Deaths       : {data['deaths']:,}")
        print(f"Total Recovered    : {data['recovered']:,}")
        print(f"Active Cases       : {data['active']:,}")
        print(f"Today's Cases      : {data.get('todayCases', 0):,}")
        print(f"Today's Deaths     : {data.get('todayDeaths', 0):,}")
    except ValueError as exc:
        print(f"Input Error: {exc}")
    except APIError as exc:
        message = str(exc).lower()
        if "not found" in message:
            print("API Error: Invalid country name. No COVID data found.")
        else:
            print(f"API Error: {exc}")


def main() -> None:
    while True:
        print("\nLab 18.3 - API Integration")
        print("1. Public Transport Route Fare API")
        print("2. Currency Exchange Rates")
        print("3. GitHub Repository Info Fetcher")
        print("4. News Headlines Aggregator")
        print("5. COVID-19 Statistics API Integration")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            task1_public_transport()
        elif choice == "2":
            task2_currency_exchange()
        elif choice == "3":
            task3_github_repo()
        elif choice == "4":
            task4_news_headlines()
        elif choice == "5":
            task5_covid_stats()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
