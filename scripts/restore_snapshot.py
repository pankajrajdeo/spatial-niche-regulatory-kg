"""Restore the private Git LFS continuation snapshot without overwriting divergent files."""
import argparse
import hashlib
import json
from pathlib import Path
import tarfile
import tempfile

ROOT = Path(__file__).resolve().parents[1]

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
        with tempfile.TemporaryFile() as combined:
            for item in manifest['parts']:
                with (ROOT / item['path']).open('rb') as part:
                    while chunk := part.read(1024 * 1024):
                        combined.write(chunk)
            combined.seek(0)
            with tarfile.open(fileobj=combined, mode='r:gz') as archive:
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
