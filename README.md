# Static Site Generator

![GitHub License](https://img.shields.io/github/license/ellisf09/static-site-generator)
![GitHub last commit](https://img.shields.io/github/last-commit/ellisf09/static-site-generator)

<img src="https://skillicons.dev/icons?i=py,html">

A custom static site generator built from scratch in Python that converts raw Markdown files and static assets into a complete, styled HTML website.



## ✨ Features
- **Markdown Parsing:** Converts block-level and inline Markdown syntax (headings, lists, code blocks, links, images, bold/italics) into semantic HTML.
- **Template Injection:** Injects generated HTML content dynamically into a base `template.html` layout.
- **Asset Management:** Automatically copies static stylesheets and images from `static/` into the public build directory.

## 📂 Project Structure
- `content/` – Source Markdown (`.md`) pages
- `static/` – CSS stylesheets, images, and static assets
- `src/` – Core Python parsing and HTML node generation logic
- `docs/` – Compiled output directory ready for deployment

## 🚀 Usage
**Run locally:**
```bash
./main.sh
```

**Build for production:**
```bash
./build.sh
```

**Run unit tests:**
```bash
./test.sh
```
