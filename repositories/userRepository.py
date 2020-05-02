import pyodbc 
from app import app
from utility.constant import*

class userRepository:

	def getUserList(pageNumber,recordsPerPage):
		response = userListResponse()
		try:
			data = []		
			conn = pyodbc.connect(app.config['CONNECTIONSTRING'])
			cursor = conn.cursor()
			sp = "exec GetUserList " + str(pageNumber) + "," + str(recordsPerPage)
			cursor.execute(sp)
			empRows = cursor.fetchall()
			for i in range(len(empRows)):
				dataDict = {
					"DisplayName": empRows[i][2],
					"LoginId": empRows[i][3],
					"FirstName": empRows[i][4],
					"MiddleName": empRows[i][5],
					"LastName": empRows[i][6],
					"PhoneNumber": empRows[i][7],
					"ManagerLoginId": empRows[i][8],
					"EmployeeId": empRows[i][9],
					"Status": empRows[i][10],
					"AdvanceSearcherGroup": empRows[i][11],
					"SkillLevel": empRows[i][12],
					"ASTEmployeeId": empRows[i][13],
					"IsASTImpersonate": empRows[i][14],
					"IsUserPreferenceAllowed": empRows[i][15],
					"IsTotalSummaryEnabled": empRows[i][16],
					"EnableAutoLoadLookupId": empRows[i][17],
					"ApprovalLevelLookupId": empRows[i][18],
					"SipAddress": empRows[i][19]
				}
				data.append(dataDict)
				response.totalUserCount = empRows[i][25]
			response.userList = data
			response.resultCode = uamErrorCodes.Success.value
			response.resultMessage = uamMessage.Success
			return response
		except Exception as e:			
			response.resultCode = uamErrorCodes.RequestFailed.value
			response.resultMessage = uamMessage.Error
		finally:
			cursor.close() 
			conn.close()
		return response

	def getUserDetail(loginId):
		response = userResponse()
		try:
			data = {}	
			conn = pyodbc.connect(app.config['CONNECTIONSTRING'])
			cursor = conn.cursor()
			sp = "exec [GetUserDetails] '" + str(loginId)+"'"
			cursor.execute(sp)
			empRows = cursor.fetchall()
			for i in range(len(empRows)):
				dataDict = {
					"AppUserId":empRows[i][0],
					"DisplayName":empRows[i][1],
					"LoginId":empRows[i][2],
					"FirstName":empRows[i][3],
					"MiddleName":empRows[i][4],
					"LastName":empRows[i][5],
					"EmployeeId":empRows[i][6],
					"Status":empRows[i][7],
					"AdvanceSearcherGroup":empRows[i][8],
					"SkillLevel":empRows[i][9],
					"ASTEmployeeId":empRows[i][10],
					"IsASTImpersonate":empRows[i][11],
					"IsUserPreferenceAllowed":empRows[i][12],
					"IsTotalSummaryEnabled":empRows[i][13],
					"EnableAutoLoadLookupId":empRows[i][14],
					"ApprovalLevelLookupId":empRows[i][15],
					"SipAddress":empRows[i][16],
					"CreatedBy":empRows[i][17],
					"CreatedTime":empRows[i][18],
					"ModifiedBy":empRows[i][19],
					"ModifiedTime":empRows[i][20],
					"EmailAddress":empRows[i][21],
					"AutoLoadEnabled":empRows[i][22]
				}
				data=dataDict
			response.userDetail = data
			response.resultCode = uamErrorCodes.Success.value
			response.resultMessage = uamMessage.Success
			return response
		except Exception as e:			
			response.resultCode = uamErrorCodes.RequestFailed.value
			response.resultMessage = uamMessage.Error
		finally:
			cursor.close() 
			conn.close()
		return response