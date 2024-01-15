class Response:
    def read(data):
        return {
            'status_code': 200,
            'data': data
        }

    def updated(updated_id):
        return {
            'status_code': 200,
            'updated_id': updated_id,
            'msg': 'Successfully updated!'
        }

    def created(data):
        return {
            'status_code': 201,
            'data': data
        }

    def deleted(deleted_id):
        return {
            'status_code': 200,
            'deleted_id': deleted_id,
            'msg': 'Successfully deleted!'
        }