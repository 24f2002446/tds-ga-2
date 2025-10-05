from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json
import math

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


class Data(BaseModel):
    regions: list[str]
    threshold_ms: int


def get_p95_lat(all_lats):
    index = (len(all_lats) - 1) * 0.95
    if index.is_integer():
        return all_lats[int(index)]
    else:
        lower_value = all_lats[int(math.floor(index))]
        upper_value = all_lats[int(math.ceil(index))]
        return lower_value + (upper_value - lower_value) * (
            index - int(math.floor(index))
        )


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/post")
async def post(data: Data):
    item = data.model_dump()

    with open("data.json", "r") as f:
        regions_data = json.load(f)

    result = []
    for region in item.get("regions"):
        matches = [obj for obj in regions_data if obj.get("region") == region]
        matches.sort(key=lambda x: x.get("latency_ms"))

        avg_latency = sum([obj.get("latency_ms") for obj in matches]) / len(matches)
        p95_latency = get_p95_lat(
            list(map(lambda x: x.get("latency_ms"), list(matches)))
        )
        avg_uptime = sum([obj.get("uptime_pct") for obj in matches]) / len(matches)
        breaches = len(
            [obj for obj in matches if obj.get("latency_ms") > item.get("threshold_ms")]
        )

        res = {
            "region": region,
            "avg_latency": avg_latency,
            "p95_latency": p95_latency,
            "avg_uptime": avg_uptime,
            "breaches": breaches,
        }
        result.append(res)

    return result
