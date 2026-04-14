import time
from datetime import datetime
from config import SiteRule, load_config
from blocker import block, unblock

def run():
    """Runs the SiteFence daemon."""

    while True:
        rules = load_config()
        urls_to_block = []
        urls_to_unblock = []
        for rule in rules:
            if should_block(rule):
                urls_to_block.extend(rule.urls)
            else:
                urls_to_unblock.extend(rule.urls)
        if urls_to_block:
            block(urls_to_block)
        if urls_to_unblock:
            unblock(urls_to_unblock)

        time.sleep(300)

def should_block(rule: SiteRule) -> bool:
    """Checks if a rule should be blocked."""
    current_day = datetime.now().strftime("%A").lower()
    current_time = datetime.now().strftime("%H:%M")
    for schedule in rule.schedules:
        if current_day in schedule.days:
            if current_time >= schedule.start and current_time <= schedule.end:
                return True
    return False

