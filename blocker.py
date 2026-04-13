def block(urls: list[str]):
    """Blocks a list of urls."""

    hosts_path = "/etc/hosts"

    with open(hosts_path, "r") as f:
        lines = f.read()

    with open(hosts_path, "a") as f:
        for url in urls:
            if url not in lines:
                f.write(f"127.0.0.1 {url} # SiteFence\n")

def unblock(urls: list[str]):
    """Unblocks an url."""

    hosts_path = "/etc/hosts"
    with open(hosts_path, "r") as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        if any(url in line for url in urls):
            pass
        else:
            new_lines.append(line)

    with open(hosts_path, "w") as f:
        f.writelines(new_lines)
