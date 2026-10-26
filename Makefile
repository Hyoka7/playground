.PHONY: run

run:
	@PYTHONPATH=. .venv/bin/pyc main.py -t op.QuestionOP 2>/dev/null
