-- Query 3: schema
SELECT condition, COUNT(*) AS subject_count
FROM Subjects
GROUP BY condition;

-- Query 4: melanoma PBMC samples at baseline (treatment = 'tr1')
SELECT *
FROM Samples
WHERE condition = 'melanoma'
  AND sample_type = 'PBMC'
  AND time_from_treatment_start = 0
  AND treatment = 'tr1';

-- Query 5a: Count of samples by project (from filtered samples)
SELECT project, COUNT(*) AS sample_count
FROM Samples
WHERE condition = 'melanoma'
  AND sample_type = 'PBMC'
  AND time_from_treatment_start = 0
  AND treatment = 'tr1'
GROUP BY project;

-- Query 5b: Count of responders vs. non-responders (from filtered samples)
SELECT response, COUNT(*) AS count
FROM Samples
WHERE condition = 'melanoma'
  AND sample_type = 'PBMC'
  AND time_from_treatment_start = 0
  AND treatment = 'tr1'
GROUP BY response;

-- Query 5c:Count of males vs. females (from filtered samples)
SELECT sex, COUNT(*) AS count
FROM Samples
WHERE condition = 'melanoma'
  AND sample_type = 'PBMC'
  AND time_from_treatment_start = 0
  AND treatment = 'tr1'
GROUP BY sex;