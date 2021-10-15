# python.flask
1. 간단한 API 작성시 유리함
2. 웹서비스 미들웨어랑 같이 쓰는걸 장려 
	1. uwsg <- 연결 하니 잘 안되서 
	2. flask , ngnix만 사용했음

3. ngnix 설정 /etc/nginx/conf.d
		upstream etl_api {
			server localhost:32002;
			# server localhost:32002;
		}
		server {
			listen 32006 default_server;	
			access_log /var/log/nginx/access.log;
			error_log /var/log/nginx/error.log;		
			location / {
				proxy_pass_header Server;
				proxy_set_header Host $http_host;
				proxy_set_header X-Real-IP $remote_addr;
				proxy_set_header X-Scheme $scheme;
				proxy_pass http://etl_api;
			}
		}