COPY wines(fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur,
total_sulfur, density, ph, sulphates, alcohol, quality, good, wine_id)
FROM 'wine_sql_data.csv' DELIMITER ',' CSV HEADER;

