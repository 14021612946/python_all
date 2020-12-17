CREATE DATABASE 销售数据库 CHARACTER SET utf8;

-- 创建article表
CREATE TABLE `Article`(
       商品号 CHAR(10)PRIMARY KEY,
       商品名 CHAR(10),
       单价   FLOAT(8),
       库存量 INT


);

-- 创建customer表
CREATE TABLE `customer`(
       顾客号  CHAR(10)PRIMARY KEY,
       顾客名  CHAR(10),
       性别    CHAR(2),
       年龄    INT
   
   
);       

  -- 创建orderitem表
CREATE TABLE orderitem(
        顾客号 CHAR(10),
        商品号 CHAR(10),
        数量   INT,
        购买价 FLOAT(8),
        购买日期 DATETIME,
        PRIMARY KEY(顾客号,商品号,购买日期)
          
);       

-- 设置article表约束
ALTER TABLE Article ADD CONSTRAINT CK_单价 CHECK (单价>0);

-- 创建外键
ALTER TABLE orderitem ADD CONSTRAINT  FK_article_orderitem FOREIGN KEY(商品号) REFERENCES article(商品号);


ALTER TABLE orderitem ADD CONSTRAINT  FK_customer_orderitem FOREIGN KEY(顾客号) REFERENCES customer(顾客号); 

-- 插入数据
INSERT INTO article VALUE('S001','计算机',5000,10)
,('S002','打印机',1000,12)
,('S003','洗衣机',800,10)
,('S004','电冰箱',1100,20);

INSERT INTO customer VALUE('G001','张兰','男',29)
,('G002','李四','女',25)
,('G003','王五','女',31)
,('G004','赵六','男',25);

INSERT INTO orderitem VALUE
('G001','S001',2,4000,'2015-08-16'),
('G001','S002',1,800,'2008-01-25'),
('G001','SOO3',3,600,'2008-01-25'),
('G001','S004',1,880,'2008-01-25'),
('G002','S001',3,4500,'2008-01-01'),
('G003','S001',1,5000,'2008-01-01'),
('G003','S002',1,1000,'2008-01-01');


