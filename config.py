with open("config") as f:
    config = {k: v for k, v in (l.rstrip().split('=') for l in f)}
