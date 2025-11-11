# world_version is defined in archipelago.json manifest file
minimum_client_version = "0.10.0"
client_version = "0.10.0"
minimum_world_version = "0.10.0"
minimum_mod_version = "0.10.0"

def is_version_valid(version: str, minimum_version: str) -> bool:
    return tuple(map(int, version.split('.'))) >= tuple(map(int, minimum_version.split('.')))
