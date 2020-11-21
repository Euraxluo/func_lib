# DATABASE_URL="mysql://user:password@hostname/dbname?charset=utf8"
DATABASE_URL="sqlite:///components.db"+ "?check_same_thread=False"
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000
REGISTER_ROUTE = "/register"
SERVICE_ROUTE = "/service"
REGISTER_CLIENT_ROUTE = "/client"
SERVER_URL=f"http://{SERVER_HOST}:{SERVER_PORT}{REGISTER_ROUTE}{REGISTER_CLIENT_ROUTE}"