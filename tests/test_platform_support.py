"""Tests for platform-specific GatorGrade feature support."""

import pytest

from gatorgrade import platform_support

ARCH_ARM64 = "arm64"
SYSTEM_LINUX = "linux"
SUPPORTED_PLATFORMS = (
    (platform_support.SYSTEM_DARWIN, ARCH_ARM64),
    (SYSTEM_LINUX, platform_support.ARCH_X86_64),
)


def test_supports_local_auto_hints_rejects_darwin_x86_64(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    """Reject local auto-hints on Darwin x86_64."""
    monkeypatch.setattr(
        platform_support.sys, "platform", platform_support.SYSTEM_DARWIN
    )
    monkeypatch.setattr(
        platform_support.platform,
        "machine",
        lambda: platform_support.ARCH_X86_64,
    )
    assert not platform_support.supports_local_auto_hints()


@pytest.mark.parametrize(("system", "architecture"), SUPPORTED_PLATFORMS)
def test_supports_local_auto_hints_accepts_supported_platforms(
    monkeypatch: pytest.MonkeyPatch,
    system: str,
    architecture: str,
) -> None:
    """Accept local auto-hints on supported platform combinations."""
    monkeypatch.setattr(platform_support.sys, "platform", system)
    monkeypatch.setattr(
        platform_support.platform, "machine", lambda: architecture
    )
    assert platform_support.supports_local_auto_hints()
