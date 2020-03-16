with generic_json (doc) as (
   values
    ('{data}'::json)
)
insert into period (client_id, month, year, value, is_pay)
select p.*
from generic_json l
  cross join lateral json_populate_recordset(null::period, doc) as p
on conflict (client_id,month, year) do update
  set value = excluded.value,
      is_pay = excluded.is_pay;
