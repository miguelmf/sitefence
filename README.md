# SiteFence

SiteFence is a daemon that blocks distracting websites on a schedule. It works by editing the /etc/hosts file.

## Installation and usage

1. Clone the repo.
2. Edit/Create the sites.json file to add your desired sites and schedule. You can save the sites.json file in either the default location or in `~/.config/sitefence/`. `sites.example.json` serves as an example. You can just re-name that to `sites.json`.
3. Run `sudo python3 sitefence.py start` to start the daemon. Sadly, it does need sudo.


### Dealing with sudo

You should be running this sitefence at OS startup. Since this requires sudo, you need someway to deal with this conumdrum, as you do not want to have to write a password every time OS boots up. One way of tackling this is the following:

1. Do `sudo visudo` and add the following line to the bottom of the file:

```
<username> ALL=(ALL) NOPASSWD: /usr/bin/python3 /path-to-sitefence/sitefence.py start
```
I do not like this approach, so I will be switching it to a systemd service in the future.


## How it works

The daemon reads the sites.json file and checks if the current time is within the specified time range for each rule. If it is, it adds the urls to the /etc/hosts file. It also removed the websites from the /etc/hosts file when appropriate.

### Code structure

- `config.py`: Contains the `find_config()` and `load_config()`. Loads the sites.json file and parses it into a list of `SiteRule` objects. The config here refers to the sites.json. I may additional settings/configs in the future.
- `blocker.py`: Contains the functions for blocking (`block()`) and unblocking (`unblock()`) urls.
- `daemon.py`: Contains the main logic for the daemon. It runs, in a loop, and checks if urls should be blocked.
- `sitefence.py`: Contains the CLI commands for starting, stopping, and checking the status of the daemon. It uses [click](https://click.palletsprojects.com/en/stable/).


## Limitations

- Linux only. I have 0 interest in supporting other operating systems. I am sure they have better alternatives though. In fact, there are better alternatives for linux, most likely.
- Requires sudo.
- You have have to restart the WebBrowser to re-enable the blocked sites? It seems like this is necessary on some browsers but not others, according to my tests.
- This only blocks on the local machine. You can still skip this by picking up your smartphone. I recommend buying a dumbphone.
- Just one schedule-rule per day. I need to add support for multiple rules per day (soon-tm).
- Due to browser cache issues, the hosts file may not be properly followed for a minute or so. If you use firejail, it seems like you need to restart the browser.

## TODO

- Add support for multiple rules per day.
- Switch to systemd service.
