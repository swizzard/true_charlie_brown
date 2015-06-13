with open("config") as f:
    config = {k: v for k, v in (l.split('=') for l in f)}
