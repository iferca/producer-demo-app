
import os

defaults = {
    "BROKER": "localhost",
    "CONSUMER_TOPICS": "test_topic_in",
}


def resolve_config(key: str) -> str:
    maybe_value = os.environ.get(key)
    value = maybe_value and maybe_value.split() or None
    return value or defaults.get(key)
