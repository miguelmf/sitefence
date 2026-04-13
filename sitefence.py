# https://click.palletsprojects.com/en/stable/
import click 
from daemon import run

@click.group()
def cli():
    """SiteFence: Block manipulative distracting websites, on a schedule. This works via the /etc/hosts file"""
    pass

@cli.command()
def start():
    """Start the sitefence daemon."""
    click.echo("To start SiteFence as a service, run: sudo systemctl start sitefence")
    click.echo("This is starting it manually (not recommended): running daemon now...")
    run()

@cli.command()
def stop():
    """Stop the SiteFence daemon."""
    click.echo("To stop SiteFence, run: sudo systemctl stop sitefence")

@cli.command()
def status():
    """Show current blocking status."""

    with open("/etc/hosts", "r") as f:
        all_lines = f.readlines()

    lines = []
    for line in all_lines:
        if "SiteFence" in line:
            lines.append(line)

    if lines:
        click.echo("Currently blocked with SiteFence:")
        for line in lines:
            click.echo(f"  {line.strip()}")
    else:
        click.echo("No sites currently blocked.")

if __name__ == "__main__":
    cli()
