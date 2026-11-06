# Practice App: A RealWorld API

**Status:** Draft · **Owner:** CoE Team · **Last updated:** 2026-11-06 · **Next review:** 2027-02-06

Every back-end path in the academy builds the same app: the API for **RealWorld**, an open-source Medium-style
blogging app also called Conduit. You build it stage by stage in your stack, and RealWorld's own API tests check it
the same way for everyone.

## Why This App

- **It is a real API.** Sign-up, sign-in, articles, comments, tags, profiles, following, favourites, feeds and
  pagination cover most of what client APIs do.
- **The contract is fixed.** One API specification means you spend your time on back-end skills, not on deciding
  what to build.
- **It is tested for you.** A shared set of API tests sends 157 requests and checks every response, including the
  error cases.
- **It pairs with any front end.** Every RealWorld front end calls the same API, including one you build in a
  [front-end path](../02-frontend/README.md).

## Key Details

| Detail | Value |
|--------|-------|
| Repository | [realworld-apps/realworld](https://github.com/realworld-apps/realworld), MIT licence |
| API specification | `specs/api/openapi.yml` in the repository: every endpoint, request and response |
| API tests | 13 [Hurl](https://hurl.dev) files in `specs/api/hurl`, run by `specs/api/run-api-tests-hurl.sh` |
| Header for signed-in requests | `Authorization: Token <token>`. The token can be any string your API can check; it does not have to be a JWT. |
| Error format | `{"errors": {"<field>": ["<message>"]}}`, with 422 for validation errors and 409 for a username or email that is already taken |
| Other status codes the tests check | 200, 201, 204, 401, 403 and 404 |

## Setting Up

1. Create a repository for your practice work, as agreed with your lead, and give your reviewer write access.
2. Clone the [RealWorld repository](https://github.com/realworld-apps/realworld) next to it. You need the API
   specification and the tests from it.
3. Install [Hurl](https://hurl.dev/docs/installation.html). On Windows, run the test script from Git Bash or WSL.
4. Read `specs/api/openapi.yml` before you write any code. Every endpoint, field name and status code it lists must
   match your API, or the tests fail.

## Running the API Tests

From `specs/api` in the RealWorld repository, run:

```bash
HOST=http://localhost:8000 ./run-api-tests-hurl.sh
```

- Replace 8000 with the port your API runs on.
- Set `HOST` to your server's address **without** `/api`. The test files add `/api` to every path themselves.
- Each run creates new users with a unique suffix, so you can run the tests again without resetting the database.
- To run one file while you work on a feature, pass it to the script, for example
  `./run-api-tests-hurl.sh hurl/auth.hurl`.

When you report results, show how many files and requests passed and failed. A file that did not run is not a pass.

## Details the Tests Check

The tests check some details that are easy to miss. Read `openapi.yml` and the Hurl files for the full contract.

| Detail | What the tests expect |
|--------|-----------------------|
| Error bodies | Exact messages, such as `errors.token` `is missing` for a missing token, `errors.credentials` `invalid` for a failed sign-in, `errors.article` `forbidden` or `not found`, and `can't be blank` for an empty required field |
| Request headers | The tests send JSON but no `Accept` header, so the API must answer in JSON for every `/api` path regardless |
| Status codes | Sign-up, creating an article and adding a comment return 201. Sign-in, follow, unfollow, favourite and unfavourite return 200 with a body. Deleting an article or comment returns 204. |
| `/api/articles/feed` | Must not be read as an article slug. Signed out, it returns 401. |
| `updatedAt` | Must change when an article is updated, even within the same second as its creation, so store timestamps with fractions of a second |
| Sign-up volume | One run signs up 22 users from one address within seconds, so rate limits must allow a full run |

## Practice-Only Parts of the Contract

Three parts of the RealWorld contract differ from Techversant's rules for client work. Follow RealWorld in your
practice app, so the tests pass, and follow Techversant on client projects:

- **The error format.** Techversant APIs use the
  [standard error response format](../../../standards/general/rest-api-best-practices.md#52-error-response-format)
  from the REST API best practices.
- **The `Token` header and the token itself.** Client APIs use the standard `Authorization: Bearer <token>` header,
  or, for a Techversant front end, a session cookie. Sign-in code is Red Zone work: write it by hand, and have a
  senior engineer review it.
- **No version in the paths.** Techversant APIs put the version in the URL, as the
  [versioning strategy](../../../standards/general/rest-api-best-practices.md#21-versioning-strategy-mandatory)
  requires.

Use the app for practice only. Do not deploy it with real users' data, and do not copy its code into client work.

## Paths That Use It

- [PHP and Laravel](./laravel/README.md)
