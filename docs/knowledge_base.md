# Knowledge Base Policy

Agree-Autogen supports retrieval-augmented generation. External knowledge bases are configured as local resources so that each experiment can use an explicitly controlled corpus.

## Bundling policy

- Keep API keys, generated vector stores, and private corpora outside the repository.
- Commit only documents, examples, and metadata that are owned by the project or explicitly redistributable.
- Record corpus sources and versions when preparing reproducible experiment releases.

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
