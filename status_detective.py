import requests


def get_category(status_code):
    if 200 <= status_code < 300:
        return "Success"
    elif 400 <= status_code < 500:
        return "Client Error"
    elif 500 <= status_code < 600:
        return "Server Error"
    else:
        return "Other"


def get_description(status_code):
    descriptions = {
        200: "Request succeeded — resource returned",
        201: "Resource created successfully",
        204: "Request succeeded — no content returned",
        400: "Bad request",
        401: "Authentication required",
        403: "Permission denied",
        404: "Resource not found",
        405: "HTTP method not allowed",
        422: "Data validation failed",
        429: "Too many requests",
        500: "Internal server error",
        503: "Service unavailable",
    }

    return descriptions.get(status_code, "Unknown status code")


def print_report(method, uri, response):
    category = get_category(response.status_code)
    description = get_description(response.status_code)

    print(f"{method} {uri}")
    print(f"  Status: {response.status_code} ({category})")
    print(f"  Description: {description}")
    print()


BASE_URL = "https://jsonplaceholder.typicode.com"


# 1. GET /posts/1
response = requests.get(f"{BASE_URL}/posts/1")
print_report("GET", "/posts/1", response)


# 2. GET /posts/99999
response = requests.get(f"{BASE_URL}/posts/99999")
print_report("GET", "/posts/99999", response)


# 3. POST /posts
new_post = {
    "title": "My New Post",
    "body": "This is a test post",
    "userId": 1
}

response = requests.post(
    f"{BASE_URL}/posts",
    json=new_post
)

print_report("POST", "/posts", response)


# 4. DELETE /posts/1
response = requests.delete(f"{BASE_URL}/posts/1")
print_report("DELETE", "/posts/1", response)


# 5. GET /invalidendpoint
response = requests.get(f"{BASE_URL}/invalidendpoint")
print_report("GET", "/invalidendpoint", response)


# 6. GET /users/1/todos
response = requests.get(f"{BASE_URL}/users/1/todos")
print_report("GET", "/users/1/todos", response)

def check_status(url, method="GET", data=None):
    method = method.upper()

    if method == "GET":
        response = requests.get(url)

    elif method == "POST":
        response = requests.post(url, json=data)

    elif method == "DELETE":
        response = requests.delete(url)

    else:
        return "Method not supported"

    category = get_category(response.status_code)
    description = get_description(response.status_code)

    return (
        f"{method} {url}\n"
        f"Status: {response.status_code} ({category})\n"
        f"Description: {description}"
    )