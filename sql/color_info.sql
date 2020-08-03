drop procedure if exists calc_colors_info();

create procedure calc_colors_info() as
$$
declare
    bird_color record;
    bird  record;
begin
    for bird_color in select unnest(enum_range(NULL::bird_color)) as color_name
        loop
            insert into bird_colors_info values (bird_color.color_name, 0);
        end loop;
    for bird in select * from birds
        loop
            update bird_colors_info set count = count + 1 where color = bird.color;
        end loop;
end;
$$ LANGUAGE plpgsql;