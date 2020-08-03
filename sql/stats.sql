drop procedure if exists calc_stats();

create procedure calc_stats() as
$$
declare
    avg_body_length    numeric;
    median_body_length numeric;
    mode_body_length   numeric;
    avg_wingspan       numeric;
    median_wingspan    numeric;
    mode_wingspan      numeric;
begin
    select avg(body_length) from birds into avg_body_length;
    select avg(wingspan) from birds into avg_wingspan;
    select percentile_disc(0.5) within group ( order by body_length ) from birds into median_body_length;
    select percentile_disc(0.5) within group ( order by wingspan ) from birds into median_wingspan;
    SELECT mode() WITHIN GROUP (ORDER BY body_length) FROM birds into mode_body_length;
    SELECT mode() WITHIN GROUP (ORDER BY wingspan) FROM birds into mode_wingspan;
    insert into birds_stat values (avg_body_length, median_body_length, array[mode_body_length], avg_wingspan, median_wingspan, array[mode_wingspan]);
end ;
$$ LANGUAGE plpgsql;