python_sources()

pex_binary(
    name="users_app",
    entry_point="services.users.main:main",
)

docker_image(
    name="users_image",
    dependencies=[":users_app"],
    instructions=[
        "FROM python:3.12-slim",
        "WORKDIR /app",
        "COPY users_app.pex ./",
        "EXPOSE 8002",
        'ENTRYPOINT ["./users_app.pex"]',
    ],
)
