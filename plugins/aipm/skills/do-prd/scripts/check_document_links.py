"""Check handoff links against a full canonical Confluence page URL."""

import argparse
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit


def link_errors(text, canonical_url):
    canonical = urlsplit(canonical_url)
    page = re.match(r"/spaces/[^/]+/pages/\d+(?=/|$)", canonical.path)
    if canonical.scheme not in {"http", "https"} or not canonical.netloc or not page or canonical.path.rstrip("/") == page[0]:
        raise ValueError("Supply a full canonical Confluence URL, including the page title")
    errors, seen = [], False
    for raw in re.findall(r"https?://[^\s<>\"'\])]+", text):
        url = urlsplit(raw)
        if url.path.rstrip("/") == page[0] or url.path.startswith(page[0] + "/"):
            seen = True
            if (url.scheme, url.netloc, url.path) != (canonical.scheme, canonical.netloc, canonical.path):
                errors.append(f"Non-canonical page link: {raw}")
    return errors if seen else ["Canonical page link is missing from the handoff"]


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:
        canonical = "https://example.test/spaces/T/pages/123/Page+title"
        assert not link_errors(f"[Page]({canonical})", canonical)
        assert not link_errors(f"[Comment]({canonical}?focusedCommentId=456#comment-456)", canonical)
        assert link_errors("[Page](https://example.test/spaces/T/pages/123/)", canonical)
        assert link_errors(f"{canonical}\nhttps://example.test/spaces/T/pages/123/Wrong", canonical)
        assert link_errors(f"{canonical}\nhttps://wrong.test/spaces/T/pages/123/Page+title", canonical)
        assert link_errors("No page link", canonical)
        print("Link self-check passed")
    else:
        parser = argparse.ArgumentParser(description=__doc__)
        parser.add_argument("canonical_url")
        parser.add_argument("text_file", type=Path)
        args = parser.parse_args()
        errors = link_errors(args.text_file.read_text(), args.canonical_url)
        if errors:
            sys.exit("\n".join(errors))
        print("Canonical page links verified")
