import io
from flask import Flask, request, send_file, jsonify
from PIL import Image, ImageOps

app = Flask(__name__)

# Allowed formats map: UI value -> (Pillow format, file extension, mimetype)
ALLOWED = {
    "PNG":  ("PNG",  "png",  "image/png"),
    "JPEG": ("JPEG", "jpg",  "image/jpeg"),
    "WEBP": ("WEBP", "webp", "image/webp"),
    "GIF":  ("GIF",  "gif",  "image/gif"),
    "BMP":  ("BMP",  "bmp",  "image/bmp"),
    "TIFF": ("TIFF", "tiff", "image/tiff"),
}

def build_save_params(fmt, quality):
    q = max(1, min(int(quality or 85), 100))
    if fmt in ("JPEG", "WEBP"):
        return {"quality": q}
    elif fmt == "PNG":
        # Map 1..100 -> compress_level 9..0
        comp = max(0, min(9, 9 - int(q / 11.12)))
        return {"optimize": True, "compress_level": comp}
    return {}

@app.post("/api/convert")
def convert():
    """
    Multipart form-data:
      - file: image file
      - format: PNG | JPEG | WEBP | GIF | BMP | TIFF
      - mode: percent | exact | none
      - percent: e.g. "50"
      - width, height: integers (for exact)
      - quality: 1..100  (JPEG/WEBP use; PNG compresses)
    Response: converted image as attachment.
    """
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["file"]
    target = (request.form.get("format") or "PNG").upper()
    if target not in ALLOWED:
        return jsonify({"error": "Unsupported format"}), 400

    mode = (request.form.get("mode") or "none").lower()
    quality = request.form.get("quality", "85")

    try:
        img = Image.open(file.stream)
        img = ImageOps.exif_transpose(img)  # fix EXIF orientation

        # --- Resize ---
        if mode == "percent":
            percent = float(request.form.get("percent") or "100")
            if percent != 100:
                w = max(1, int(img.width * percent / 100))
                h = max(1, int(img.height * percent / 100))
                img = img.resize((w, h), Image.Resampling.LANCZOS)
        elif mode == "exact":
            w = int(request.form.get("width") or 0)
            h = int(request.form.get("height") or 0)
            if w > 0 and h > 0:
                img = img.resize((w, h), Image.Resampling.LANCZOS)

        fmt, ext, mime = ALLOWED[target]

        # remove alpha for formats that don't support it
        if fmt in ("JPEG", "BMP", "TIFF") and img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        save_params = build_save_params(fmt, quality)

        buf = io.BytesIO()
        img.save(buf, fmt, **save_params)
        buf.seek(0)

        filename = (file.filename or f"image.{ext}").rsplit(".", 1)[0] + f".{ext}"
        return send_file(
            buf,
            mimetype=mime,
            as_attachment=True,
            download_name=filename
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500
