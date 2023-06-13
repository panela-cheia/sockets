MAIN = src/main.py

all:
	python3 -B $(MAIN)

venv:
	python3 -m venv . && . bin/activate && pip3 install -r requirements.txt && prisma generate

run_venv:
	. bin/activate && python3 -B $(MAIN)

clean:
	true || deactivate && rm -rf bin/ lib/ lib64/ lib64 include/ share/ pyvenv.cfg

populate:
	python3 -B prisma/seed.py

test:
	python3 -B src/test-server.py