python_sources()

pex_binary(
    name="orders_app",
    entry_point="services.orders.main:main",
)

docker_image(
    name="orders_image",
    dependencies=[":orders_app"],
    instructions=[
        "FROM python:3.12-slim",
        "WORKDIR /app",
        "COPY services.orders/orders_app.pex ./orders_app.pex",
        "EXPOSE 8001",
        'ENTRYPOINT ["./orders_app.pex"]',
    ],
)
