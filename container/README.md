Build the general worker image from the repository root:

    docker build -t cairn-general-worker:local container

The image uses an unprivileged Node user and a minimal Python/Git environment. No Kali or offensive toolkits are installed. Supply model configuration via the dispatcher. Prefer bridge networking.
