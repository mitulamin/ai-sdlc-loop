# guides

Plain-language guides to the principles. The guides are in [developer/](developer/README.md), and `scripts/build-site.py` publishes each one as a page under `docs/guides/developer/`.

Writing a guide:

- The first `#` heading is the page title and the label in the guides listing. The listing follows the order of the links in `developer/README.md`.
- Link to another guide by its file name, such as `quality-principles.md`.
- Link to a site page by its file under `docs/`, such as `../../docs/agents.html` or `../../docs/principles/4.1.html`. The link works on GitHub, and the site build rewrites it to the site-relative link (`../../agents.html`). Any other repo path becomes a GitHub link.
- Headings get the same ids as on GitHub, so `#section` links work in both places.
- The renderer supports headings, paragraphs, one-line list items, tables, fenced code, inline code, bold, italic and links. Write a callout as a paragraph that starts with a bold lead, such as `**Lead.** Body`; there are no blockquotes, diagrams or raw HTML.
- A guide whose text contains the words "coming later" is shown as a stub. The build fails on a `cursor.com/canvas` link.
