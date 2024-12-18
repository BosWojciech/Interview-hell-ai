-- Insert job offers
INSERT INTO JobOffers (title) VALUES
    ('Satan''s Butt Scratcher'),
    ('Hell''s Lava Pool Lifeguard'),
    ('Eternal Screams DJ'),
    ('Infernal Flame Adjuster'),
    ('Demon Horn Polisher'),
    ('Purgatory Queue Manager'),
    ('Human Feet Tickler Engineer'),
    ('Soul Contracts Lawyer'),
    ('Hellhound Groomer'),
    ('Pit of Despair Tour Guide'),
    ('Toilet Cleaner (Lava-resistant)'),
    ('Torture Chamber Sound Designer'),
    ('Chainsaw Blade Sharpener'),
    ('Sin Counting Accountant'),
    ('Demonic Karaoke Host'),
    ('Bone Furniture Assembler'),
    ('Sulfur Smell Tester'),
    ('Fireproof Cloak Designer'),
    ('Ash Sorting Specialist'),
    ('Nightmare Architect'),
    ('Ginger People Torture Specialist');


-- Insert categories
INSERT INTO Categories (name) VALUES
    ('HR'),
    ('Technical'),
    ('Problem Solving');

-- Insert questions for job offers
-- Example for "Satan's Butt Scratcher"
INSERT INTO Questions (job_offer_id, category_id, text) VALUES
    (1, 1, 'Why do you think you are the best fit for scratching Satan''s butt?'),
    (1, 1, 'What motivates you to work in such a personal role?'),
    (1, 1, 'How do you handle situations where Satan might be unhappy with your work?'),
    (1, 2, 'What tools or techniques would you use for optimal butt-scratching?'),
    (1, 2, 'Describe your past experience with similar tasks.'),
    (1, 2, 'How would you innovate in the field of infernal hygiene?'),
    (1, 3, 'What would you do if Satan''s tail got in the way?'),
    (1, 3, 'How would you handle a situation where lava spilled during your task?'),
    (1, 3, 'If your scratching tool breaks, how do you improvise?');

-- Example for "Hell's Lava Pool Lifeguard"
INSERT INTO Questions (job_offer_id, category_id, text) VALUES
    (2, 1, 'Why do you want to save souls who are already in Hell?'),
    (2, 1, 'How do you keep morale high when no one wants to be saved?'),
    (2, 1, 'What makes you passionate about lifeguarding in a lava pool?'),
    (2, 2, 'How do you ensure safety when the pool is boiling at 2000°C?'),
    (2, 2, 'What equipment would you use to rescue a drowning soul?'),
    (2, 2, 'Describe your approach to managing lava currents.'),
    (2, 3, 'What would you do if two souls started fighting in the pool?'),
    (2, 3, 'How would you handle a soul pretending to drown for attention?'),
    (2, 3, 'What steps do you take if a lava shark enters the pool?');

-- Example for "Eternal Screams DJ"
INSERT INTO Questions (job_offer_id, category_id, text) VALUES
    (3, 1, 'What music genres inspire your creativity as a DJ?'),
    (3, 1, 'How do you handle criticism from demons about your playlist?'),
    (3, 1, 'Why do you think you can make eternal screams sound enjoyable?'),
    (3, 2, 'What mixing techniques would you use for blending screams and beats?'),
    (3, 2, 'Describe your experience working with tortured souls as backup singers.'),
    (3, 2, 'How do you maintain your equipment in an environment of eternal despair?'),
    (3, 3, 'What would you do if a demon smashed your DJ console during a gig?'),
    (3, 3, 'How would you handle a riot on the dance floor of agony?'),
    (3, 3, 'If your headphones catch fire mid-performance, what''s your backup plan?');

-- Example for "Ginger People Torture Specialist"
INSERT INTO Questions (job_offer_id, category_id, text) VALUES
    (21, 1, 'Why do you think you have the perfect temperament for torturing ginger people?'),
    (21, 1, 'What motivates you to work in a role focused on such specific targets?'),
    (21, 1, 'How do you ensure professional boundaries when dealing with fiery personalities?'),
    (21, 1, 'What makes you passionate about joining Hell Inc. in this unique capacity?'),
    (21, 1, 'How do you approach situations where a ginger person might be unbreakable?'),
    (21, 2, 'What tools or methods do you consider most effective for torturing gingers?'),
    (21, 2, 'Describe your experience with flame-resistant instruments.'),
    (21, 2, 'How would you adjust your methods for redheads with extra resilience?'),
    (21, 2, 'What is your preferred technique for balancing physical and psychological torture?'),
    (21, 2, 'How do you innovate in the field of demonic torment targeting specific traits?'),
    (21, 3, 'How would you handle a situation where the subject starts singing loudly to disrupt your work?'),
    (21, 3, 'What would you do if a ginger person escaped mid-session?'),
    (21, 3, 'How would you modify your approach if their fiery hair literally caught fire?'),
    (21, 3, 'What steps would you take if your primary tools were confiscated by Hell''s HR department?'),
    (21, 3, 'How do you handle situations where the subject starts negotiating terms of their torment?'),
    (21, 3, 'What would you do if a fellow demon challenged your methods during a live torture demonstration?'),
    (21, 3, 'How would you improvise if a new regulation banned the use of traditional fire techniques?'),
    (21, 3, 'What creative solutions would you employ if your tools melted in the infernal heat?'),
    (21, 3, 'How would you manage a session when the audience of demons starts booing your performance?');

