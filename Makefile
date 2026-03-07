.PHONY: check backend-test frontend-test test

PYTHON ?= python3

check:
	$(PYTHON) tools/checks/check_post_detail.py

backend-test:
	cd backend && $(PYTHON) manage.py test --filter tests.test_post_detail

frontend-test:
	cd frontend && CI=true npm test -- --watchAll=false --runInBand

test: backend-test frontend-test
