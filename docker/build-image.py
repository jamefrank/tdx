from pathlib import Path
import docker
from setuptools_scm import get_version

CURRENT_DIR = Path(__file__).parent.parent
CURRENT_DIR = str(CURRENT_DIR)

print("current dir:", CURRENT_DIR)

NAME = "tdx-tools"
VERSION = get_version(root='..', relative_to=__file__).split('+')[0]
IMAGE = f"{NAME}:{VERSION}"


def main():
    print(f"Building image {IMAGE}")
    client = docker.from_env()
    build_output = client.api.build(path=CURRENT_DIR, dockerfile='docker/Dockerfile', tag=IMAGE, rm=True)
    for line in build_output:
        if 'stream' in line.decode('utf-8'):
            print(line.decode('utf-8'), end='')


if __name__ == '__main__':
    main()
