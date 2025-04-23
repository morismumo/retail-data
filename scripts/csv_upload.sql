\c retail;

create table if not exists Amazon_Sale_Report (
    Index int not null,
    Order_id varchar(20),
    Date varchar(20),
    Status varchar(40),
    Fulfilment varchar(20),
    Sales_channel varchar(20),
    Ship_service_level varchar(20),
    Style varchar(20),
    Sku varchar(30),
    Category varchar(20),
    Size varchar(5),
    Asin varchar(20),
    Courier_status varchar(20),
    Qty int,
    Currency varchar(10),
    Amount decimal,
    Ship_city varchar(50),
    Ship_state varchar(50),
    Ship_postal_code varchar(20),
    Ship_country varchar(20),
    B2b varchar(10),
    Fullfilled_by varchar(20)
);

\copy Amazon_Sale_Report FROM 'scripts/mydata/silver/Amazon_Sale_Report.csv' DELIMITER ',' CSV HEADER;

create table if not exists International_sale_Report (
    Index int not null,
    Date varchar(20),
    Month varchar(10),
    Customer varchar(30),
    Style varchar(20),
    Sku varchar(30),
    Size varchar(5),
    Pcs decimal,
    Rate decimal,
    Gross_amt decimal
);

\copy International_sale_Report From 'scripts/mydata/silver/International_sale_Report.csv' DELIMITER ',' CSV HEADER;

create table if not exists May_2022 (
    Index int not null,
    Sku varchar(30),
    Style_id varchar(20),
    Catalog varchar(20),
    Category varchar(30)
    Weight decimal,
    Tp int,
    Mrp_old int,
    Final_mrp_old int,
    Ajio_mrp int,
    Amazon_mrp int,
    Amazon_fba_mrp int,
    FlipKart_mrp int,
    Limeroad_mrp int,
    Myntra_mrp int,
    Paytm_mrp int,
    Snapdeal_mrp int
);

\copy May-2022 From 'scripts/mydata/silver/May-2022.csv' DELIMITER ',' CSV HEADER;

create table if not exists March_2021 (
    Index int not null,
    Sku varchar(30),
    Style_id varchar(20),
    Catalog varchar(20),
    Category varchar(30)
    Weight decimal,
    Tp_1 int,
    Tp_2 int,
    Mrp_old int,
    Final_mrp_old int,
    Ajio_mrp int,
    Amazon_mrp int,
    Amazon_fba_mrp int,
    FlipKart_mrp int,
    Limeroad_mrp int,
    Myntra_mrp int,
    Paytm_mrp int,
    Snapdeal_mrp int
);

\copy May-2022 From 'scripts/mydata/silver/P__L_March_2021.csv' DELIMITER ',' CSV HEADER;

Create table if not exists Sale_Report.csv (
    Index int not null,
    Sku_code varchar(30),
    Design_no varchar(20),
    Stock int,
    Category varchar(30),
    Size varchar(10),
    Color varchar(15)
);

create table if not exists May-2022 (
    Index int not null,
    Sku varchar(30),
    Style_id varchar(20),
    Catalog varchar(20),
    Category varchar(30)
    Weight decimal,
    Tp int,
    Mrp_old int,
    Final_mrp_old int,
    Ajio_mrp int,
    Amazon_mrp int,
    Amazon_fba_mrp int,
    FlipKart_mrp int,
    Limeroad_mrp int,
    Myntra_mrp int,
    Paytm_mrp int,
    Snapdeal_mrp int
);

\copy May-2022 From 'scripts/mydata/silver/Sale_Report.csv' DELIMITER ',' CSV HEADER;