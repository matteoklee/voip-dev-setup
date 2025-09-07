
INSERT INTO subscriber (id, username, domain, password, ha1, ha1b)
VALUES
  (1001, 'alice', 'localhost',
   'alicepw',
   MD5(CONCAT('alice', ':', 'localhost', ':', 'alicepw')),
   MD5(CONCAT('alice', '@localhost', ':', 'example.com', ':', 'alicepw'))),

  (1002, 'bob', 'localhost',
   'bobpw',
   MD5(CONCAT('bob', ':', 'localhost', ':', 'bobpw')),
   MD5(CONCAT('bob', '@localhost', ':', 'example.com', ':', 'bobpw')));
