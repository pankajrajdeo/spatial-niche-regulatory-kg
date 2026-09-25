"""Restore the private Git LFS continuation snapshot without overwriting divergent files."""
import argparse
from contextlib import contextmanager
import hashlib
import io
import json
from pathlib import Path
import tarfile

ROOT = Path(__file__).resolve().parents[1]

@contextmanager
def joined_parts(paths):
    """Stream verified chunks without allocating a second multi-GB archive."""
    class PartsReader(io.RawIOBase):
        def __init__(self):
            self.paths = iter(paths)
            self.current = None

        def read(self, size=-1):
            if size < 0:
                raise ValueError('Streaming reader requires a bounded read')
            chunks = []
            remaining = size
            while remaining:
                if self.current is None:
                    path = next(self.paths, None)
                    if path is None:
                        break
                    self.current = path.open('rb')
                chunk = self.current.read(remaining)
                if not chunk:
                    self.current.close()
                    self.current = None
                    continue
                chunks.append(chunk)
                remaining -= len(chunk)
            return b''.join(chunks)

    stream = PartsReader()
    try:
        yield stream
    finally:
        if stream.current is not None:
            stream.current.close()

def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--verify-only', action='store_true')
    args = parser.parse_args()
    manifest = json.loads((ROOT / 'transfer/snapshot.json').read_text())
    if not args.verify_only:
        for item in manifest['parts']:
            path = ROOT / item['path']
            if not path.is_file() or path.stat().st_size != item['bytes'] or digest(path) != item['sha256']:
                raise SystemExit(f"Missing/invalid LFS part: {path.name}; run git lfs pull")
        for item in manifest['files']:
            path = ROOT / item['path']
            if path.exists() and (not path.is_file() or digest(path) != item['sha256']):
                raise SystemExit(f"Existing divergent file: {item['path']}; preserve/move it before restore")
        with joined_parts([ROOT / item['path'] for item in manifest['parts']]) as combined:
            with tarfile.open(fileobj=combined, mode='r|gz') as archive:
                allowed = {item['path'] for item in manifest['files']}
                for member in archive:
                    if not member.isfile() or member.name not in allowed:
                        raise SystemExit(f'Unexpected archive member: {member.name}')
                    archive.extract(member, ROOT, filter='data')
    missing = []
    for item in manifest['files']:
        path = ROOT / item['path']
        if not path.is_file() or path.stat().st_size != item['bytes'] or digest(path) != item['sha256']:
            missing.append(item['path'])
    if missing:
        raise SystemExit(f'Snapshot verification failed for {len(missing)} files; first: {missing[:5]}')
    print(f"Verified {len(manifest['files'])} snapshot files.")

if __name__ == '__main__':
    main()
