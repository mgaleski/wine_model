CREATE TABLE wines (
    fixed_acidity FLOAT   NOT NULL,
    volatile_acidity FLOAT   NOT NULL,
    citric_acid FLOAT,
    residual_sugar FLOAT   NOT NULL,
    chlorides FLOAT   NOT NULL,
    free_sulfur INT   NOT NULL,
    total_sulfur INT,
    density FLOAT,
    ph FLOAT,
    sulphates FLOAT,
    alcohol FLOAT,
    quality INT,
    good BOOLEAN,
    wine_id INT NOT NULL,
    PRIMARY KEY (wine_id)
);


