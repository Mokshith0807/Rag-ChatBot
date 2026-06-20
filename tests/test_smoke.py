def test_app_imports():
    # basic smoke test to ensure app imports without heavy deps at runtime
    import importlib

    mod = importlib.import_module("app")
    assert hasattr(mod, "st")
