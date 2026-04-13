import time
from datetime import datetime
from config import SiteRule, load_config
from blocker import block, unblock
from pathlib import Path
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

        for rule in rules:
            if should_block(rule):
                block(rule.urls)
            else:
                unblock(rule.urls)

        time.sleep(300)

def should_block(rule: SiteRule) -> bool:
    """Checks if a rule should be blocked."""

    current_day = datetime.now().strftime("%A").lower()
    current_time = datetime.now().strftime("%H:%M")

    if current_day in rule.days:
        if current_time >= rule.start and current_time <= rule.end:
            # print("----1")
            # print(f"Blocking {rule.urls} on {current_day} at {current_time}.")
            # print("----1")
            return True
        else:
            # print("----2")
            # print(f"Not blocking {rule.urls} on {current_day} at {current_time}.")
            # print("----2")
            return False
    else:
        # print("----3")
        # print(f"Not blocking {rule.urls} on {current_day} at {current_time}.")
        # print("----3")
        return False


