SET search_path = 'parser';

BEGIN;

INSERT INTO django_site(id, domain, name) VALUES (1, 'example.com', 'example.com');

COMMIT;
