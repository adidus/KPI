INSERT INTO Typess(weight, road_id)
    (SELECT (trunc(random() + 1)),
            (SELECT road_id FROM Roads ORDER BY random() LIMIT 1) FROM generate_series(1, 3));

INSERT INTO Bicycles (brand, model, road_legal, type_id)
    (SELECT md5(random()::text),
            md5(random()::text),
            cast(cast(random() as integer) as boolean),
            (SELECT type_id FROM Typess ORDER BY random() LIMIT 1) FROM generate_series(1, 1));

INSERT INTO Owners (name, age, pro, bicycle_id, type_id)
    (SELECT md5(random()::text),
            (trunc(random() + 10)),
            (cast(cast(random() as integer) as boolean)),
            (SELECT bicycle_id FROM Bicycles ORDER BY random() LIMIT 1),
            (SELECT type_id FROM Typess ORDER BY random() LIMIT 1) FROM generate_series(1, 4));


--
-- INSERT INTO players(first_name, last_name, date_of_birth, is_injured, height, position_id, club_id)
-- (SELECT md5(random()::text),
--         md5(random()::text),
--         ('01.01.2000'::date -(random() * ('01.01.2000'::date -'01.01.1975'::date))::int),
--         random() > 0.5,
--         trunc(random() * 39 + 160),
--         trunc(random() * 3 + 1),
--         (SELECT club_id FROM clubs ORDER BY random() LIMIT 1) FROM generate_series(1, 4000));
--
--
-- INSERT INTO tournaments(name, description)
--     (SELECT md5(random()::text),
--         md5(random()::text) FROM generate_series(1, 1000));