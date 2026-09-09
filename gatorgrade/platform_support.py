"""Platform support checks for GatorGrade features."""

import platform
import sys

# match the values used by the dependency marker in pyproject.toml
ARCH_X86_64 = "x86_64"
SYSTEM_DARWIN = "darwin"
UNSUPPORTED_LOCAL_AUTO_HINT_PLATFORMS = frozenset(
    {(SYSTEM_DARWIN, ARCH_X86_64)}
)


def supports_local_auto_hints() -> bool:
    """Return whether the current platform supports local auto-hints."""
    current_platform = (sys.platform, platform.machine())
    return current_platform not in UNSUPPORTED_LOCAL_AUTO_HINT_PLATFORMS
