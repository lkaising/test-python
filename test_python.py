#!/usr/bin/env python
# ---------------------------------------------------------------------
#  File: test-python/test_python.py
#
#  Purpose: A sanity check for Python installations and package dependencies.
#
#  Copyright (C) 2025 Logan Kaising.  All rights reserved.
# ---------------------------------------------------------------------

from __future__ import annotations

import sys
import platform
import warnings
from typing import Literal

warnings.filterwarnings("ignore")


class Colors:
    """ANSI color codes for terminal output."""

    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    END = "\033[0m"

    @classmethod
    def disable(cls) -> None:
        """Disable colors for non-TTY environments."""
        cls.BLUE = cls.CYAN = cls.GREEN = cls.YELLOW = cls.RED = cls.BOLD = cls.END = ""


if not sys.stdout.isatty():
    Colors.disable()


def print_section(title: str, *, style: Literal["header", "success"] = "header") -> None:
    """Print a section header."""
    width = 70
    border = "═" * width

    if style == "success":
        print(f"\n{Colors.GREEN}{Colors.BOLD}{border}")
        print(f"{title:^{width}}")
        print(f"{border}{Colors.END}\n")
    else:
        print(f"\n{Colors.CYAN}{Colors.BOLD}{border}")
        print(f"{title:^{width}}")
        print(f"{border}{Colors.END}")


def test_environment() -> None:
    """Display environment information."""
    print_section("ENVIRONMENT INFO")

    info = {
        "Python version": sys.version.split()[0],
        "Python executable": sys.executable,
        "Platform": platform.platform(),
        "Architecture": platform.machine(),
    }

    for key, value in info.items():
        print(f"{Colors.BOLD}{key:20s}{Colors.END} {Colors.BLUE}{value}{Colors.END}")


def test_package_versions() -> bool:
    """Test package imports and display versions."""
    print_section("PACKAGE VERSIONS")

    packages = {
        "numpy": "numpy",
        "opencv-python": "cv2",
        "scipy": "scipy",
        "scikit-image": "skimage",
        "matplotlib": "matplotlib",
        "pillow": "PIL",
    }

    for display_name, import_name in packages.items():
        try:
            module = __import__(import_name)
            version = getattr(module, "__version__", "unknown")
            checkmark = f"{Colors.GREEN}✓{Colors.END}"
            print(f"{checkmark} {display_name:20s} {Colors.YELLOW}{version}{Colors.END}")
        except ImportError:
            cross = f"{Colors.RED}✗{Colors.END}"
            print(f"{cross} {display_name:20s} {Colors.RED}NOT INSTALLED{Colors.END}")
            return False

    return True


def main() -> bool:
    """Run all verification tests."""
    try:
        test_environment()

        if not test_package_versions():
            print(f"\n{Colors.RED}{Colors.BOLD}✗ FAILED:{Colors.END} Some packages are not installed")
            return False

        print_section("ALL TESTS PASSED", style="success")
        return True

    except Exception as e:
        print(f"\n{Colors.RED}{Colors.BOLD}✗ TEST FAILED:{Colors.END} {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
