from service import method

@method("ping.ping")
def ping(args):
    return dict(success=True)
