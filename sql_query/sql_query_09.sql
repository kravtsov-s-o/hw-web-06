SELECT DISTINCT sub.name as course_name
FROM students s
JOIN marks m ON s.id = m.student_id
JOIN subjects sub ON m.subject_id = sub.id
WHERE s.name = 'Єлисавета Лавренко';