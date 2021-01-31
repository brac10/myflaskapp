from __future__ import print_function
import re
import pytest

from myapp import create_app


@pytest.fixture()
def app():
    app = create_app()
    app.debug = True
    return app
