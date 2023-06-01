CREATE TABLE ppr_raw_all(
    
    id SERIAL PRIMARY KEY NOT NULL,
    date_of_sale VARCHAR(55),
    address VARCHAR(255),
    postal_code VARCHAR(55),
    county VARCHAR(55),
    price VARCHAR(55),
    description VARCHAR(255)
    );

CREATE TABLE ppr_clean_all(
    
    id SERIAL PRIMARY KEY NOT NULL,
    date_of_sale DATE,
    address VARCHAR(255),
    postal_code VARCHAR(55),
    county VARCHAR(55),
    price INTEGER,
    description VARCHAR(255)
    );