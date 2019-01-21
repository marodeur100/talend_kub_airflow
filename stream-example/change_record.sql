select * from customer_nf where id<5 order by id;
update customer_nf set customeraddress=concat('Demo Test at ',cast(current_timestamp as text)) where id=4;
commit;
select * from customer_nf where id<5 order by id;


