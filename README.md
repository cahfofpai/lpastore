# LPAStore

Short for _Linux Phone App Store_

## Development

Set up the dev environment

```bash
npm run setup
```

Start the backend and frontend

```bash
npm run dev
```

### Test the API

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