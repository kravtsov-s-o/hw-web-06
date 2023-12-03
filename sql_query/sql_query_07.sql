SELECT s.name AS student_name, m.mark
FROM students s
JOIN marks m ON s.id = m.student_id
JOIN subjects sub ON m.subject_id = sub.id
JOIN students_groups sg ON s.group_id = sg.id
WHERE sg.name = 'Група 1' AND sub.name = 'Няня';
