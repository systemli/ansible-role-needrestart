# AGENTS.md

Ansible role that installs and configures needrestart on Debian (trixie, bookworm).

## Layout

- `defaults/main.yml`: all role variables with defaults
- `tasks/main.yml`: installs needrestart and deploys its configuration
- `templates/`, `files/`: needrestart configuration (`needrestart.conf` and friends)
- `meta/main.yml`: Galaxy metadata
- `molecule/default/`: integration test (Docker, Debian 13)

## Checks

- `ansible-lint .` must pass without warnings (default configuration, no config file)
- `molecule test` runs the role in a container; CI runs it via the shared systemli workflow
- `ansible-lint` creates `.ansible/`; never commit it

## Conventions

- Use fully qualified module names, quoted octal `mode` values and `true`/`false` booleans
- Give every task a `name`
- New or changed role variables need an entry in `defaults/main.yml` and the README
- Pin GitHub Actions to commit SHAs with a trailing `# vX.Y.Z` comment; Dependabot updates them

## Commits and PRs

- Write in English, use conventional commit titles (`feat:`, `fix:`, `chore:`, `ci:`; `!` for breaking changes)
- The PR title sets the release-drafter label (`enhancement`, `bug`, `chore`, `breaking`); a breaking change bumps the major version
- Open PRs as draft and fill in `.github/pull_request_template.md`: what changed and why, plus a breaking changes section if needed
- Do not list changed files or claim test results in the description; CI covers that
