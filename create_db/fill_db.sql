
INSERT INTO ogranizations (title, inn, created_at, udated_at)
VALUES 
	('����� ���������� ��������� ���', 74488, DATETIME('now', 'localtime'), DATETIME('now', 'localtime')),
	('����� ��������� ���', 7548, DATETIME('now', 'localtime'), DATETIME('now', 'localtime'));


INSERT INTO contractors (title, inn, created_at)
VALUES
	('����-������ ���', 8364028, DATETIME('now', 'localtime')),
	('�������� ����� ���', 093487, DATETIME('now', 'localtime')),
	('�������� ��������� ���', 98763, DATETIME('now', 'localtime')),
	('�������������� ������� ���', 67537613, DATETIME('now', 'localtime')),
	('�������� � ����������� ���', 8374322, DATETIME('now', 'localtime')),
	('�����-�� ����������� ���', 8763487, DATETIME('now', 'localtime')),
	('������������ � ������� ���', 9748932, DATETIME('now', 'localtime')),
	('��������� ����� ���', 32451435, DATETIME('now', 'localtime'));
	
-- DELETE FROM contractors;


INSERT INTO builders (title, inn, created_at)
VALUES
	('����������� ���', 9845792, DATETIME('now', 'localtime')),
	('���������� ������ � ������������� ���', 9274942, DATETIME('now', 'localtime')),
	('��������� ������������ ���', 9827371, DATETIME('now', 'localtime')),
	('������ � ���� ���', 3452573, DATETIME('now', 'localtime')),
	('�������� �� ���', 983272, DATETIME('now', 'localtime')),
	('���������� �� ���� ���', 736784, DATETIME('now', 'localtime'));

-- DELETE FROM builders;

INSERT INTO projects (title, organization_id, created_at)
VALUES
	('�� 34/34', 1, DATETIME('now', 'localtime')),
	('�� 30/34', 1, DATETIME('now', 'localtime')),
	('�� 15/33', 1, DATETIME('now', 'localtime')),
	('������������ 40/34', 1, DATETIME('now', 'localtime')),
	('�-� 23/���������', 2, DATETIME('now', 'localtime')),
	('�� 3/���������', 2, DATETIME('now', 'localtime')),
	('�� 5/���������', 2, DATETIME('now', 'localtime')),
	('�� 7/���������', 2, DATETIME('now', 'localtime'));


INSERT INTO workpacks (title, created_at)
VALUES
	('���������������� ������', DATETIME('now', 'localtime')),
	('�������� ������', DATETIME('now', 'localtime')),
	('����������', DATETIME('now', 'localtime')),
	('����������� ������� ��������������', DATETIME('now', 'localtime')),
	('���������� ������', DATETIME('now', 'localtime')),
	('���������� ������', DATETIME('now', 'localtime')),
	('��������������� ������', DATETIME('now', 'localtime'));
	

INSERT INTO contracts (title, project_id, organization_id, contractor_id, from_date, created_at)
VALUES
	('1/125-2014/��', 5, 2, 38, DATE('2014-04-18'), DATETIME('now', 'localtime')),
	('3/127-2015/���', 1, 1, 42, DATE('2015-01-10'), DATETIME('now', 'localtime')),
	('17/003-2017/���', 3, 1, 39, DATE('2013-06-11'), DATETIME('now', 'localtime')),
	('125/125-2014/��', 7, 2, 45, DATE('2014-07-23'), DATETIME('now', 'localtime')),
	('2/009-2015/���', 2, 1, 40, DATE('2015-09-01'), DATETIME('now', 'localtime')),
	('17/123-2015/���', 4, 1, 41, DATE('2015-11-13'), DATETIME('now', 'localtime')),
	('115/008-2020/��', 6, 2, 43, DATE('2020-05-03'), DATETIME('now', 'localtime')),
	('25/003-2021/��', 8, 2, 44, DATE('2013-06-11'), DATETIME('now', 'localtime')),
	('11/125-2014/���', 1, 1, 45, DATE('2014-04-28'), DATETIME('now', 'localtime')),
	('30/127-2015/��', 5, 2, 39, DATE('2015-10-01'), DATETIME('now', 'localtime')),
	('117/003-2017/��', 6, 2, 40, DATE('2013-06-12'), DATETIME('now', 'localtime')),
	('12/125-2014/���', 2, 1, 41, DATE('2014-08-24'), DATETIME('now', 'localtime')),
	('20/009-2015/��', 3, 2, 38, DATE('2015-12-10'), DATETIME('now', 'localtime')),
	('170/123-2015/��', 7, 2, 42, DATE('2015-01-13'), DATETIME('now', 'localtime')),
	('11/008-2020/���', 4, 1, 43, DATE('2020-07-13'), DATETIME('now', 'localtime')),
	('251/003-2021/���', 8, 1, 44, DATE('2021-06-21'), DATETIME('now', 'localtime'));


-- DELETE FROM contracts;


INSERT INTO specs (title, contract_id, workpack_id, amount)
VALUES
	('1', 17, 1, 1000.25),
	('21', 18, 1, 250000),
	('3', 19, 2, 342000),
	('5', 20, 2, 115000),
	('7', 21, 3, 1864213),
	('17', 22, 3, 37488),
	('14', 23, 4, 8243),
	('326', 24, 4, 723676),
	('245', 25, 5, 3761),
	('113', 26, 5, 87126),
	('35', 27, 6, 376193),
	('34', 28, 6, 3879192),
	('24', 29, 7, 100000),
	('123', 30, 7, 1354200),
	('12', 31, 1, 1133311),
	('4', 32, 2, 200000);


INSERT INTO types (title)
VALUES
	('�������� �����'),
	('���������� � �����������'),
	('���������'),
	('����������� ����������'),
	('��������������� ����������'),
	('���������'),
	('����������������'),
	('�������'),
	('�����������');


INSERT INTO services (title, type_id, created_at)
VALUES
	('CGC___ ������ ���������� ������������ � ������� ����� 1.0 �3', 4, DATETIME('now', 'localtime')),
	('CGC___ ������ ���������� ������������ � ������� ����� 1.4 �3', 4, DATETIME('now', 'localtime')),
	('CGC___ ������ ���������� ���������������� ����������������� 3.5�', 5, DATETIME('now', 'localtime')),
	('CGC___ ������ ���������� ���������������� ����������������� 5�', 5, DATETIME('now', 'localtime')),
	('CGC___ ������ ���������� ���������������� ����������������� 10�', 5, DATETIME('now', 'localtime')),
	('CGC___ ������ ���������� ��������� 180 �.�.', 2,  DATETIME('now', 'localtime')),
	('CGC___ ������ ���������� ��������� 320 �.�.', 2,  DATETIME('now', 'localtime')),
	('CGC___ ������ ����������� � ������� ����� 0.4�3', 2,  DATETIME('now', 'localtime')),
	('CGC___ ������ ����������� � ������� ����� 1�3', 2,  DATETIME('now', 'localtime')),
	('CGC___ ������ ����������� � ������� ����� 1,4�3', 2,  DATETIME('now', 'localtime')),
	('CGC___ ������ ��������� �/� 25�', 3, DATETIME('now', 'localtime')),
	('CGC___ ������ ��������� �/� 40�', 3, DATETIME('now', 'localtime')),
	('CGC___ ������ ��������� �/� 75�', 3, DATETIME('now', 'localtime')),
	('CGC___ ������ ��������� ����� �/� 8�', 1, DATETIME('now', 'localtime')),
	('CGC___ ������ ���������� �/� 10�', 6, DATETIME('now', 'localtime')),
	('CGC___ ������ ���������� �/� 16�', 6, DATETIME('now', 'localtime')),
	('CGC___ ������ ���������� �/� 24�', 6, DATETIME('now', 'localtime')),
	('CGC___ ������ ��� � ������� ������ 36�', 7, DATETIME('now', 'localtime')),
	('CGC___ ������ ��� � ������� ������ 40�', 7, DATETIME('now', 'localtime')),
	('CGC___ ������ ��� � ������� ������ 52�', 7, DATETIME('now', 'localtime')),
	('CGC___ ������ ��� ������� 3�3', 8, DATETIME('now', 'localtime')),
	('CGC___ ������ ��� ������� 6�3', 8, DATETIME('now', 'localtime')),
	('CGC___ ������ ��� ������� 9�3', 8, DATETIME('now', 'localtime')),
	('CGC___ ������ ��� ������� 12�3', 8, DATETIME('now', 'localtime')),
	('CGC___ ������ ������������ �������� �/� 20�', 9,  DATETIME('now', 'localtime'));
	
	
	
	








































	