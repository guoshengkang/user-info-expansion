DROP table tmp_kgs_life_mobile_160000;

CREATE TABLE if not exists tmp_kgs_life_mobile_160000
(
mobile_no   STRING COMMENT '手机号',
label       STRING COMMENT '标记'
) 
comment "签名发送短信统计表"
-- PARTITIONED BY (ds STRING) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

INSERT INTO tmp_kgs_life_mobile_160000
SELECT
mobile_no,
label
FROM tmp_kgs_life_mobile_60000
UNION ALL
SELECT
mobile_no,
label
FROM tmp_kgs_life_mobile_100000  