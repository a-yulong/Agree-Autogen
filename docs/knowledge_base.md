# Knowledge Base Policy

Agree-Autogen supports retrieval-augmented generation, but this repository does not bundle large external knowledge bases by default.

## Why the knowledge base is not bundled

- AGREE manuals, AADL examples, papers, PDFs, and course materials may have independent copyright or distribution terms.
- Generated vector stores are large derived artifacts and are usually not appropriate for source control.
- Reproducible research repositories commonly provide the code, configuration templates, lightweight examples, and instructions for rebuilding local indexes rather than committing private corpora or generated caches.

## Recommended layout

Place locally available and legally redistributable documents under a path such as:

```text
docs/AGREE_Users_Guide/
|-- guide.pdf
|-- syntax_notes.txt
`-- examples.txt
```

Then set:

```powershell
$env:AGREE_DOCS_DIR = "docs/AGREE_Users_Guide"
```

If a document is not redistributable, keep it outside the repository and point `AGREE_DOCS_DIR` to that local path.

## What may be committed

- Small original examples created for this project.
- Publicly redistributable documentation with a compatible license.
- Metadata that describes corpus sources, versions, and download instructions.

## What should not be committed

- Private datasets.
- API keys or service credentials.
- Generated vector stores or cache directories.
- Third-party PDFs or manuals without explicit redistribution permission.
