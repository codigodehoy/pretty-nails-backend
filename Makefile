create-env:
	python3 -m venv .venv \
	&& . .venv/bin/activate

install-dependencies:
	. .venv/bin/activate \
	&& pip3 install -r requirements.txt

start:
	. .venv/bin/activate \
	&& python3 runner.py

test:
	. .venv/bin/activate \
	&& pytest
