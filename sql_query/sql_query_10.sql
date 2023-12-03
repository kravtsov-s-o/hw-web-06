SELECT DISTINCT sub.name as course_name
FROM students s
JOIN marks m ON s.id = m.student_id
JOIN subjects sub ON m.subject_id = sub.id
JOIN teachers t ON sub.teacher_id = t.id
WHERE s.name = 'Єлисавета Лавренко' AND t.name = 'Вікторія Канівець';