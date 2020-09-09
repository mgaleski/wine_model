CREATE TABLE wines (
    fixed_acidity FLOAT,
    volatile_acidity FLOAT,
    citric_acid FLOAT,
    residual_sugar FLOAT,
    chlorides FLOAT,
    free_sulfur INT ,
    total_sulfur INT,
    density FLOAT,
    ph FLOAT,
    sulphates FLOAT,
    alcohol FLOAT,
    quality INT,
    good BOOLEAN,
    color STRING,
    wine_id INT NOT NULL,
    PRIMARY KEY (wine_id)
);


