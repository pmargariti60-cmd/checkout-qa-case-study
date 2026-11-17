from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--build", choices=("reference", "candidate"), default="reference"
    )


@pytest.fixture(scope="session")
def demo_url():
    demo = Path(__file__).resolve().parents[1] / "demo"
    handler = partial(SimpleHTTPRequestHandler, directory=str(demo))
    with ThreadingHTTPServer(("127.0.0.1", 0), handler) as server:
        worker = Thread(target=server.serve_forever, daemon=True)
        worker.start()
        try:
            yield f"http://127.0.0.1:{server.server_port}"
        finally:
            server.shutdown()
            worker.join()


@pytest.fixture
def checkout(page, demo_url, pytestconfig):
    build = pytestconfig.getoption("--build")
    page.goto(f"{demo_url}/?build={build}")
    return page
