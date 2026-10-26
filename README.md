# PAKRAM — Psychology, Cognition, Emotion & Brain

Bilingual (English / Hebrew) website for the **PAKRAM** research M.A. division
(פסיכולוגיה, קוגניציה, רגש ומוח) of the Department of Psychology, Bar-Ilan University.

Official track page: https://psychology.biu.ac.il/tracks/2189

## Structure

| Path | What it is |
| --- | --- |
| `index.html` | English page (generated) |
| `he/index.html` | Hebrew page, right-to-left (generated) |
| `assets/style.css`, `assets/site.js`, `assets/favicon.svg` | Styles, small script, icon |
| `build/content.py` | **All site copy, in both languages.** Edit this file. |
| `build/build.py` | Generator that writes the two HTML pages |

## Editing the site

1. Edit the text in `build/content.py` (`EN` and `HE` dictionaries, `FACULTY_BASE`,
   `FACULTY_TEXT`, and the reading lists).
2. Regenerate the pages:

   ```bash
   python3 build/build.py
   ```

3. Commit and push. GitHub Pages serves the committed HTML directly
   (`.nojekyll` disables Jekyll processing).

No dependencies beyond Python 3 are needed. Fonts load from Google Fonts.

## Local preview

```bash
python3 -m http.server 8765
```

Then open http://127.0.0.1:8765/ (English) or http://127.0.0.1:8765/he/ (Hebrew).
