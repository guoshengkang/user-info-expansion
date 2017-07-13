DROP table tmp_kgs_life_user_words2;

CREATE TABLE if not exists tmp_kgs_life_user_words2
(
mobile_no          STRING COMMENT '手机号',
label              STRING COMMENT '标记',
gender             STRING COMMENT '性别',
occupation         STRING COMMENT '职业',
level_edu          STRING COMMENT '教育程度'
) 
comment "签名发送短信统计表"
-- PARTITIONED BY (ds STRING) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY '\073'
MAP KEYS TERMINATED BY '\072'
STORED AS TEXTFILE;

INSERT INTO tmp_kgs_life_user_words2
SELECT 
t1.mobile_no,
t1.label,
t2.gender,
t3.occupation,
t4.level_edu
FROM tmp_kgs_life_mobile_160000 t1
LEFT JOIN
    (SELECT
    mobile_no,
    IF(prob_male>0.5,'男性','女性') AS gender
    FROM idl_user_gender_prob_agg
    WHERE ds="2017-06-26"
    ) t2
On t1.mobile_no=t2.mobile_no
LEFT JOIN
    (SELECT
    mobile_no,
    occupation
    FROM idl_user_address_summar_agg
    WHERE ds="2017-06-26"
    ) t3
ON t1.mobile_no=t3.mobile_no
LEFT JOIN
    (SELECT
    mobile_no,
    IF(level_edu=0,'大学',IF(level_edu=1,'高中','初中')) level_edu
    FROM idl_user_eduagenet_level_agg
    WHERE ds="2017-06-26"
    ) t4
ON t1.mobile_no=t4.mobile_no;