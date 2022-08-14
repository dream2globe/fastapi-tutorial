from fastapi import FastAPI, Path, Query

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    item_id: int = Path(title="The ID of the item to get"),  # metadata
    q: str | None = Query(default=None, alias="item-query"),
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# Order the parameters as you need
@app.get("/items/{item_id}")
async def read_items2(
    q: str, item_id: int = Path(title="The ID of the item to get")
):  # it doesn't care about the order.
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get("/items/{item_id}")
async def read_items3(
    *, item_id: int = Path(title="The ID of the item to get"), q: str
):  # trick (kwargs)
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# Number validations: greater than and less than or equal
@app.get("/items/{item_id}")
async def read_items4(
    *,
    item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
    q: str,
    size: float = Query(gt=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# Recap
# With Query, Path (and others you haven't seen yet)
# you can declare metadata and string validations in the same ways as with Query Parameters and String Validations.

# And you can also declare numeric validations:

# gt: greater than
# ge: greater than or equal
# lt: less than
# le: less than or equal
