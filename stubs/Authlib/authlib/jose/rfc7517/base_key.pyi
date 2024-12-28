from _typeshed import Incomplete

class Key:
    kty: str
    ALLOWED_PARAMS: Incomplete
    PRIVATE_KEY_OPS: Incomplete
    PUBLIC_KEY_OPS: Incomplete
    REQUIRED_JSON_FIELDS: Incomplete
    options: Incomplete
    def __init__(self, options: Incomplete | None = None) -> None: ...
    @property
    def tokens(self): ...
    @property
    def kid(self): ...
    def keys(self): ...
    def __getitem__(self, item): ...
    @property
    def public_only(self) -> None: ...
    def load_raw_key(self) -> None: ...
    def load_dict_key(self) -> None: ...
    def check_key_op(self, operation) -> None: ...
    def as_dict(self, is_private: bool = False, **params) -> None: ...
    def as_json(self, is_private: bool = False, **params): ...
    def thumbprint(self): ...
    @classmethod
    def check_required_fields(cls, data) -> None: ...
    @classmethod
    def validate_raw_key(cls, key) -> None: ...