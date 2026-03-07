import argparse
import json
import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, List, Optional

ROOT = Path(__file__).resolve().parents[2]
BACKEND = ROOT / "backend"
FRONTEND = ROOT / "frontend"
PYTHON = sys.executable

FILES = {
    "controller": ROOT / "backend" / "post" / "controllers.py",
    "view": ROOT / "backend" / "post" / "views.py",
    "urls": ROOT / "backend" / "post" / "urls.py",
    "frontend_page": ROOT / "frontend" / "src" / "post" / "post_detail_page.tsx",
    "frontend_api": ROOT / "frontend" / "src" / "backend.tsx",
    "frontend_entry": ROOT / "frontend" / "src" / "index.tsx",
    "backend_unit_test": ROOT / "backend" / "tests" / "test_post_detail.py",
    "backend_api_test": ROOT / "backend" / "tests" / "test_post_detail_api.py",
    "frontend_test": ROOT / "frontend" / "src" / "post" / "post_detail_page.test.tsx",
    "ci": ROOT / ".github" / "workflows" / "ci.yml",
    "package_json": ROOT / "frontend" / "package.json",
}


def read(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def has_all(path: Path, needles: List[str]) -> bool:
    text = read(path)
    return all(needle in text for needle in needles)


def run(cmd: List[str], cwd: Path, env: Optional[Dict[str, str]] = None) -> dict:
    merged_env = os.environ.copy()
    if env:
        merged_env.update(env)

    process = subprocess.run(
        cmd,
        cwd=str(cwd),
        capture_output=True,
        text=True,
        env=merged_env,
    )
    return {
        "command": " ".join(cmd),
        "passed": process.returncode == 0,
        "stdout": process.stdout[-4000:],
        "stderr": process.stderr[-4000:],
    }


def task_1() -> dict:
    checks = [
        {
            "name": "controller has get_post_detail",
            "passed": has_all(FILES["controller"], ["def get_post_detail"]),
        },
        {
            "name": "view has PostDetailView.get and 404",
            "passed": has_all(
                FILES["view"],
                ["class PostDetailView", "def get", "HTTP_404_NOT_FOUND"],
            ),
        },
        {
            "name": "detail url exists",
            "passed": "api/v1/post/<int:postId>" in read(FILES["urls"]),
        },
        {
            "name": "backend controller tests pass",
            **run([PYTHON, "manage.py", "test", "--filter", "tests.test_post_detail"], BACKEND),
        },
    ]

    return {
        "task": 1,
        "name": "后端帖子详情接口",
        "passed": all(item["passed"] for item in checks),
        "checks": checks,
    }


def task_2() -> dict:
    checks = [
        {
            "name": "frontend page has loadPost",
            "passed": has_all(FILES["frontend_page"], ["const loadPost"]),
        },
        {
            "name": "frontend api has post(postId)",
            "passed": has_all(
                FILES["frontend_api"],
                ["export async function post(postId: number)"],
            ),
        },
        {
            "name": "frontend post detail tests pass",
            **run(
                [
                    "npm",
                    "test",
                    "--",
                    "--watchAll=false",
                    "--runInBand",
                    "--testPathPattern=post_detail_page.test.tsx",
                ],
                FRONTEND,
                env={"CI": "true"},
            ),
        },
    ]

    return {
        "task": 2,
        "name": "前端帖子详情页加载",
        "passed": all(item["passed"] for item in checks),
        "checks": checks,
    }


def task_3() -> dict:
    checks = [
        {
            "name": "frontend route mentions /post/:postId",
            "passed": "/post/:postId" in read(FILES["frontend_entry"]),
        },
        {
            "name": "frontend package has CRA proxy",
            "passed": '"proxy": "http://127.0.0.1:8000"' in read(FILES["package_json"]),
        },
        {
            "name": "backend detail url exists",
            "passed": "api/v1/post/<int:postId>" in read(FILES["urls"]),
        },
        {
            "name": "task 1 already passed",
            "passed": task_1()["passed"],
        },
        {
            "name": "task 2 already passed",
            "passed": task_2()["passed"],
        },
    ]

    return {
        "task": 3,
        "name": "前后端联调",
        "passed": False,
        "status": "manual_required",
        "checks": checks,
        "manual_steps": [
            "cd backend && python manage.py runserver",
            "cd frontend && npm start",
            "浏览器打开 http://localhost:3000/post/1",
            "再打开一个不存在的帖子 ID，确认页面显示错误信息",
            "打开浏览器 Network 面板，确认请求发到了后端接口",
        ],
    }


def task_4() -> dict:
    checks = [
        {
            "name": "unit test file exists",
            "passed": FILES["backend_unit_test"].exists(),
        },
        {
            "name": "unit tests include required cases",
            "passed": has_all(
                FILES["backend_unit_test"],
                [
                    "test_get_post_detail_success",
                    "test_get_post_detail_not_found",
                    "test_reply_order_and_root_reply_id",
                ],
            ),
        },
        {
            "name": "unit tests pass",
            **run([PYTHON, "manage.py", "test", "--filter", "tests.test_post_detail"], BACKEND),
        },
    ]

    return {
        "task": 4,
        "name": "后端单元测试",
        "passed": all(item["passed"] for item in checks),
        "checks": checks,
    }


def task_5() -> dict:
    checks = [
        {
            "name": "api test file exists",
            "passed": FILES["backend_api_test"].exists(),
        },
        {
            "name": "api tests include required cases",
            "passed": has_all(
                FILES["backend_api_test"],
                [
                    "test_get_post_detail_returns_200",
                    "test_get_post_detail_returns_404_for_missing_post",
                    "test_get_post_detail_requires_auth",
                ],
            ),
        },
    ]

    if FILES["backend_api_test"].exists():
        checks.append(
            {
                "name": "api tests pass",
                **run(
                    [PYTHON, "manage.py", "test", "--filter", "tests.test_post_detail_api"],
                    BACKEND,
                ),
            }
        )

    return {
        "task": 5,
        "name": "API 测试",
        "passed": all(item["passed"] for item in checks),
        "checks": checks,
    }


def task_6() -> dict:
    ci_text = read(FILES["ci"])
    checks = [
        {
            "name": "ci file exists",
            "passed": FILES["ci"].exists(),
        },
        {
            "name": "ci has push and pull_request",
            "passed": all(k in ci_text for k in ["push:", "pull_request:"]),
        },
        {
            "name": "ci has backend unit/api/frontend jobs",
            "passed": all(
                k in ci_text
                for k in ["backend-unit-tests", "backend-api-tests", "frontend-tests"]
            ),
        },
        {
            "name": "ci runs backend unit test command",
            "passed": "tests.test_post_detail" in ci_text,
        },
        {
            "name": "ci runs backend api test command",
            "passed": "tests.test_post_detail_api" in ci_text,
        },
        {
            "name": "ci runs frontend test command",
            "passed": "npm test" in ci_text,
        },
    ]

    return {
        "task": 6,
        "name": "GitHub Actions CI",
        "passed": all(item["passed"] for item in checks),
        "checks": checks,
        "manual_steps": [
            "git add . && git commit -m 'complete ci'",
            "git push",
            "打开 GitHub Actions 页面确认 workflow 通过",
        ],
    }


TASKS = {
    1: task_1,
    2: task_2,
    3: task_3,
    4: task_4,
    5: task_5,
    6: task_6,
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", type=int, choices=TASKS.keys())
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    if args.all:
        results = [TASKS[i]() for i in range(1, 7)]
        print(
            json.dumps(
                {
                    "mode": "all",
                    "results": results,
                    "passed": all(
                        item.get("passed", False) for item in results if item["task"] != 3
                    ),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.task:
        print(json.dumps(TASKS[args.task](), ensure_ascii=False, indent=2))
        return

    parser.error("use --task N or --all")


if __name__ == "__main__":
    main()
