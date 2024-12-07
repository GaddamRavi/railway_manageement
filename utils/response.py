def success_response(data, message="Success", status=200):
    return {
        "status": "success",
        "message": message,
        "data": data
    }, status

def error_response(message="An error occurred", status=400):
    return {
        "status": "error",
        "message": message
    }, status
