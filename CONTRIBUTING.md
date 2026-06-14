# Contributing

This is a personal portfolio project, but issues and pull requests are welcome.

## Commit messages

Follow [Conventional Commits](https://www.conventionalcommits.org/):
`feat(scope): ...`, `fix(scope): ...`, `docs: ...`, `chore: ...`.

## Before opening a PR

- App changes: `cd app && ruff check . && pytest`
- Terraform changes: `cd terraform && terraform fmt -check && terraform validate`
- Ansible changes: `ansible-playbook --syntax-check -i ansible/inventory.example.ini ansible/playbook.yml`

CI runs the app lint and tests automatically on every PR.
