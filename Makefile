build:
	docker build -t api_docker_flask:latest .
run:	build
	docker run --name=api -d -v ~/dockerlogs:/var/log -p 3000:3000 api_docker_flask:latest
