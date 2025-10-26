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
	uv run main.py create alpha --size 100000
	uv run main.py create beta --size 100000
	uv run main.py create gamma --size 100000
	uv run main.py create delta --size 100000
	uv run main.py create epsilon --size 100000
	uv run main.py create zeta --size 100000
	uv run main.py create eta --size 100000
	uv run main.py create theta --size 100000
	uv run main.py create iota --size 100000
	uv run main.py create kappa --size 100000
	uv run main.py create lambda --size 100000
	uv run main.py create mu --size 100000
	uv run main.py create nu --size 100000
	uv run main.py create xi --size 100000
	uv run main.py create omicron --size 100000
	uv run main.py create pi --size 100000
	uv run main.py create rho --size 100000
	uv run main.py create sigma --size 100000
	uv run main.py create tau --size 100000
	uv run main.py create upsilon --size 100000
	uv run main.py create phi --size 100000
	uv run main.py create chi --size 100000
	uv run main.py create psi --size 100000
	uv run main.py create omega --size 100000
