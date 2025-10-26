create table if not exists client (
	  id uuid default gen_random_uuid() primary key
	, name text not null unique
);

create table if not exists line (
	  id uuid default gen_random_uuid() not null
	, length double precision not null
	, name text not null
	, client_id uuid references client(id) 
	)
	partition by list (client_id)
;
alter table line enable row level security;

create role client_user with login password 'test';

grant usage on schema public to client_user;
grant select on all tables in schema public to client_user;

create policy line_policy
	on public.line 
	to client_user 
	using (client_id = current_setting('my.current_client_id')::uuid);

-- create policy line_policy
-- 	on public.line 
-- 	to client_user 
-- 	using (client_id = (select id from client where name = current_setting('my.current_client_name')));

-- The above two policies should be equivalent in terms of security and performance. Strangely the latter, while obviously easier to use since you don't need pre-knowledge of the id, just the name of the client, produces a bunch of "never executed" subplans per `EXPLAIN ANALYZE`. This doesn't seem to have an impact on planning time, but possibly it would if the client table was larger.
