with generic_json (doc) as (
   values
    ('{data}'::json)
)
insert into client (id, name, payment)
select p.*
from generic_json l
  cross join lateral json_populate_recordset(null::client, doc) as p
on conflict (id) do update
  set name = excluded.name,
      payment = excluded.payment;
