from rest_framework.exceptions import APIException


class ProfileNotFound(APIException):
    """Custom exception for profile not found"""
    status_code = 404
    default_detail = "The requested profile does not exist"


class NotYourProfile(APIException):
    """Custom exception for another user's profile"""
    status_code = 403
    default_detail = "You can't edit a profile that doesn't being to you"
