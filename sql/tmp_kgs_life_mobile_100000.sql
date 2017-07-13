DROP table tmp_kgs_life_mobile_100000;

CREATE TABLE if not exists tmp_kgs_life_mobile_100000
(
mobile_no   STRING COMMENT '手机号',
label       STRING COMMENT '标记'
) 
comment "签名发送短信统计表"
-- PARTITIONED BY (ds STRING) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

INSERT INTO tmp_kgs_life_mobile_100000
SELECT
mobile_no,
"100000" AS label
FROM
    (SELECT
    mobile_no,
    row_number()over(ORDER BY rand_k DESC) AS ranks
    FROM
        (SELECT
        mobile_no,
        rand() rand_k
        FROM adl_person_tag_agg
        WHERE ds="2017-06-26"
        limit 50000000
        ) t1
    ) t2
WHERE ranks<=100000;
