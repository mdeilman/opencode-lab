import hashlib
import io
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

import sha256_file


class HashFileTests(unittest.TestCase):
    def test_known_and_empty_contents(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "datei"
            for content, expected in (
                (b"abc", "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"),
                (b"", "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"),
            ):
                with self.subTest(content=content):
                    path.write_bytes(content)
                    self.assertEqual(sha256_file.hash_file(path), expected)

    def test_multiple_bounded_reads(self):
        content = b"\x00\xffabc" * (sha256_file.BLOCK_SIZE // 2)

        class RecordingFile(io.BytesIO):
            def __init__(self, data):
                super().__init__(data)
                self.read_sizes = []

            def read(self, size=-1):
                self.read_sizes.append(size)
                return super().read(size)

        stream = RecordingFile(content)
        with patch("builtins.open", return_value=stream) as open_file:
            result = sha256_file.hash_file("datei")
        open_file.assert_called_once_with("datei", "rb")
        self.assertEqual(result, hashlib.sha256(content).hexdigest())
        self.assertGreater(len(stream.read_sizes), 2)
        self.assertTrue(all(size == sha256_file.BLOCK_SIZE for size in stream.read_sizes))


class CommandLineTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(Path(sha256_file.__file__).resolve()), *args],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_success(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "datei mit leerzeichen"
            path.write_bytes(b"abc")
            result = self.run_cli(str(path))
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad\n")
        self.assertEqual(result.stderr, "")

    def test_invalid_arguments(self):
        for args in ((), ("eins", "zwei")):
            with self.subTest(args=args):
                result = self.run_cli(*args)
                self.assertNotEqual(result.returncode, 0)
                self.assertEqual(result.stdout, "")
                self.assertIn("usage:", result.stderr)

    def test_missing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = str(Path(directory) / "fehlt")
            result = self.run_cli(path)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "")
        self.assertIn(path, result.stderr)
        self.assertIn("Fehler", result.stderr)

    def test_open_and_read_errors(self):
        class FailingRead(io.BytesIO):
            def read(self, size=-1):
                raise OSError("Lesefehler")

        for failure in (PermissionError("Zugriff verweigert"), FailingRead(b"abc")):
            with self.subTest(failure=failure):
                stdout, stderr = io.StringIO(), io.StringIO()
                if isinstance(failure, OSError):
                    open_patch = patch("builtins.open", side_effect=failure)
                else:
                    open_patch = patch("builtins.open", return_value=failure)
                with open_patch, redirect_stdout(stdout), redirect_stderr(stderr):
                    status = sha256_file.main(["datei"])
                self.assertNotEqual(status, 0)
                self.assertEqual(stdout.getvalue(), "")
                self.assertIn("datei", stderr.getvalue())
                self.assertIn("Fehler", stderr.getvalue())
