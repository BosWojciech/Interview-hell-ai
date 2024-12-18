CREATE TABLE JobOffers (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL
);

CREATE TABLE Categories (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE Questions (
    id SERIAL PRIMARY KEY,
    job_offer_id INT REFERENCES JobOffers(id),
    category_id INT REFERENCES Categories(id),
    text TEXT NOT NULL,
    rating INT
);

CREATE TABLE Answers (
    id SERIAL PRIMARY KEY,
    question_id INT REFERENCES Questions(id),
    text TEXT NOT NULL,
    ai_rating INT,
    user_feedback INT
);
