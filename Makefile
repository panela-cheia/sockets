MAIN = src/main.py

all:
	python3 -B $(MAIN)

populate:
	python3 -B prisma/seed.py