To run server:
1. download project
2. install python (if missing)
3. open terminal
4. go to project location
5. type "python manage.py runserver [port number if needed]"

Requests endpoint - http://127.0.0.1:[port number]/api/birds

To execute task with database:
1. execute sql scripts (they will create procedures)
2. call the procedure you want:
    calc_colors_info - count amount of birds of each color
    calc_species_info -  count amount of birds of each species
    calc_stats - save stats of all birds into 'birds_stat' table (avg_body_length, median_body_length, mode_body_length
        avg_wingspan, median_wingspan, mode_wingspan)
