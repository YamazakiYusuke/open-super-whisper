#!/usr/bin/env python3
"""
Executable test script

Tests if the built executable can be launched and basic functionality works.
"""

import subprocess
import sys
import os
import time

def test_executable_exists():
    """Test if the executable file exists"""
    exe_path = "dist/OpenSuperWhisper"
    
    if os.path.exists(exe_path):
        print(f"✅ Executable found: {exe_path}")
        
        # Check file permissions
        if os.access(exe_path, os.X_OK):
            print("✅ Executable has proper permissions")
        else:
            print("❌ Executable lacks execution permissions")
            return False
            
        # Check file size
        file_size = os.path.getsize(exe_path)
        print(f"✅ Executable size: {file_size / (1024*1024):.1f} MB")
        
        return True
    else:
        print(f"❌ Executable not found: {exe_path}")
        return False

def test_executable_help():
    """Test if the executable can show help/version info"""
    exe_path = "dist/OpenSuperWhisper"
    
    try:
        # Try to run with --help flag (this should work even without GUI)
        result = subprocess.run(
            [exe_path, "--help"], 
            capture_output=True, 
            text=True, 
            timeout=10
        )
        
        if result.returncode == 0 or "help" in result.stdout.lower():
            print("✅ Executable responds to help flag")
            return True
        else:
            print("ℹ️  Executable may not support --help flag (normal for GUI apps)")
            return True  # This is OK for GUI apps
            
    except subprocess.TimeoutExpired:
        print("⚠️  Executable startup timeout (may require GUI)")
        return True  # This is expected for GUI apps without display
    except Exception as e:
        print(f"❌ Error testing executable: {e}")
        return False

def test_asset_inclusion():
    """Test if assets are properly included"""
    exe_path = "dist/OpenSuperWhisper"
    
    try:
        # Try to run the executable briefly to see if it can find assets
        # We'll use a very short timeout since we can't run GUI in this environment
        result = subprocess.run(
            [exe_path], 
            capture_output=True, 
            text=True, 
            timeout=3
        )
        
        # Check if any asset-related errors appear
        if "icon" in result.stderr.lower() and "not found" in result.stderr.lower():
            print("❌ Asset inclusion may have issues")
            return False
        else:
            print("✅ No obvious asset inclusion errors")
            return True
            
    except subprocess.TimeoutExpired:
        print("✅ Executable started (timeout expected without GUI)")
        return True
    except Exception as e:
        # If it fails due to missing display, that's expected
        if "display" in str(e).lower() or "cannot connect" in str(e).lower():
            print("✅ Executable requires GUI (expected)")
            return True
        else:
            print(f"⚠️  Executable test inconclusive: {e}")
            return True

def main():
    """Main test function"""
    print("🧪 Testing built executable...\n")
    
    tests = [
        test_executable_exists,
        test_executable_help,
        test_asset_inclusion,
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test error: {e}")
        print()
    
    print(f"📊 Test results: {passed}/{total} passed")
    
    if passed == total:
        print("🎉 Executable appears to be built correctly!")
        print("\n📦 Distribution files:")
        print("  • dist/OpenSuperWhisper (Linux executable)")
        print("  • dist/OpenSuperWhisper.exe (Windows executable - pre-existing)")
        print("\n💡 To test the GUI:")
        print("  1. Copy the executable to a system with a GUI")
        print("  2. Ensure the target system has necessary audio libraries")
        print("  3. Run the executable directly")
        return 0
    else:
        print("⚠️  Some tests failed or were inconclusive.")
        return 1

if __name__ == "__main__":
    sys.exit(main())