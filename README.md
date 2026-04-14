# SiteFence

SiteFence is a daemon that blocks distracting websites on a schedule. It works by editing the /etc/hosts file.

## Installation and usage

1. Clone the repo: 

```bash
git clone https://github.com/miguelmf/sitefence.git
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Edit/Create the sites.json file to add your desired sites and schedule. You can save the sites.json file in either the default location or in `~/.config/sitefence/`. `sites.example.json` serves as an example. You can just re-name that to `sites.json`.
4. Edit/Create the `sitefence.service` file with your path to the sitefence.py file. Just copy `sitefence.example.service` and edit the path.
5. Install the service:

```bash
sudo cp sitefence.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable sitefence
sudo systemctl start sitefence
```

If you wish to remove/stop the service:

```bash
sudo systemctl stop sitefence
sudo systemctl disable sitefence
sudo rm /etc/systemd/system/sitefence.service
sudo systemctl daemon-reload
```

## How it works

The daemon reads the sites.json file and checks if the current time is within the specified time range for each rule. If it is, it adds the urls to the /etc/hosts file. It also removed the websites from the /etc/hosts file when appropriate.

### Code structure

- `config.py`: Contains the `find_config()` and `load_config()`. Loads the sites.json file and parses it into a list of `SiteRule` objects. The config here refers to the sites.json. I may additional settings/configs in the future.
- `blocker.py`: Contains the functions for blocking (`block()`) and unblocking (`unblock()`) urls.
- `daemon.py`: Contains the main logic for the daemon. It runs, in a loop, and checks if urls should be blocked.
- `sitefence.py`: Contains the CLI commands for starting, stopping, and checking the status of the daemon. It uses [click](https://click.palletsprojects.com/en/stable/).


## Limitations

- Linux only. I have 0 interest in supporting other operating systems. I am sure they have better alternatives though. In fact, there are better alternatives for linux, most likely.
- This only blocks on the local machine. You can still skip this by picking up your smartphone. I recommend buying a dumbphone. For network-wide blocking, I suggest something like the pi-hole.
- Just one schedule-rule per day. I need to add support for multiple rules per day (soon-tm).
- Due to browser cache issues, the hosts file may not be properly followed for a minute or so. If you use firejail, it seems like you need to restart the browser.

## To Do

- Consider cron jobs instead of systemd service.
