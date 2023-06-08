USE forbes;

CREATE TABLE forbes_billionaires (
    person_name VARCHAR(100) NOT NULL,
    age INT,
    country VARCHAR(100),
    organization VARCHAR(100),
    PRIMARY KEY (person_name)
);

INSERT INTO forbes_billionaires (person_name, age, country, organization)
VALUES
    ('Phongthep Chiaravanont', 70, 'Thailand', 'Diversified'),
    ('Elon Musk', 54, 'USA', 'Tesla'),
    ('Jeff Bezos', 52, 'USA', 'Amazon Inc.'),
    ('Yogesh Kothari', 73, 'India', 'Speciality Chemicals');
