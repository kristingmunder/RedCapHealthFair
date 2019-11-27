import subprocess
import DataSync as ds


def save_travis_env(key, value):
    cmd: str = f'travis env set {key} {value}'
    process = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
    print(process.stdout.decode("utf-8"))


config: dict = ds.load_config()

[save_travis_env(k, v) for k, v in config.items()]
