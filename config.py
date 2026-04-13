import json
from pathlib import Path
from dataclasses import dataclass

@dataclass
class SiteRule:
    urls: list[str]
    days: list[str]
    start: str
    end: str
    comment: str


def find_config() -> Path:
    """Finds the config file in one of two possible locations."""

    path_to_config1 = Path.home() / ".config" / "sitefence" / "sites.json"
    path_to_config2 = Path(__file__).parent / "sites.json"

    if path_to_config1.exists():
        return path_to_config1
    elif path_to_config2.exists():
        return path_to_config2
    else:
        raise FileNotFoundError("File with hosts to block (sites.json) not found.")


def load_config() -> list[SiteRule]:
    """Loads the config file."""
    path_to_config = find_config()
    with open(path_to_config) as f:
        config = json.load(f)

    rules = []
    for site in config["sites"]:
        rule = SiteRule(
            urls = site["urls"],
            days = site["time"]["days"],
            start = site["time"]["start"],
            end = site["time"]["end"],
            comment = site["comment"]
        )
        rules.append(rule)

    return rules


