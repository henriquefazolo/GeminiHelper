# build.py
import subprocess
import sys


def build_with_nuitka():
    cmd = [
        sys.executable, "-m", "nuitka",
        "--onefile",
        "--windows-console-mode=disable",
        "--windows-icon-from-ico=ico.ico",
        "--include-data-dir=config=config",
        "--product-name=MyApp",
        "--file-description=MyApp Desktop",
        "--product-version=1.0.0",
        "--file-version=1.0.0",
        "--copyright=© 2026 Henrique",
        "--company-name=My Company Name Test",
        "--output-filename=MyApp.exe",
        "--assume-yes-for-downloads",
        "--show-progress",
        "main.py"
    ]

    try:
        subprocess.run(cmd, check=True)
        print("✅ Compilação concluída com sucesso!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro na compilação: {e}")


if __name__ == "__main__":
    build_with_nuitka()