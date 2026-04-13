# https://click.palletsprojects.com/en/stable/
import click 
from daemon import run
import os
# from daemon import stop as daemon_stop
import subprocess


@click.group()
def cli():
    """SiteFence: Block manipulative distracting websites, on a schedule. This works via the /etc/hosts file"""
    pass

@cli.command()
def start():
    """Start the sitefence daemon."""
    click.echo("Starting SiteFence...")
    run()

@cli.command()
def stop():
    """Stop the SiteFence daemon."""
    click.echo("Stopping SiteFence...")
    result = subprocess.run(["pkill", "-f", "sitefence.py start"], )
    if result.returncode == 0:
        click.echo("SiteFence stopped.")
    else:
        click.echo("SiteFence is not running.")

@cli.command()
def status():
    """Show current blocking status."""
    click.echo("Status...")

if __name__ == "__main__":
    cli()
