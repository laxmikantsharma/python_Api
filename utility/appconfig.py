from app import app

app.config.update(
		DEVELOPMENT=True,
        ENV = "",
        DEBUG = True,
		CONNECTIONSTRING='Driver={SQL Server};Server=AINDLPC0JCZ4Q;Database=UserAccessManagement;Trusted_Connection=yes;',
)
