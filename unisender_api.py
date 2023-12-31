from pathlib import Path
from typing import Any

import requests

DEFAULT_LANG = "en"
BASE_URL = "https://api.unisender.com/{LANG}/api/{METHOD}"
__API_KEY = (Path.home() / ".talk" / "unisender_api_key").read_text()


def make_request(method: str, params: dict[str, Any], lang: str = DEFAULT_LANG) -> Any:
    resp = requests.post(
        BASE_URL.format(LANG=lang, METHOD=method),
        params=params,
        data={"api_key": __API_KEY},
        timeout=10,
    )
    resp.raise_for_status()
    print(resp.json())
    return resp.json()["result"]
