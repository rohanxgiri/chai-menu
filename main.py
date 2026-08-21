from fastapi import FastAPI

app = FastAPI(
    title="Chai Point menu API",
    description="Read only menu API for Kiosk diplays and mobile app"
)

@app.get("/")
def root():
    return {
        "message" : "Wlecome to Chai point Menu API"
    }
