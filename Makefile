.PHONY: run

TRACERS := $(shell PYTHONPATH=. .venv/bin/python -c 'import inspect, op, pyccolo; print(" ".join("op." + name for name, cls in inspect.getmembers(op, inspect.isclass) if cls.__module__ == "op" and issubclass(cls, pyccolo.BaseTracer)))' 2>/dev/null)

run:
	@PYTHONPATH=. .venv/bin/pyc main.py -t $(TRACERS) 2>/dev/null
