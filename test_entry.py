"""Tests for main.py: output range and determinism."""

import os
import subprocess
import sys
import tempfile
from pathlib import Path


def run_once(out_dir: str) -> str:
    env = dict(os.environ)
    env["MAKEFUN_OUTPUT_DIR"] = out_dir
    result = subprocess.run(
        [sys.executable, str(Path(__file__).parent / "main.py")],
        env=env,
        capture_output=True,
        text=True,
        check=True,
    )
    assert result.returncode == 0
    return (Path(out_dir) / "entry.txt").read_text(encoding="utf-8")


def main() -> None:
    with tempfile.TemporaryDirectory() as tmp1, tempfile.TemporaryDirectory() as tmp2:
        first = run_once(tmp1)
        second = run_once(tmp2)
        assert 1 <= len(first) <= 200, f"length out of range: {len(first)}"
        assert first == second, "output is not deterministic"
        assert first.strip(), "output is empty"
    print(f"ok: {len(first)} chars, deterministic")
    print(first)


if __name__ == "__main__":
    main()
