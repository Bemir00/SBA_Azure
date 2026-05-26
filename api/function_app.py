import azure.functions as func  # Core Azure Functions library
import json                      # To format the JSON response

# The FunctionApp object is the entry point (Python V2 programming model).
app = func.FunctionApp()


# HTTP-triggered endpoint. Anonymous auth so the frontend can call it for testing.
@app.route(route="CalculateArea", auth_level=func.AuthLevel.ANONYMOUS)
def CalculateArea(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Parse the JSON body sent by the frontend: {"shape": ..., "data": {...}}
        req_body = req.get_json()
        shape = req_body.get("shape")   # which geometric shape
        data = req_body.get("data")     # the dimensions for that shape

        area = 0

        if shape == "square":
            area = data["side"] ** 2
        elif shape == "rectangle":
            area = data["width"] * data["height"]
        elif shape == "circle":
            area = 3.14159 * (data["radius"] ** 2)
        elif shape == "triangle":
            area = 0.5 * data["base"] * data["height"]

        # Return the result as JSON: the bridge between backend and frontend.
        return func.HttpResponse(
            json.dumps({"area": area}),
            mimetype="application/json"
        )

    except Exception as e:
        # On bad/malformed input, return HTTP 400.
        return func.HttpResponse(
            f"Error processing request: {str(e)}",
            status_code=400
        )
