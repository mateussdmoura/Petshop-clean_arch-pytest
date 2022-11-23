class HttpErrors:
    """Class to define errors in http"""
    
    @staticmethod
    def error_422():
        """HTTP 422"""
        
        return {
            "status_code": 422,
            "body": {
                "error": "Unprocessable Entity"
            }
        }
    