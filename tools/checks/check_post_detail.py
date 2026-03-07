import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

FILES = {
    "controller": ROOT / "backend" / "post" / "controllers.py",
    "view": ROOT / "backend" / "post" / "views.py",
    "frontend": ROOT / "frontend" / "src" / "post" / "post_detail_page.tsx",
    "backend_test": ROOT / "backend" / "tests" / "test_post_detail.py",
    "frontend_test": ROOT / "frontend" / "src" / "post" / "post_detail_page.test.tsx",
    "ci": ROOT / ".github" / "workflows" / "ci.yml",
}


def contains(path: Path, needle: str) -> bool:
    if not path.exists():
        return False
    return needle in path.read_text(encoding="utf-8")


def main() -> None:
    result = {
        "task": "post-detail",
        "checks": [
            {
                "name": "controller function exists",
                "passed": contains(FILES["controller"], "def get_post_detail"),
            },
            {
                "name": "view returns 404 path",
                "passed": contains(FILES["view"], "HTTP_404_NOT_FOUND"),
            },
            {
                "name": "frontend loadPost exists",
                "passed": contains(FILES["frontend"], "const loadPost"),
            },
            {
                "name": "backend unittest file exists",
                "passed": FILES["backend_test"].exists(),
            },
            {
                "name": "frontend test file exists",
                "passed": FILES["frontend_test"].exists(),
            },
            {
                "name": "github actions exists",
                "passed": FILES["ci"].exists(),
            },
        ],
        "suggested_commands": [
            "cd backend && python manage.py test tests.test_post_detail",
            "cd frontend && CI=true npm test -- --watchAll=false --runInBand",
        ],
    }
    result["passed"] = all(item["passed"] for item in result["checks"])
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
