def pytest_configure(config):
    config.addinivalue_line("markers", "positive: positive tests")
    config.addinivalue_line("markers", "negative: negative tests")