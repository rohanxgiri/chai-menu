from fastapi import FastAPI, Query, HTTPException
from models import MenuItem, MenuResponse
from data import menu_items

app = FastAPI(
    title="Chai Point menu API",
    description="Read only menu API for Kiosk diplays and mobile app",
)


@app.get("/")
def root():
    return {"message": "Wlecome to Chai point Menu API"}


"""category
   ↓
comes from the URL query parameter

str | None
   ↓
can either be a string or None

Query(None, ...)
   ↓
the parameter is optional

description="..."
   ↓
shows this explanation in Swagger docs
"""

"""
filterd = [item for item in menu_items if item["category"] == category.lower()]
#          ^^^^   ^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#          |      |                      |
#          |      |                      condition — only keep items where this is True
#          |      loop over every item in menu_items
#          what to put in the new list (the item itself, unchanged)

"""


@app.get("/menu", response_model=MenuResponse)
def get_menu(
    category: str | None = Query(None, description="Filter by chai, snack or combo")
):
    if category:
        filterd = [item for item in menu_items if item["category"] == category.lower()]
        if not filterd:
            raise HTTPException(
                status_code=404, detail=f"No item found category: {category}"
            )
        return MenuResponse(count=len(filterd), items=filterd)
    
    return MenuResponse(count=len(menu_items), items=menu_items)

@app.get("/menu/{item_id}", response_model=MenuItem)
def get_item(item_id: int):
    for item in menu_items:
        if item["id"] == item_id:
            return item

    raise HTTPException(
        status_code=404, detail=f"Menu item with id {item_id} not found"
    )
