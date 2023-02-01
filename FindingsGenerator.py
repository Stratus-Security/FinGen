import argparse
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from time import sleep
from revChatGPT.Official import Chatbot

class Loader:
    def __init__(self, desc="Loading...", end="Done!", timeout=0.1):
        """
        A loader-like context manager

        Args:
            desc (str, optional): The loader's description. Defaults to "Loading...".
            end (str, optional): Final print. Defaults to "Done!".
            timeout (float, optional): Sleep time between prints. Defaults to 0.1.
        """
        self.desc = desc
        self.end = end
        self.timeout = timeout

        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]
        self.done = False

    def start(self):
        self._thread.start()
        return self

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            print(f"\r{self.desc} {c}", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        print(f"\r{self.end}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()

parser = argparse.ArgumentParser()
parser.add_argument(
    "-t",
    "--title",
    required=True,
    action='append',
    help="Finding Title",
)
parser.add_argument(
    "--api_key",
    type=str,
    required=True,
    help="OpenAI API key",
)
args = parser.parse_args()

chatbot = Chatbot(api_key=args.api_key)

for title in args.title:
    loader = Loader("Thinking...", "").start()
    prompt = (
        "Write me a penetration testing finding about " + title + "." 
        "It should contain a description and remediation section. "
        "It should also have a risk rating based on the likelihood and impact of exploitation."
    )
    message = chatbot.ask(prompt)
    loader.stop()
    print(message["choices"][0]["text"])
    print("")