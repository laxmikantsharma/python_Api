from app import app
from enum import Enum
import datetime

class uamErrorCodes(Enum):
    SystemError = 10400
    Unknown = 10300
    Success = 10601
    RequestFailed = 10501
    ValidationFailed = 10502
    MandatoryField = 10503
    AppNameMandatory = 10504
    SecretKeyMandatory = 10505
    LoginIdMandatory = 10506
    NoResultFound = 10507
    EmployeeIdInvalid = 10508
    AstEmployeeIdInvalid = 10509
    AstEmployeeIdMandatory = 10510
    SkillLevelMandatory = 10511
    SpsSipAddressInvalid = 105012
    SaveFailed = 10513
    AccessDenied = 10514
    InvalidAppKey = 10515
    GroupNameMandatory = 10516
    InvalidUser = 10517
    AccessAccountIdMandatory = 10518

class uamMessage:
    Success = "The Web Service processed successfully." 
    Error = "Request failed." 

class baseResponse:
    resultCode=""
    resultMessage=""       
    errorCollection = []

class userListResponse(baseResponse):
    userList = []
    totalUserCount=0

class userResponse(baseResponse):
    userDetail = {}

def datetimeCheck(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
