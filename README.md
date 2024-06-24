# API Documentation

## Overview
This API provides an endpoint to search for Wikipedia pages and retrieve image information.

## Endpoints

### Wikipedia Image Search Endpoint
- **URL**: `/api/v1`
- **Method**: `GET`
- **Description**: Searches for a Wikipedia page by title and retrieves the title and thumbnail image URL.
- **Query Parameters**:
  - `query` (str): The search query for the Wikipedia page title.
- **Response**:
  - **Status Code**: `200 OK`
  - **Content**: A JSON object containing the title and image URL of the first search result.

#### Example Request
```http
GET /api/v1?query=Python
```

#### Example Response
```json
{
  "title": "Python",
  "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png"
}
```
