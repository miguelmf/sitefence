import time
from datetime import datetime
from config import SiteRule, load_config
from blocker import block, unblock
import os, sys
import click

def run():
    """Runs the SiteFence daemon."""

    pid = os.fork()
    if pid > 0:
        click.echo("SiteFence started in run().")
        sys.exit(0)
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

    if current_day in rule.days:
        if current_time >= rule.start and current_time <= rule.end:
            return True
        else:
            return False
    else:
        return False


