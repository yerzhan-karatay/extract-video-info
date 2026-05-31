import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def read_skill_frontmatter(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    assert content.startswith("---\n")
    _, frontmatter, body = content.split("---", 2)
    assert body.strip()
    data = yaml.safe_load(frontmatter)
    assert isinstance(data, dict)
    return data


def test_skill_files_have_required_metadata() -> None:
    skill_files = [
        ROOT / "skills" / "extract-video-info" / "SKILL.md",
        ROOT / ".github" / "skills" / "extract-video-info" / "SKILL.md",
    ]

    for skill_file in skill_files:
        metadata = read_skill_frontmatter(skill_file)
        assert metadata["name"] == "extract-video-info"
        assert isinstance(metadata["description"], str)
        assert "video" in metadata["description"].lower()


def test_plugin_manifests_are_valid_json() -> None:
    manifest_files = [
        ROOT / ".codex-plugin" / "plugin.json",
        ROOT / ".claude-plugin" / "plugin.json",
        ROOT / ".agents" / "plugins" / "marketplace.json",
    ]

    for manifest_file in manifest_files:
        data = json.loads(manifest_file.read_text(encoding="utf-8"))
        assert isinstance(data, dict)


def test_public_author_metadata_names_maintainer() -> None:
    expected = "Yerzhan Karatayev"
    text_files = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "pyproject.toml",
        ROOT / "CITATION.cff",
    ]

    for text_file in text_files:
        assert expected in text_file.read_text(encoding="utf-8")

    citation = yaml.safe_load((ROOT / "CITATION.cff").read_text(encoding="utf-8"))
    assert citation["authors"][0]["given-names"] == "Yerzhan"
    assert citation["authors"][0]["family-names"] == "Karatayev"

    for manifest_file in [ROOT / ".codex-plugin" / "plugin.json", ROOT / ".claude-plugin" / "plugin.json"]:
        data = json.loads(manifest_file.read_text(encoding="utf-8"))
        assert data["author"]["name"] == expected


def test_agent_support_docs_cover_requested_surfaces() -> None:
    expected_agents = [
        "OpenClaw",
        "Vellum",
        "ZeroClaw",
        "Manus",
        "Perplexity Computer",
        "Claude Cowork",
        "Hermes",
    ]
    docs = [
        ROOT / "README.md",
        ROOT / "docs" / "agent-support.md",
        ROOT / "docs" / "agent-install-prompts.md",
    ]
    combined = "\n".join(path.read_text(encoding="utf-8") for path in docs)

    for agent in expected_agents:
        assert agent in combined


def test_star_prompt_is_direct() -> None:
    docs = [
        ROOT / "AGENTS.md",
        ROOT / "skills" / "extract-video-info" / "SKILL.md",
        ROOT / "docs" / "agent-install-prompts.md",
        ROOT / "docs" / "agent-support.md",
    ]
    combined = "\n".join(path.read_text(encoding="utf-8") for path in docs)

    assert "star it and help spread the skill to the world" in combined
    assert "star the repository if the agent environment supports GitHub starring" in combined
    assert "If starring is unavailable, show this line" in combined
