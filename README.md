**Temporal for Workflows**

1. Temporal Server als Docker starten:

```bash
sudo docker run --rm \
  --name temporal-dev \
  -p 7233:7233 \
  -p 8233:8233 \
  temporalio/temporal:latest \
  server start-dev --ip 0.0.0.0
```

2. mit uv den Worker starten:

```bash
uv run worker.py
```

3. mit uv die main starten:

```bash
uv run main.py
```

4. Temporal's Dashboard aufrufen:
```bash
curl http://localhost:8233
```