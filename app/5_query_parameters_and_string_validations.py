from fastapi import FastAPI, Query

app = FastAPI()


# its length doesn't exceed 50 characters.
@app.get("/items/")
async def read_items(q: str | None = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/")
async def read_items2(q: str | None = Query(default=None, min_length=3, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# # Add regular expressions¶
# ^: starts with the following characters, doesn't have characters before.
# fixedquery: has the exact value fixedquery.
# $: ends there, doesn't have any more characters after fixedquery.
@app.get("/items/")
async def read_items3(
    q: str | None = Query(default=None, min_length=3, max_length=50, regex="^fixedquery$")
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Default values
@app.get("/items/")
async def read_items4(q: str = Query(default="fixedquery", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Make it required¶
@app.get("/items/")
async def read_items5(q: str = Query(min_length=3)):  # not declare a default value
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# There's an alternative way to explicitly declare that a value is required. You can set the default parameter to the literal value ...
@app.get("/items/")
async def read_items6(q: str = Query(default=..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Use Pydantic's Required instead of Ellipsis (...)
from pydantic import Required


@app.get("/items/")
async def read_items7(q: str = Query(default=Required, min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Query parameter list / multiple values
# http://localhost:8000/items/?q=foo&q=bar
@app.get("/items/")
async def read_items8(q: list[str] | None = Query(default=None)):
    query_items = {"q": q}
    return query_items


# Declare more metadata
@app.get("/items/")
async def read_items9(
    q: str
    | None = Query(
        default=None,
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Alias parameters
# http://127.0.0.1:8000/items/?item-query=foobaritems
@app.get("/items/")
async def read_items10(q: str | None = Query(default=None, alias="item-query")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Deprecating parameters
@app.get("/items/")
async def read_items11(
    q: str
    | None = Query(
        default=None,
        alias="item-query",
        title="Query string",
        description="Query string for the items to search in the database that have a good match",
        min_length=3,
        max_length=50,
        regex="^fixedquery$",
        deprecated=True,  # Deprecating parameters
    )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# Exclude from OpenAPI
@app.get("/items/")
async def read_items12(hidden_query: str | None = Query(default=None, include_in_schema=False)):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}


## Recap
# Generic validations and metadata
# alias
# title
# description
# deprecated
# Validations specific for strings
# min_length
# max_length
# regex
