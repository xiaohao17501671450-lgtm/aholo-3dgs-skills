# Aholo 3DGS Skills

Cursor agent skills for Aholo OpenAPI v1 3D tasks (reconstruction / generation): upload assets, create tasks (`worldId`), poll status, and fetch results (PLY / SPZ / SOG).

| Skill | Region | Gateway | API keys |
|-------|--------|---------|----------|
| `aholo-3dgs-reconstruction` | China | `api.aholo3d.cn` | [labs.aholo3d.cn](https://labs.aholo3d.cn/api-keys) |
| `aholo-3dgs-reconstruction-global` | Global | `api.aholo3d.com` | [labs.aholo3d.com](https://labs.aholo3d.com/api-keys) |

Install **one** skill for your region (or both if you use both platforms). Set `AHOLO_API_KEY` in your environment before use.

## Install

Using the [skills CLI](https://github.com/worldlabsai/marble-developer-api-skill) (recommended):

```sh
# China
npx skills add xiaohao17501671450-lgtm/aholo-3dgs-skills --skill aholo-3dgs-reconstruction --global

# Global
npx skills add xiaohao17501671450-lgtm/aholo-3dgs-skills --skill aholo-3dgs-reconstruction-global --global

# List skills in this repo
npx skills add xiaohao17501671450-lgtm/aholo-3dgs-skills --list
```

Manual install (personal skills):

```powershell
git clone https://github.com/xiaohao17501671450-lgtm/aholo-3dgs-skills.git
Copy-Item -Recurse aholo-3dgs-skills\skills\aholo-3dgs-reconstruction $env:USERPROFILE\.cursor\skills\
# or
Copy-Item -Recurse aholo-3dgs-skills\skills\aholo-3dgs-reconstruction-global $env:USERPROFILE\.cursor\skills\
```

Project skills: copy the chosen folder into `.cursor/skills/` in your repo.

Python dependencies (per skill directory):

```sh
pip install -r skills/aholo-3dgs-reconstruction/requirements.txt
```

## Example prompts

```text
Use the aholo-3dgs-reconstruction skill to rebuild a room from D:/photos with scene=space and taskQuality=high.
```

```text
Use the aholo-3dgs-reconstruction-global skill to create a 3DGS from a video and poll until complete.
```

## Layout

```text
skills/
  aholo-3dgs-reconstruction/
    SKILL.md
    aholo_reconstruct.py
    requirements.txt
  aholo-3dgs-reconstruction-global/
    SKILL.md
    aholo_reconstruct.py
    requirements.txt
```

## Legacy repos

The older single-skill repositories are deprecated in favor of this monorepo:

- [aholo-3dgs-reconstruction](https://github.com/xiaohao17501671450-lgtm/aholo-3dgs-reconstruction)
- [aholo-3dgs-reconstruction-global](https://github.com/xiaohao17501671450-lgtm/aholo-3dgs-reconstruction-global)
