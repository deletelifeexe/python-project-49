.PHONY: install

install:
	uv sync

brain-games:
	uv run brain-games

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --force dist/*.whl
