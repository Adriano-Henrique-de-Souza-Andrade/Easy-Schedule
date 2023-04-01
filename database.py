from sqlalchemy import create_engine, text

db_connection_string = "mysql+pymysql://zqghdq1xlwsdlkyrj1nq:pscale_pw_fnTtNLxbWnrV79oZZLNUmWX1neJvCXRW7pN9PCOEpP9@aws.connect.psdb.cloud/mps_agenda?charset=utf8mb4"

engine = create_engine(
	db_connection_string,
	connect_args={
		"ssl": {
			"ssl_ca": "/etc/ssl/cert.pen"
		}
	})

with engine.connect() as conn:
	result = conn.execute(text("select * from agenda_usuario"))
	print(result.all())