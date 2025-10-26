port := x"${PORT:-5432}"

setup:
	docker pull postgres:18
	docker run --name part-test -e POSTGRES_PASSWORD=test -d -p "{{port}}:5432" postgres:18
	sleep 5
	psql "postgres://postgres:test@localhost:{{port}}" -f setup.sql


clean:
	docker stop part-test
	docker rm part-test


clients:
	uv run main.py create alpha --size 100
	uv run main.py create beta --size 100
	uv run main.py create gamma --size 100
