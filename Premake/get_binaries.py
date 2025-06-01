import os
import platform
import sys
from dataclasses import dataclass

@dataclass
class PlatformModel:
    platform_name: str
    opt_file_extension: str|None

platform_model_mappings = {
    "Windows": PlatformModel("Windows", ".exe"),
    "Linux": PlatformModel("Linux", None),
}

system = platform.system()
if not system in platform_model_mappings:
    print(f"Unsupported platform: {system}", file=sys.stderr)
    sys.exit(1)

platform_model = platform_model_mappings[system]
script_dir = os.path.dirname(os.path.abspath(__file__))
binaries_path = os.path.normpath(os.path.join(script_dir, "Binaries", platform_model.platform_name, f"premake5{platform_model.opt_file_extension or ''}"))

if not os.path.isfile(binaries_path):
    print(f"Error: Premake binary not found at: {binaries_path}", file=sys.stderr)
    sys.exit(1)

print(binaries_path)