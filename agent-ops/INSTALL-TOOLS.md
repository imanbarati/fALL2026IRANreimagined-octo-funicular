# RTK and Caveman — Token Efficiency Setup

Last checked against upstream documentation: 2026-11-10. Re-check upstream instructions before installing because commands and supported agents can change.

These tools are optional local developer tools. A repository cannot install them on every agent's machine simply by adding a Markdown file. Each Claude Code / Codex / Gemini / OpenCode workstation or container must install and verify its own copy.

## 1. RTK (Rust Token Killer)

Upstream: https://github.com/rtk-ai/rtk

RTK is a CLI that reduces noisy terminal output before it enters an agent's context. Do not confuse it with unrelated packages also named `rtk`.

### Windows PowerShell
```powershell
winget install rtk-ai.rtk
rtk --version
rtk gain
```
If the package manager cannot find it, use the official RTK releases page and install the Windows binary from the upstream project. Do not install an arbitrary package named `rtk`.

### macOS / Linux
```bash
curl -fsSL https://raw.githubusercontent.com/rtk-ai/rtk/master/install.sh | sh
rtk --version
rtk gain
```
Review the upstream installer before executing it if your environment requires script inspection.

### Activate for Claude Code
Preview first:
```bash
rtk init --global --dry-run
```
Then, after reviewing the proposed changes:
```bash
rtk init --global
```
Restart Claude Code. For one repository only, run `rtk init` from that repository instead. Global mode installs a hook and may update Claude settings; inspect the diff/backup and do not overwrite existing custom hooks. Windows users who need full hook support may use WSL as documented upstream.

Verify:
```bash
rtk --version
rtk gain
```
If `rtk gain` does not show the RTK savings dashboard, verify that the correct Rust Token Killer binary is installed.

## 2. Caveman skill (shorter agent responses)

Upstream: https://github.com/JuliusBrussee/caveman
Docs: https://docs.caveman.so/caveman/installation

### Install the skill only (recommended low-impact option)
```bash
npx skills add JuliusBrussee/caveman -g
```
For Windows systems where symlink creation is unavailable:
```powershell
npx skills add JuliusBrussee/caveman --copy
```
Use `/caveman` in Claude Code when needed. In Codex the documented invocation is `$caveman`.

### Claude Code plugin option
```bash
claude plugin marketplace add JuliusBrussee/caveman
claude plugin install caveman@caveman
claude plugin list
```
Restart Claude Code after installation/update so hooks and skills load.

### Optional full CLI/proxy
The full Caveman CLI is distinct from the skill-only install:
```bash
npm install -g @caveman-ai/cli
caveman setup --install
caveman learn
```
Use `caveman claude` as documented upstream if you intentionally want to launch Claude through the proxy. Review the installation scope and hooks first. Do not install both variants blindly or assume a proxy is necessary.

## 3. Multi-agent installation rules
- Install and verify separately for each machine, user profile, WSL distro, container or remote dev environment.
- Do not commit local binaries, user settings, credentials, hook state, caches or machine-specific paths.
- Do not run global installers as an unprivileged agent without user authorization.
- Prefer project-local documentation and optional skills; never silently modify another agent's configuration.
- Before updates, inspect release notes and current config. Back up settings before changing hooks.
- Record tool name, version, install method, environment and verification result in the task handoff.
- RTK and Caveman reduce context overhead; they do not authorize omitting chapters, source material, test output needed for diagnosis, or required handoff details.

## 4. Efficient working protocol
- Read handoffs and relevant files before asking another agent to repeat context.
- Use targeted file ranges, search, diffs and summaries; open full files when needed for meaning.
- Keep factual research notes with URLs and access dates.
- Keep output concise but preserve all substantive claims, caveats and citations.
- Do not compress legal, safety, financial or historical source text into a form that loses important qualifications.
- Before reporting token savings, run the tool's own measurement command; do not invent a percentage.
