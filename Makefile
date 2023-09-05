run-traefik:
	docker compose -f ./traefik/docker-compose.yml up -d --build

run-portainer:
	docker compose -f ./portainer/docker-compose.yml up -d --build

run-netdata:
	docker compose -f ./netdata/docker-compose.yml up -d --build

run-nginx:
	docker compose -f ./nginx/docker-compose.yml up -d --build

run-all: \
	run-traefik \
	run-portainer \
	run-netdata \
	run-nginx
