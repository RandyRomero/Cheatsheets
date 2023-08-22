from time import sleep


class TooManyCalls(Exception):
    def __init__(
        self,
        timeout: float,
        message: str = "You've already made too many calls. Chill for at least {:.2} seconds",
    ):
        self.timeout = timeout
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message.format(self.timeout)


@throttle(timeout=1, attempts=2)
def say_whee():
    print("wheeee")


say_whee()
say_whee()
sleep(0.5)
say_whee()
sleep(2)
say_whee()
say_whee()
