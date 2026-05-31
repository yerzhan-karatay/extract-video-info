from __future__ import annotations

import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


@dataclass
class CommandResult:
    command: list[str]
    stdout: str
    stderr: str
    returncode: int


class CommandError(RuntimeError):
    def __init__(self, result: CommandResult) -> None:
        self.result = result
        command = " ".join(result.command)
        stderr = result.stderr.strip()
        message = f"Command failed ({result.returncode}): {command}"
        if stderr:
            message = f"{message}\n{stderr}"
        super().__init__(message)


def run_command(
    command: list[str],
    *,
    env: dict[str, str] | None = None,
    cwd: Path | None = None,
    check: bool = True,
) -> CommandResult:
    result = subprocess.run(
        command,
        cwd=str(cwd) if cwd else None,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )
    command_result = CommandResult(
        command=command,
        stdout=result.stdout or "",
        stderr=result.stderr or "",
        returncode=result.returncode,
    )
    if check and result.returncode != 0:
        raise CommandError(command_result)
    return command_result


def find_command(name: str) -> str | None:
    return shutil.which(name)


def require_command(name: str, install_hint: str | None = None) -> str:
    path = find_command(name)
    if path:
        return path
    hint = f" {install_hint}" if install_hint else ""
    raise RuntimeError(f"Required command not found: {name}.{hint}")
