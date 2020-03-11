
import os

defaults = {
    "CONSUMER_TOPICS": "spanda.poc.test.in",
}


def resolve_config(key: str) -> str:
    maybe_value = os.environ.get(key)
    value = maybe_value and maybe_value.split() or None
    return value or defaults.get(key)
