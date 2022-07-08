# LPAStore

Short for _Linux Phone Apps Store_

## Development

You can start the backend with

```
uvicorn main:app --reload
```

You can easily query the API endpoints using curl (and prettify it with jq): `curl -s localhost:8000 | jq`

### curl

You can easily query the API endpoints using curl (and prettify it with jq):

```bash
curl -s localhost:8000 | jq
```

Include the header with the status code (does not work in combination with jq):

```bash
curl -i localhost:8000
```

Make a put request:

```bash
curl -s -X 'PUT' \
  'http://localhost:8000/apps/test' \
  -H 'Content-Type: application/json' \
  -d '{
  "id": "string",
  "appdata": "string",
  "name": "string",
  "description": "string"
}' | jq
```

Hint: With zsh it is much easier to edit multi line commands than with bash

# License

This project is licensed under the [GNU AGPLv3](LICENSE).