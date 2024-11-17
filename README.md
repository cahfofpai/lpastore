# LPAStore
Short for _Linux Phone App Store_
 
This repo contains the prototype for an app store for (GNU/)Linux phones. Apps can be added and browsed using the web interface. App entries are stored as JSON files on the server.

Technologies used:
* frontend
  * Svelte
  * Routify
  * Svelte Materialify
* backend
  * FastAPI

For all dependencies, see `package.json` and `requirements.txt`.

## Configuration

The app store can be configured using `config_backend.ini` for the backend and `config_frontend.js` for the frontend.

## Screenshots
*The app descriptions in the screenshots are quotes from the respective app repositories / websites. The urls of the source of the quotes is not visible in some screenshots because the text area does not display all text at the same time.*

Start page

![Start page](screenshots/1%20start%20page.png)

App list

![App list](screenshots/2%20app%20list.png)

App details

![App details](screenshots/3%20app%20details.png)

Add and edit app entry

<img alt="Add app entry" src="screenshots/4 add app entry.png" width="49%" >
<img alt="Edit app entry" src="screenshots/5 edit app entry.png" width="49%" >

Mobile

<img alt="Mobile start page" src="screenshots/6 mobile start page.png" width="24%" >
<img alt="Mobile app list" src="screenshots/7 mobile app list.png" width="24%" >
<img alt="Mobile app details" src="screenshots/8 mobile app details.png" width="24%" >
<img alt="Mobile edit app entry" src="screenshots/9 mobile edit app entry.png" width="24%" >

## Development
 
If you use a distribution which has `python3` instead of `python`, you have to ensure that Python 3 is also available as `python`.

Set up the dev environment

```bash
npm run setup
```

Start the backend and frontend

```bash
npm run dev
```

Then the application is available:

-   frontend: <http://localhost:3000>
-   backend: <http://localhost:8000>
    -   Swagger UI: <http://localhost:8000/docs>
    -   ReDoc: <http://localhost:8000/redoc>
    -   openapi.json: <http://localhost:8000/openapi.json>

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