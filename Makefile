.PHONY: check check-all \
	check-task-1 check-task-2 check-task-3 check-task-4 check-task-5 check-task-6 \
	backend-test backend-api-test frontend-test test

PYTHON ?= python3

check: check-all

check-task-1:
	$(PYTHON) tools/checks/check_post_detail.py --task 1

check-task-2:
	$(PYTHON) tools/checks/check_post_detail.py --task 2

check-task-3:
	$(PYTHON) tools/checks/check_post_detail.py --task 3

check-task-4:
	$(PYTHON) tools/checks/check_post_detail.py --task 4

check-task-5:
	$(PYTHON) tools/checks/check_post_detail.py --task 5

check-task-6:
	$(PYTHON) tools/checks/check_post_detail.py --task 6

check-all:
	$(PYTHON) tools/checks/check_post_detail.py --all

backend-test:
	cd backend && $(PYTHON) manage.py test --filter tests.test_post_detail

backend-api-test:
	cd backend && $(PYTHON) manage.py test --filter tests.test_post_detail_api

frontend-test:
	cd frontend && CI=true npm test -- --watchAll=false --runInBand --testPathPattern=post_detail_page.test.tsx

test: backend-test backend-api-test frontend-test
