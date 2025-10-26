create table if not exists client (
	  id uuid default gen_random_uuid() primary key
	, name text not null unique
);

create table if not exists lines (
	  id uuid default gen_random_uuid() not null
	, length double precision not null
	, name text not null
	, client_id uuid references client(id) 
	)
	partition by list (client_id)
;
alter table lines enable row level security;

create role client_user with login password 'test';

grant usage on schema public to client_user;
grant select on all tables in schema public to client_user;

create policy lines_policy
	on public.lines 
	to client_user 
	using (client_id = current_setting('my.current_client_id')::uuid);
