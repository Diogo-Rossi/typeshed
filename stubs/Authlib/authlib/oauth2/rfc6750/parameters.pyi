from _typeshed import Incomplete

def add_to_uri(token, uri): ...
def add_to_headers(token, headers: Incomplete | None = None): ...
def add_to_body(token, body: Incomplete | None = None): ...
def add_bearer_token(token, uri, headers, body, placement: str = "header"): ...