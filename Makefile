TEST_FILE = test_harvest.py
.PHONY: run

run :
	python3 -m unittest $(TEST_FILE)
