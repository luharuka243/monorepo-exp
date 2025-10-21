 # Monorepo FastAPI Services with Pants

 This repository contains three example FastAPI services managed by Pants, plus a shared common library.

 ## Directory Layout

 ```
 services/
   orders/
   users/
   payments/
 common/
 ```

 - Each service is a FastAPI app in its own `services/<name>` directory.
 - Shared Python code lives under `common/`.

 ## Dependencies & Lockfile

 Third-party requirements are declared in `requirements.txt`. To generate the lockfile run:

 ```bash
 ./pants generate-lockfiles
 ```

 ## Running a Service

### Running a Service Locally

To run a service via Pants (for development), use:

```bash
./pants run services/orders:orders_app
./pants run services/users:users_app
./pants run services/payments:payments_app
```

## Building Docker Images

Each service provides a Docker image target. To build the images:

```bash
./pants package services/orders:orders_image
./pants package services/users:users_image
./pants package services/payments:payments_image
```

You can then run the built images with Docker, mapping their ports:

```bash
docker run -p 8001:8001 orders_image:latest
docker run -p 8002:8002 users_image:latest
docker run -p 8003:8003 payments_image:latest
```