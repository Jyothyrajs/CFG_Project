
CREATE DATABASE Productivity;

use Productivity;

CREATE TABLE TODO_LIST (
    Task VARCHAR(250) PRIMARY KEY,
    Priority INT,
    duration INT 
); 

SELECT * FROM TODO_LIST;
