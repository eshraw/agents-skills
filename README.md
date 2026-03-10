## Agent Skills Collection

This repository is **a growing set of skills based off the Agent Skills specifications**. Each skill is a small, focused capability that can be plugged into AI agents to give them repeatable workflows, domain expertise, or tooling integrations.

### Structure

- **Skill directories**: Each top-level folder (for example, `product-management/`, `design/`, etc.) groups related skills by domain.
- **`SKILL.md` files**: Every skill is defined in a markdown file named `SKILL.md` that:
  - Describes what the skill does and when to use it.
  - Defines the instructions the agent should follow.
  - Follows the Agent Skills specification so tools can discover and load it.

### Installation & Usage

#### OpenAI Codex

Codex loads skills from `.agents/skills` (repo scope) and `~/.agents/skills` (user scope), as described in the Codex skills docs ([link](https://developers.openai.com/codex/skills#create-a-skill)).

You have two main options to install a **single skill** from this repo:

- **Using the built-in installer** (recommended when available in your Codex environment), e.g. for `dsat-initialize-ds`:

  ```bash
  $skill-installer install https://github.com/eshraw/agents-skills/tree/main/design/design-system-as-text/dsat-initialize-ds
  ```

- **Manual copy into a skills directory**, e.g. for `assumption-audit` in the current repository:

  ```bash
  git clone https://github.com/eshane-rawat/agents-skills.git /tmp/agents-skills
  mkdir -p .agents/skills/assumption-audit
  cp -R /tmp/agents-skills/product-management/assumption-audit/* .agents/skills/assumption-audit/
  rm -rf /tmp/agents-skills
  ```

  Or as a **user-wide skill**:

  ```bash
  git clone https://github.com/eshane-rawat/agents-skills.git /tmp/agents-skills
  mkdir -p ~/.agents/skills/assumption-audit
  cp -R /tmp/agents-skills/product-management/assumption-audit/* ~/.agents/skills/assumption-audit/
  rm -rf /tmp/agents-skills
  ```

In all cases, replace the example paths and destination folder names with the specific skill you want (for example, `design/design-system-as-text/dsat-initialize-ds`). Restart Codex if it doesn’t pick up the new skill automatically.

#### Claude

Clone the repo, then copy just the skill you want into Claude’s skills directory, e.g. for `assumption-audit`:

```bash
git clone https://github.com/eshane-rawat/agents-skills.git
cd agents-skills
mkdir -p ~/.claude/skills/assumption-audit
cp -R product-management/assumption-audit/* ~/.claude/skills/assumption-audit/
```

Point your Claude client or orchestration layer at `~/.claude/skills/assumption-audit` as a single registered skill. Repeat with different target names/folders for other skills.

#### Cursor

To install these skills in Cursor using a remote GitHub rule:

- **Open** Cursor Settings → **Rules**
- In **Project Rules**, click **Add Rule**
- Choose **Remote Rule (GitHub)**
- Enter the GitHub repository URL, for example:

  ```text
  https://github.com/eshraw/agents-skills
  ```

Cursor will then pull the skills from this repository according to the rule configuration. You can add additional remote rules if you want to point to other skill repos or forks.

### Using These Skills

- **In an agent environment**: Point your agent framework or tools at this repo (or a subset of folders) so it can load `SKILL.md` definitions according to the Agent Skills spec.
- **Manually**: You can also open any `SKILL.md` and follow the documented workflow as a lightweight playbook for that domain.

### Adding a New Skill

- **Create a folder** for the domain if it does not exist yet (for example, `engineering/`, `research/`).
- **Add `SKILL.md`** inside that folder, following the existing examples:
  - Front‑matter with `name` and `description`.
  - Clear sections for overview, when to use, and step‑by‑step instructions.
- **Keep it focused**: A skill should solve one concrete task or workflow well, rather than many loosely related ones.

### Contributing & Maintenance

- **Consistent format**: Match the structure and tone of existing skills so agents can apply them predictably.
- **Incremental growth**: Treat this as a living library—add new skills as needs arise, and refine existing ones as workflows improve.
- **Compatibility**: When updating skills, avoid breaking changes to names and core behaviors that downstream agents may depend on.

