import yaml
from pathlib import Path

FLAGS_FILE = Path("feature-flags/flags.yml")
NAV_V1 = Path("feature-flags/sidebar/nav_v1.yml")
NAV_V2 = Path("feature-flags/sidebar/nav_v2.yml")
OUT = Path("mkdocs.yml")

BASE = {
    "site_name": "ITProjects-DOCS",
    "docs_dir": "docs",
    "theme": {"name": "mkdocs"},
    "plugins": ["search"],
    "repo_name": "nhateoff/ITProjects-DOCS",
    "repo_url": "https://github.com/nhateoff/ITProjects-DOCS",
    "edit_uri": "edit/main/docs/",
    "markdown_extensions": [
        {"toc": {"permalink": True}},
        "admonition",
        "tables",
    ],
}

def flag_enabled(key: str) -> bool:
    data = yaml.safe_load(FLAGS_FILE.read_text(encoding="utf-8"))
    for f in data.get("flags", []):
        if f.get("key") == key:
            # simple rule: if prod.enabled true AND rollout > 0 -> enabled
            prod = f.get("environments", {}).get("prod", {})
            return bool(prod.get("enabled", False)) and int(prod.get("rollout", 0)) > 0
    return False

def main():
    use_v2 = flag_enabled("wiki.sidebar.v2")
    nav_file = NAV_V2 if use_v2 else NAV_V1
    nav = yaml.safe_load(nav_file.read_text(encoding="utf-8"))

    cfg = dict(BASE)
    cfg["nav"] = nav

    OUT.write_text(yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"mkdocs.yml generated with {'v2' if use_v2 else 'v1'} navigation")

if __name__ == "__main__":
    main()
