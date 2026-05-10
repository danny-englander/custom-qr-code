"""Generate QR code PNGs using https://github.com/lincolnloop/python-qrcode."""

from __future__ import annotations

import argparse
import uuid
from pathlib import Path

_CODES_DIR = Path(__file__).resolve().parent / "codes"

try:
    import qrcode
    from qrcode.image.styledpil import StyledPilImage
except ModuleNotFoundError as exc:  # pragma: no cover - env setup hint
    raise SystemExit(
        "The 'qrcode' package is not installed for this Python.\n"
        "From the qr/ folder run:\n"
        "  python3 -m venv .venv\n"
        "  .venv/bin/pip install -r requirements.txt\n"
        "  .venv/bin/python main.py\n"
        "Or: source .venv/bin/activate && python main.py"
    ) from exc

from drawers import vertical_bars_drawer


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a QR code PNG.")
    parser.add_argument(
        "data",
        nargs="?",
        default="https://example.com",
        help="Payload to encode (default: https://example.com)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=_CODES_DIR,
        help=f"Directory for PNG + sidecar TXT (default: {_CODES_DIR})",
    )
    parser.add_argument(
        "--style",
        choices=("plain", "vertical-bars"),
        default="plain",
        help="plain: default squares; vertical-bars: rounded vertical bar modules",
    )
    parser.add_argument(
        "--horizontal-shrink",
        type=float,
        default=0.8,
        metavar="R",
        help="For vertical-bars only: bar width factor 0–1 (default: 0.8)",
    )
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    code_id = uuid.uuid4().hex[:10]
    png_path = args.output_dir / f"{code_id}.png"
    txt_path = args.output_dir / f"{code_id}.txt"

    if args.style == "plain":
        img = qrcode.make(args.data)
    else:
        if not 0 < args.horizontal_shrink <= 1:
            parser.error("--horizontal-shrink must be between 0 and 1 (exclusive of 0).")
        qr = qrcode.QRCode(
            version=None,
            error_correction=qrcode.constants.ERROR_CORRECT_M,
            box_size=10,
            border=4,
        )
        qr.add_data(args.data)
        qr.make(fit=True)
        img = qr.make_image(
            image_factory=StyledPilImage,
            module_drawer=vertical_bars_drawer(args.horizontal_shrink),
        )

    img.save(png_path)
    txt_path.write_text(f"{args.data}\n", encoding="utf-8")
    print(f"Wrote {png_path.resolve()}")
    print(f"Wrote {txt_path.resolve()}")


if __name__ == "__main__":
    main()
