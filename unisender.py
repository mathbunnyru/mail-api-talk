from unisender_api import make_request


def create_list(list_name: str) -> None:
    make_request("createList", {"title": list_name})


def get_list_id(list_name: str) -> int:
    lists = make_request("getLists", {})
    for list in lists:
        if list["title"] == list_name:
            return list["id"]  # type: ignore
    raise KeyError(list_name)


def subscribe(list_name: str, email: str) -> None:
    list_id = get_list_id(list_name)
    make_request("subscribe", {"list_ids": list_id, "fields[email]": email})
