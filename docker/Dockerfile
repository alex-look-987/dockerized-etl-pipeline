# Use a python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-trixie-slim

# Set up a non-root user
RUN groupadd --system --gid 999 nonroot \
    && useradd --system --gid 999 --uid 999 --create-home nonroot

# Install the project int /app
WORKDIR /app

# Keeps python from buffering stdout and stderr to avoid situations where
# the application crashed without emitting any logs due to buffering
# Enable bytecode compilation
# Copy from the cache isntead of linking since it's mounted volume
# Omit development dependencies
# Ensure installed tools can be execute out of the box

ENV PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_NO_DEV=1

# Install the project's dependencies using the lockfile and settings
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

# Then, add the rest of the project source code and install it
# Installing separately from its dependencies allows optima layer caching

# uv necesita ver el proyecto en /app para que `uv run` no avise "outside of a project"
COPY --chown=nonroot:nonroot pyproject.toml uv.lock ./

COPY --chown=nonroot:nonroot src/ ./src/
COPY --chown=nonroot:nonroot data/ ./data/

# RUN --mount=type=cache,target=/root/.cache/uv

# Place executables in the environment at the fron of the path
ENV PATH="/app/.venv/bin:$PATH"

# Reset the entrypoint, don't invoke 'uv'
ENTRYPOINT []

USER nonroot

# Use the non-root user to tun our application
CMD ["uv",  "run", "--no-sync" ,"src/test.py"]   
