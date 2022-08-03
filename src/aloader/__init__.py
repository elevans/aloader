import time
from itertools import cycle
from shutil import get_terminal_size
from threading import Thread
from typing import List


class Loader:
    def __init__(
        self,
        start_msg="Loading...",
        end_suffix="Done!",
        animation_timeout=0.1,
        style="block-rotate",
        process_time=False,
    ):
        """Loading animation wrapper.

        A wrapper for functions that provides three different loading animations. This
        class was directly adapted from a stackoverflow post (https://stackoverflow.com/a/66558182)
        describing an easy way to create animations while a process is running.

        :param start_msg: Message to dispalay while the animation cycles.
        :param end_msg: Message to display after the animation ends.
        :param timeout: Sleep timout between animation steps.
        :param style:

            * block-rotate
                A counter clockwise rotating block.
            * block-build
                A constructing block (bottom to top).
            * block-destroy
                A deconstructing block (top to bottom).
            * block-shuffle
                A block with shuffling columns.
            * block-fall
                A block falling.
            * block-rise
                A block rising.
            * stream-down
                Streaming column of dots (top to bottom).
            * stream-up
                Streaming column of dots (bottom to top).
        """
        self.start_msg = start_msg
        self.end_suffix = start_msg + end_suffix
        self.timeout = animation_timeout
        self.process_time = process_time
        self._thread = Thread(target=self._animate, daemon=True)
        self.steps = self._get_animation(style)
        self.done = False

    def start(self):
        global start_time
        start_time = time.time()
        self._thread.start()
        return self

    def _get_animation(self, style: str) -> List[str]:
        """Return specified animation."""

        animation_styles = {
            "block-rotate": ["⠚", "⠓", "⠋", "⠙"],
            "block-build": [
                "⡀",
                "⠄",
                "⠂",
                "⠁",
                "⢁",
                "⠡",
                "⠑",
                "⠉",
                "⡉",
                "⠍",
                "⠋",
                "⢋",
                "⠫",
                "⠛",
            ],
            "block-destroy": [
                "⠛",
                "⠫",
                "⢋",
                "⠋",
                "⠍",
                "⡉",
                "⠉",
                "⠑",
                "⠡",
                "⢁",
                "⠁",
                "⠂",
                "⠄",
                "⡀",
            ],
            "block-shuffle": ["⠛", "⠞", "⡜", "⡴", "⣤", "⢦", "⢣", "⠳"],
            "block-fall": [" ", "⠉", "⠛", "⠶", "⣤", "⣀", " "],
            "block-rise": [" ", "⣀", "⣤", "⠶", "⠛", "⠉", " "],
            "stream-down": [
                " ",
                "⠁",
                "⠃",
                "⠇",
                "⡎",
                "⡜",
                "⡸",
                "⢱",
                "⢣",
                "⢇",
                "⡆",
                "⡄",
                "⡀",
                " ",
            ],
            "stream-up": [
                " ",
                "⡀",
                "⡄",
                "⡆",
                "⢇",
                "⢣",
                "⢱",
                "⡸",
                "⡜",
                "⡎",
                "⠇",
                "⠃",
                "⠁",
                " ",
            ],
        }

        if style in animation_styles:
            return animation_styles[style]
        else:
            raise KeyError(f"{style} is not available.")

    def _animate(self):
        for c in cycle(self.steps):
            if self.done:
                break
            if self.process_time:
                process_time = self._get_process_time()
                print(
                    f"\r{self.start_msg} {c} -- time elapsed: {round(process_time[0])}h {round(process_time[1])}m {round(process_time[2], 1)}s",
                    flush=True,
                    end="",
                )
            else:
                print(f"\r{self.start_msg} {c} ", flush=True, end="")
            time.sleep(self.timeout)

    def _get_process_time(self):
        """Get process time.

        :return: A time tuple.
        """
        s = round(time.time() - start_time, 1)
        h, s = s // 3600, s % 3600
        m, s = s // 60, s % 60
        return (h, m, s)

    def __enter__(self):
        self.start()

    def stop(self):
        self.done = True
        cols = get_terminal_size((80, 20)).columns
        print("\r" + " " * cols, end="", flush=True)
        process_time = self._get_process_time()
        if self.process_time:
            print(
                f"\r{self.end_suffix} -- Process completed in {round(process_time[0])}h {round(process_time[1])}m {round(process_time[2], 1)}s",
                flush=True,
            )
        else:
            print(f"\r{self.end_suffix}", flush=True)

    def __exit__(self, exc_type, exc_value, tb):
        # handle exceptions with those variables ^
        self.stop()
