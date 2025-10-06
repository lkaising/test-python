#!/usr/bin/env python
"""Test script to verify Python environment and package installations."""

import sys
import platform
import warnings
warnings.filterwarnings('ignore')


def print_section(title):
    """Print formatted section header."""
    print("\n" + "=" * 70)
    print(title.center(70))
    print("=" * 70)


def test_environment():
    """Display environment information."""
    print_section("ENVIRONMENT INFO")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Python executable: {sys.executable}")
    print(f"Platform: {platform.platform()}")
    print(f"Architecture: {platform.machine()}")


def test_package_versions():
    """Test package imports and display versions."""
    print_section("PACKAGE VERSIONS")
    
    packages = {
        'numpy': 'numpy',
        'opencv-python': 'cv2',
        'scipy': 'scipy',
        'scikit-image': 'skimage',
        'matplotlib': 'matplotlib',
        'pillow': 'PIL'
    }
    
    for display_name, import_name in packages.items():
        try:
            module = __import__(import_name)
            version = getattr(module, '__version__', 'unknown')
            print(f"✓ {display_name:20s} {version}")
        except ImportError as e:
            print(f"✗ {display_name:20s} NOT INSTALLED")
            return False
    return True


def main():
    """Run all tests."""
    try:
        test_environment()
        
        if not test_package_versions():
            print("\n✗ FAILED: Some packages are not installed")
            return False
        
        print_section("ALL TESTS PASSED")
        return True
        
    except Exception as e:
        print(f"\n✗ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
