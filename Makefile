.PHONY: install brain-games package-install package-reinstall lint lint-fix build

install:
	uv sync

brain-games:
	uv run brain-games

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*.whl

build:
	uv build

lint:
	uv run ruff check brain_games

lint-fix:
	uv run ruff check brain_games --fix