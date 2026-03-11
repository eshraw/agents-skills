#!/usr/bin/env python3
"""Syncs agents-skills repo to Claude Code plugin marketplace structure.

Source (agents-skills):
  domain/plugin-name/SKILL.md            → single-skill plugin
  domain/plugin-name/skill-name/SKILL.md → multi-skill plugin

Target (skills-mkp):
  .claude-plugin/marketplace.json
  domain/plugin-name/
    .claude-plugin/plugin.json
    skills/
      skill-name/
        SKILL.md (+ scripts/, references/, assets/, ...)
"""

import json
import re
import shutil
import sys
from pathlib import Path

import yaml

SOURCE = Path(sys.argv[1])
TARGET = Path(sys.argv[2])

DOMAINS = ["product-management", "design", "engineering"]
OWNER = "eshraw"
MARKETPLACE_NAME = "agents-skills"


def find_skill_file(directory: Path):
    for name in ["SKILL.md", "SKILL.MD"]:
        f = directory / name
        if f.exists():
            return f
    return None


def parse_frontmatter(skill_file: Path) -> dict:
    content = skill_file.read_text()
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return {}
    try:
        return yaml.safe_load(match.group(1)) or {}
    except Exception:
        return {}


def read_readme_description(directory: Path):
    readme = directory / "README.md"
    if not readme.exists():
        return None
    for line in readme.read_text().split("\n"):
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("```"):
            return line
    return None


def copy_skill_dir(src: Path, dst: Path):
    """Copy skill directory to destination, skipping .claude-plugin."""
    dst.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        if item.name == ".claude-plugin":
            continue
        if item.is_file():
            shutil.copy2(item, dst / item.name)
        elif item.is_dir():
            shutil.copytree(str(item), str(dst / item.name), dirs_exist_ok=True)


def write_plugin_json(dst_plugin: Path, name: str, description: str, keywords: list, requires_mcp=None):
    data = {
        "name": name,
        "version": "1.0.0",
        "description": description,
        "author": {"name": OWNER},
        "keywords": keywords,
        "skills": "./skills",
    }
    if requires_mcp:
        data["metadata"] = {"mcp-server": requires_mcp}
    plugin_meta_dir = dst_plugin / ".claude-plugin"
    plugin_meta_dir.mkdir(parents=True, exist_ok=True)
    (plugin_meta_dir / "plugin.json").write_text(json.dumps(data, indent=2) + "\n")


def get_mcp_requirement(fm: dict):
    meta = fm.get("metadata")
    if isinstance(meta, dict):
        return meta.get("mcp-server")
    return None


def clear_target(target: Path):
    """Clear target directory except .git."""
    for item in target.iterdir():
        if item.name == ".git":
            continue
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)


def main():
    clear_target(TARGET)

    plugins = []

    for domain in DOMAINS:
        src_domain = SOURCE / domain
        if not src_domain.exists():
            continue

        for plugin_dir in sorted(src_domain.iterdir()):
            if not plugin_dir.is_dir():
                continue

            dst_plugin = TARGET / domain / plugin_dir.name
            direct_skill = find_skill_file(plugin_dir)
            skill_subdirs = [
                d for d in sorted(plugin_dir.iterdir())
                if d.is_dir() and find_skill_file(d)
            ]

            if direct_skill:
                # Single-skill plugin: SKILL.md lives at the plugin root
                fm = parse_frontmatter(direct_skill)
                name = plugin_dir.name
                description = fm.get("description", name)
                requires_mcp = get_mcp_requirement(fm)

                write_plugin_json(dst_plugin, name, description, [domain], requires_mcp)
                copy_skill_dir(plugin_dir, dst_plugin / "skills" / name)

            elif skill_subdirs:
                # Multi-skill plugin: subdirectories each contain a SKILL.md
                name = plugin_dir.name
                description = read_readme_description(plugin_dir) or name

                # Collect mcp requirement from any skill that needs it
                requires_mcp = None
                for skill_sub in skill_subdirs:
                    sf = find_skill_file(skill_sub)
                    if sf:
                        fm = parse_frontmatter(sf)
                        requires_mcp = get_mcp_requirement(fm)
                        if requires_mcp:
                            break

                write_plugin_json(dst_plugin, name, description, [domain, name], requires_mcp)

                for skill_sub in skill_subdirs:
                    copy_skill_dir(skill_sub, dst_plugin / "skills" / skill_sub.name)

                # Carry over README.md to plugin root
                readme = plugin_dir / "README.md"
                if readme.exists():
                    shutil.copy2(readme, dst_plugin / "README.md")

            else:
                # No skills found, skip
                continue

            plugins.append({
                "name": name,
                "source": f"./{domain}/{plugin_dir.name}",
                "description": description,
                "version": "1.0.0",
            })

    # Write root marketplace.json
    marketplace_meta = TARGET / ".claude-plugin"
    marketplace_meta.mkdir(parents=True, exist_ok=True)
    marketplace_json = {
        "name": MARKETPLACE_NAME,
        "owner": {"name": OWNER},
        "plugins": plugins,
    }
    (marketplace_meta / "marketplace.json").write_text(json.dumps(marketplace_json, indent=2) + "\n")

    print(f"Synced {len(plugins)} plugins to {TARGET}")
    for p in plugins:
        print(f"  - {p['name']} ({p['source']})")


if __name__ == "__main__":
    main()
