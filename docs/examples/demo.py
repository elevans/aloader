import aloader
from time import sleep

def loader_test(style):
    with aloader.Loader("Loading...", "Loading...Done!", style=style):
        for i in range(15):
            sleep(0.25)

if __name__ == "__main__":
    loader_test("build")
    loader_test("rotate")
    loader_test("destroy")
    loader_test("shuffle")