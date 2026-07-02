#!/usr/bin/env python3
"""TLS verify_ssl default behavior tests for aholo_reconstruct.py skills."""

import importlib.util
import os
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_MODULES = (
    REPO_ROOT / "skills" / "aholo-3dgs-reconstruction" / "aholo_reconstruct.py",
    REPO_ROOT / "skills" / "aholo-3dgs-reconstruction-global" / "aholo_reconstruct.py",
)


def _load_module(path: Path):
    name = f"aholo_{path.parent.name.replace('-', '_')}"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class TestSslVerifyDefault(unittest.TestCase):
    def setUp(self):
        self._saved = {
            k: os.environ.get(k)
            for k in ("AHOLO_INSECURE_SKIP_VERIFY", "AHOLO_FORCE_SSL_VERIFY")
        }
        for key in self._saved:
            os.environ.pop(key, None)

    def tearDown(self):
        for key, value in self._saved.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value

    def test_default_enables_ssl_verification(self):
        for path in SKILL_MODULES:
            with self.subTest(skill=path.parent.name):
                module = _load_module(path)
                client = module.AholoClient("test-key")
                self.assertTrue(client.verify_ssl)

    def test_insecure_skip_disables_ssl_verification(self):
        for value in ("1", "true", "yes", "on", "TRUE", " On "):
            os.environ["AHOLO_INSECURE_SKIP_VERIFY"] = value
            for path in SKILL_MODULES:
                with self.subTest(skill=path.parent.name, env=value):
                    module = _load_module(path)
                    client = module.AholoClient("test-key")
                    self.assertFalse(client.verify_ssl)

    def test_legacy_insecure_zero_still_enables_verification(self):
        os.environ["AHOLO_INSECURE_SKIP_VERIFY"] = "0"
        for path in SKILL_MODULES:
            with self.subTest(skill=path.parent.name):
                module = _load_module(path)
                client = module.AholoClient("test-key")
                self.assertTrue(client.verify_ssl)


if __name__ == "__main__":
    unittest.main()
