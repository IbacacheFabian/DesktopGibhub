-- 1. Crear 3 cursos nuevos
INSERT INTO cursos (nombre) VALUES 
    ('Curso de Matemáticas'),
    ('Curso de Historia'),
    ('Curso de Programación');

-- 2. Eliminar los 3 cursos que creaste
DELETE FROM cursos 
WHERE nombre IN ('Curso de Matemáticas', 'Curso de Historia', 'Curso de Programación');

-- 3. Crear otros 3 cursos nuevos
INSERT INTO cursos (nombre) VALUES 
    ('Curso de Física'),
    ('Curso de Filosofía'),
    ('Curso de Ingeniería');

-- 4. Crear 3 estudiantes que estén inscritos en el primer curso
INSERT INTO estudiantes (nombre, apellido, edad, curso_id) VALUES 
    ('Juan', 'Pérez', 20, 1),
    ('Ana', 'García', 22, 1),
    ('Luis', 'Martínez', 19, 1);

-- 5. Crear 3 estudiantes que estén inscritos en el segundo curso
INSERT INTO estudiantes (nombre, apellido, edad, curso_id) VALUES 
    ('Carlos', 'López', 21, 2),
    ('María', 'Rodríguez', 23, 2),
    ('Sofía', 'Hernández', 20, 2);

-- 6. Crear 3 estudiantes que estén inscritos en el tercer curso
INSERT INTO estudiantes (nombre, apellido, edad, curso_id) VALUES 
    ('Diego', 'Torres', 24, 3),
    ('Lucía', 'Ramírez', 25, 3),
    ('Paula', 'Castro', 22, 3);

-- 7. Recuperar todos los estudiantes que estén inscritos en el primer curso
SELECT * 
FROM estudiantes 
WHERE curso_id = 1;

-- 8. Recuperar todos los estudiantes que estén inscritos en el último curso
SELECT * 
FROM estudiantes 
WHERE curso_id = (SELECT MAX(id) FROM cursos);

-- 9. Recuperar el curso del último estudiante
SELECT c.*
FROM estudiantes e
JOIN cursos c ON e.curso_id = c.id
ORDER BY e.id DESC
LIMIT 1;
