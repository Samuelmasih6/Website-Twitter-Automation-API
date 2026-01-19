# Website → Twitter Automation API

**Version:** 1.0  

This API receives new post data from your website, formats it according to Twitter constraints, and automatically publishes it on Twitter.

## Features
- Secure API key authentication
- Background (non-blocking) Twitter posting
- Automatic content formatting (280 characters)
- Swagger UI for testing
- Clean, scalable FastAPI architecture

##System Architecture
Website Backend
↓ (POST JSON + API KEY)
FastAPI Ingestion API
↓
Formatter Service
↓
Twitter API


## Authentication

This API uses **header-based API key authentication**.

### Header
X-API-KEY


**Ingest Website Post** (Main Endpoint)

POST /ingest/post

Receives a new post from your website, formats it for Twitter, and posts it asynchronously.

Request Headers
Header 	      Required	  Description
X-API-KEY	    Yes	        Internal API authentication key
Content-Type	Yes	        application/json

Request Body
{
  "post_id": "string",
  "title": "string",
  "body": "string",
  "author": "string (optional)",
  "tags": ["string"],
  "url": "string (optional)"
}

Field Description
Field	      Required	Description
post_id	    Yes      	Unique ID from your website
title      	Yes	      Post title
body	      Yes	      Main post content
author	    No	      Author name
tags	      No	      Converted to hashtags (max 3)
url	        No	      Link to full post

Example Request
POST /ingest/post HTTP/1.1
Content-Type: application/json
X-API-KEY: super-secret-key-123

{
  "post_id": "42",
  "title": "FastAPI Automation",
  "body": "This post was created on our website and automatically shared on Twitter.",
  "author": "Samuel",
  "tags": ["fastapi", "python", "automation"],
  "url": "https://yourwebsite.com/posts/42"
}

Success Response
200 OK
{
  "status": "accepted",
  "post_id": "42"
}
The post has been accepted and queued for Twitter posting.

Error Responses
401 Unauthorized
{
  "detail": "Invalid API Key"
}
Causes:
-Missing API key
-Incorrect API key

422 Validation Error
{
  "detail": [
    {
      "loc": ["body", "title"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
Cause
Required fields missing or invalid data


**Twitter Formatting Rules**
Max 280 characters
Uses up to 3 hashtags
Appends URL if provided

Example Tweet
FastAPI Automation

This post was created on our website and automatically shared on Twitter...

#fastapi #python #automation
https://yourwebsite.com/posts/42

Background Processing
-Twitter posting happens asynchronously
-API response is immediate
-Prevents request timeouts
-Scales safely

Security Notes
-API key stored in .env
-Twitter credentials never exposed
-Do NOT call this API directly from frontend JavaScript

Recommended
-Call API from backend only
-Rotate API keys periodically
-Use HTTPS in production

Testing
Swagger UI
http://127.0.0.1:8000/docs

Steps:
1.Open POST /ingest/post
2.Click Try it out
3.Enter x-api-key
4.Provide request body
5.Click Execute

Environment Variables
TWITTER_API_KEY=xxxx
TWITTER_API_SECRET=xxxx
TWITTER_ACCESS_TOKEN=xxxx
TWITTER_ACCESS_SECRET=xxxx
INTERNAL_API_KEY=super-secret-key-123

Running the API
uvicorn app.main:app --reload
