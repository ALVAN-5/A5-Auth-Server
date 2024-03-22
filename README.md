# A5-Auth-Server
A server to create, store, and validate session tokens

## Run With Docker

### Server Container

> `docker network create --subnet 192.168.2.0/24 al-net # This only has to be run once`

> `docker build -t a5-auth-server:0.0.0.SNAPSHOT . --build-arg A5TPS_ENV=PROD --build-arg A5TPS_HOST_IP="192.168.2.2" --build-arg A5TPS_HOST_PORT=80`

> `docker run --network=al-net --ip 192.168.2.3 -p 80:80 -p 5000:5000 a5-auth-server:0.0.0.SNAPSHOT`

### Testing Container
> `docker run -ti --network=al-net --ip 192.168.2.69 --rm ubuntu:20.04 /bin/bash`

> `apt update && apt install lsb-core # To install standard ubuntu libraries`

## Endpoints

### IP Validation

#### `auth/ip/createIPUser/` - POST
- This endpoint saves an IP address which can be used to authenticate a request.
- Returns 200 if the data was successfully entered into the database, or a matching record was found.
- The request, rather than looking at the IP address of the sender, uses a body parameter to take the client IP address. This is done because the server, in production mode, will be deployed to only take in requests from the [A5-Server](https://github.com/ALVAN-5/A5-Server) which will format the requests appropriately and safely.

| Body Parameter | Required | Description| Formating Requirements |
|----------------|----------|------------|------------------------|
|clientIP| &#9745;  |IP address of user to be saved as an authentication key|IPv4 or IPv6 string|
|home_group| &#9745;  |A key, used to associate multiple saved IP addresses to the same home.| String, 6-32 characters in length|

##### Response
| Key | Datatype | Description |
|-|-|-|
|ip_address| string | The IP address saved to the database|
|token| string | The token used to create authenticated sessions from devices with different IP addresses, or used to authenticate same device if IP address might change|
|home_group| string | The key, used to associate multiple saved IP addresses to the same home |
|already_exists| boolean | True if newly created record, False if record already was in the database |

<br/><b>
Sample Response:
</b><br/>
Status Code: 200
```JSON
{
    "ip_address": "192.168.1.113",
    "token": "l8EF}R[0RQbg_O1(LP]b(H-s",
    "home_group": "sample_home",
    "already_existed": false
}
```

<hr/><br/>

#### `auth/ip/createSession/` - POST
- This endpoint takes in an IP address and returns a 200 with a session key if the IP address is stored in the database.

| Body Parameter | Required | Description| Formating Requirements |
|----------------|----------|------------|------------------------|
|clientIP| &#9745;  |IP address of user to be saved as an authentication key|IPv4 or IPv6 string|


##### Response
| Key | Datatype | Description |
|-|-|-|
|ip_address| string | The IP address saved to the database|
|session_key | string | The session key that will be sent back to the user and used to validate requests |
|expiration | string | The timestamp of the session key's expiration |

<br/><b>
Sample Response:
</b><br/>
Status Code: 200
```JSON
{
    "ip_address": "192.168.1.113",
    "session_key": "S2JUTDSIASLMAXWX86BQKK9CDFVD988G2IHYU5DDDPJCPBMMVC5MFQQNRTYAL5YT",
    "expiration": "2025-03-13 03:04:55.973239+00:00"
}
```

<hr/><br/>

#### `auth/ip/createSession/token/` - POST
- This endpoint takes in a the token associated with an IP address and returns a 200 with a session key if the token is stored and associated with an IP in the database.

| Body Parameter | Required | Description| Formating Requirements |
|----------------|----------|------------|------------------------|
|token| &#9745;  |The token associated to a saved IP|string|


##### Response
| Key | Datatype | Description |
|-|-|-|
|ip_address| string | The IP address saved to the database|
|session_key | string | The session key that will be sent back to the user and used to validate requests |
|expiration | string | The timestamp of the session key's expiration |

<br/><b>
Sample Response:
</b><br/>
Status Code: 200
```JSON
{
    "ip_address": "192.168.1.113",
    "session_key": "S2JUTDSIASLMAXWX86BQKK9CDFVD988G2IHYU5DDDPJCPBMMVC5MFQQNRTYAL5YT",
    "expiration": "2025-03-13 03:04:55.973239+00:00"
}
```

<hr/><br/>

#### `auth/ip/validateSession/<session_key>/` - GET
- This endpoint takes in a session key as a path parameter and validates that it is in the database and not expired

| Path Parameter | Required | Description| Formating Requirements |
|----------------|----------|------------|------------------------|
|session| &#9745;  |The session key to be authenticated|string|


##### Response
| Key | Datatype | Description |
|-|-|-|
|ip_address| string | The IP address saved to the database|
|session_key | string | The validated session key, or an empty string if the session key was not valid |

<br/><b>
Sample Response:
</b><br/>
Status Code: 200
```JSON
{
    "session_key": "S2JUTDSIASLMAXWX86BQKK9CDFVD988G2IHYU5DDDPJCPBMMVC5MFQQNRTYAL5YT",
}
```

<hr/><br/>

#### `auth/ip/resetIPToken/` - POST
- This endpoint takes in a clientIP and a home_group pair. It uses the provided data to reset the token on the matching IPUser, if one is found.

| Body Parameter | Required | Description| Formating Requirements |
|----------------|----------|------------|------------------------|
|clientIP| &#9745;  |IP address of user to be identify the IP user to reset|IPv4 or IPv6 string|
|home_group| &#9745;  |Extra data for security validation| String, 6-32 characters in length|


##### Response
| Key | Datatype | Description |
|-|-|-|
|ip_address| string | The IP address saved to the database|
|token| string | The updated token used to create authenticated sessions from devices with different IP addresses, or used to authenticate same device if IP address might change|
|home_group| string | The key, used to associate multiple saved IP addresses to the same home |

<br/><b>
Sample Response:
</b><br/>
Status Code: 200
```JSON
{
    "ip_address": "192.168.1.113",
    "token": "l8EF}R[0RQbg_O1(LP]b(H-s",
    "home_group": "sample_home",
    "already_existed": false
}
```

<hr/><br/>

#### `auth/ip/removeIPUser/` - POST
- This endpoint removes an IPUser from the database. All associated sessions will be removed as well.

| Body Parameter | Required | Description| Formating Requirements |
|----------------|----------|------------|------------------------|
|clientIP| &#9745;  |IP address of user to be identify the IP user to reset|IPv4 or IPv6 string|


##### Response
| Key | Datatype | Description |
|-|-|-|
|ip_address| string | The IP address saved to the database of the deleted IPUser|
|token| string | The token used to create authenticated sessions from devices with different IP addresses of the deleted IPUser|
|home_group| string | The key, used to associate multiple saved IP addresses to the same home of the deleted IPUser |

<br/><b>
Sample Response:
</b><br/>
Status Code: 200
```JSON
{
    "ip_address": "192.168.1.113",
    "token": "l8EF}R[0RQbg_O1(LP]b(H-s",
    "home_group": "sample_home"
}
```

<hr/><br/>

#### `health/` - GET
- This endpoint just exists to check the health of the server.
- If the server is alive, the following is returned:
```JSON
{
    "health": "ok"
}
```
- Otherwise, an error status code will return

##### Parameters
- None

##### Response
| Key | Datatype | Description |
|-|-|-|
|health| string | "ok" |
