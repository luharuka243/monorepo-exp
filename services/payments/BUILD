python_sources()

pex_binary(
    name="payments_app",
    entry_point="services.payments.main:main",
)

docker_image(
    name="payments_image",
    dependencies=[":payments_app"],
    instructions=[
        "FROM python:3.12-slim",
        "WORKDIR /app",
        "COPY payments_app.pex ./",
        "EXPOSE 8003",
        'ENTRYPOINT ["./payments_app.pex"]',
    ],
)
