import logging
import datetime
import json
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # name = req.params.get('name')
    # if not name:
    #     try:
    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')


    if req.method == "GET":
        d = datetime.datetime.today().strftime('%Y-%m-%d')
        func.HttpResponse.mimetype = 'application/json'
        func.HttpResponse.charset = 'utf-8'
        return func.HttpResponse(
            body=json.dumps({'text': f"Hello from the API. Todays date is {d}"}),
            mimetype="application/json",
            status_code=200
        )
    else:  # POST
        return func.HttpResponse("Bad request. Only GET allowed.", status_code=400)
