# Ultimate Image Converter (Web Version)

A simple **drag-and-drop** image converter built with **Python (Flask)**, **Pillow** for image manipulation, and **Vercel** for serverless deployment. This tool allows users to convert images between multiple formats (PNG, JPEG, WEBP, GIF, BMP, TIFF) and resize them via percentage, exact dimensions, or target file size.

---

## Features

* ✅ Convert images between **PNG, JPEG, WEBP, GIF, BMP, TIFF**
* ✅ Resize images by **percentage**, **exact dimensions**, or **target file size**
* ✅ Adjust **quality** (1-100) for JPEG/WEBP formats
* ✅ Easy-to-use web interface with **drag and drop** support
* ✅ Hosted on **Vercel** for quick deployment

---

## Requirements

* **Python 3.7+**
* **Vercel account** for deployment
* **Python libraries**:

  * Flask
  * Pillow

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/image_converter-web.git
cd image_converter-web
```

### 2. Create a virtual environment and activate it

#### For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

#### For macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

---

## Running Locally

To run the app locally, use Flask to serve the API:

#### For Windows (PowerShell):

```bash
set FLASK_APP=api/convert.py && flask run
```

#### For macOS/Linux:

```bash
FLASK_APP=api/convert.py flask run
```

After this, open `http://127.0.0.1:5000` in your browser, and you should see the **Ultimate Image Converter** interface.

---

## Vercel Deployment

1. **Install Vercel CLI** (if you don’t have it yet):

```bash
npm install -g vercel
```

2. **Login to Vercel**:

```bash
vercel login
```

3. **Deploy the app to Vercel**:

```bash
vercel
```

4. Follow the prompts to link your project, and Vercel will deploy the Flask serverless functions automatically.

5. After deployment, you can access your image converter through the provided Vercel URL.

---

## File Structure

```plaintext
image-converter-web/
│
├── api/
│   └── convert.py      # Flask serverless function to handle image conversion
├── public/
│   └── index.html      # Frontend for file upload and settings
├── requirements.txt    # Python dependencies
├── vercel.json         # Vercel configuration for Python runtime
└── README.md           # Project overview and instructions
```

---

## Troubleshooting

* **Missing dependencies**: If you run into `ModuleNotFoundError`, make sure to install all dependencies with `pip install -r requirements.txt`.
* **Vercel errors**: If the app doesn't deploy on Vercel, check the logs with `vercel logs <deployment-url>`.
* **File size issues**: Vercel has a body size limit for serverless functions. If your image is too large, you may encounter a 413 error. Consider resizing before uploading large files.

---

## License

MIT License – feel free to use, modify, and contribute to this project.

---

## Contact

If you have any questions or issues, feel free to open an issue on the [GitHub repository](https://github.com/YOUR_USERNAME/image_converter-web/issues).
