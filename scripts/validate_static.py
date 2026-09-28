from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    text = (ROOT / "index.html").read_text(encoding="utf-8")
    if "media/" in text:
        raise SystemExit("Ainda existem referências locais para a pasta media/ ausente.")
    if "data:image/svg+xml" not in text:
        raise SystemExit("Placeholder visual esperado não encontrado.")
    print("Portal acadêmico validado sem referências de mídia ausentes.")


if __name__ == "__main__":
    main()
