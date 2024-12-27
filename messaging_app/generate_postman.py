import json

postman_collection = {
    "info": {
        "name": "Messaging App API",
        "description": "Postman collection for testing the Messaging App API endpoints.",
        "schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
    },
    "item": [
        {
            "name": "Obtain JWT Token",
            "request": {
                "method": "POST",
                "header": [
                    {"key": "Content-Type", "value": "application/json"}
                ],
                "url": {
                    "raw": "{{base_url}}/api/token/",
                    "host": ["{{base_url}}"],
                    "path": ["api", "token"],
                },
                "body": {
                    "mode": "raw",
                    "raw": '{"username": "testuser", "password": "password123"}',
                },
            },
        },
        {
            "name": "Create a Conversation",
            "request": {
                "method": "POST",
                "header": [
                    {"key": "Content-Type", "value": "application/json"},
                    {"key": "Authorization", "value": "Bearer {{jwt_token}}"},
                ],
                "url": {
                    "raw": "{{base_url}}/api-auth/conversations/",
                    "host": ["{{base_url}}"],
                    "path": ["api-auth", "conversations"],
                },
                "body": {
                    "mode": "raw",
                    "raw": '{"participants": ["<user_id_1>", "<user_id_2>"]}',
                },
            },
        },
        {
            "name": "Send a Message",
            "request": {
                "method": "POST",
                "header": [
                    {"key": "Content-Type", "value": "application/json"},
                    {"key": "Authorization", "value": "Bearer {{jwt_token}}"},
                ],
                "url": {
                    "raw": "{{base_url}}/api-auth/conversations/{{conversation_id}}/messages/",
                    "host": ["{{base_url}}"],
                    "path": [
                        "api-auth",
                        "conversations",
                        "{{conversation_id}}",
                        "messages",
                    ],
                },
                "body": {
                    "mode": "raw",
                    "raw": '{"sender": "<user_id>", "message_body": "Hello, this is a test message!"}',
                },
            },
        },
        {
            "name": "Fetch Conversations",
            "request": {
                "method": "GET",
                "header": [
                    {"key": "Authorization", "value": "Bearer {{jwt_token}}"}
                ],
                "url": {
                    "raw": "{{base_url}}/api-auth/conversations/",
                    "host": ["{{base_url}}"],
                    "path": ["api-auth", "conversations"],
                },
            },
        },
        {
            "name": "Fetch Messages in a Conversation",
            "request": {
                "method": "GET",
                "header": [
                    {"key": "Authorization", "value": "Bearer {{jwt_token}}"}
                ],
                "url": {
                    "raw": "{{base_url}}/api-auth/conversations/{{conversation_id}}/messages/",
                    "host": ["{{base_url}}"],
                    "path": [
                        "api-auth",
                        "conversations",
                        "{{conversation_id}}",
                        "messages",
                    ],
                },
                "query": [
                    {"key": "page", "value": "1"},
                    {"key": "sender", "value": ""},
                    {"key": "sent_after", "value": ""},
                ],
            },
        },
    ],
    "variable": [
        {"key": "base_url", "value": "http://localhost:8000"},
        {"key": "jwt_token", "value": ""},
        {"key": "conversation_id", "value": ""},
    ],
}

# Write the Postman collection to a JSON file
with open("messaging_app/post_man-Collections", "w") as file:
    json.dump(postman_collection, file, indent=4)

print("Postman collection file created: messaging_app/post_man-Collections")
