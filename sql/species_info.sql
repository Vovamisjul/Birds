drop procedure if exists calc_species_info();

create procedure calc_species_info() as
$$
declare
    bird_species record;
    bird  record;
begin
    for bird_species in select unnest(enum_range(NULL::bird_species)) as species_name
        loop
            insert into bird_species_info values (bird_species.species_name, 0);
        end loop;
    for bird in select * from birds
        loop
            update bird_species_info set count = count + 1 where species = bird.species;
        end loop;
end;
$$ LANGUAGE plpgsql;