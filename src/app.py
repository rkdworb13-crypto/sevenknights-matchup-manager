from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def check_project():
    print("=" * 50)
    print(" SevenKnights Matchup Manager ")
    print("=" * 50)

    folders = [
        PROJECT_ROOT / "assets" / "heroes",
        PROJECT_ROOT / "data",
        PROJECT_ROOT / "credentials",
    ]

    for folder in folders:
        if folder.exists():
            print(f"[OK] {folder.name}")
        else:
            print(f"[CREATE] {folder}")
            folder.mkdir(parents=True, exist_ok=True)

    print()
    print("프로젝트 확인 완료")


if __name__ == "__main__":
    check_project()
