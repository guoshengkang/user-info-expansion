DROP table tmp_kgs_life_user_words;

CREATE TABLE if not exists tmp_kgs_life_user_words
(
mobile_no          STRING COMMENT '手机号',
label              STRING COMMENT '标记',
tag_psb            MAP<STRING,STRING> COMMENT '用户画像标签',
token_t            MAP<STRING,STRING> COMMENT '物品描述',
subroots           ARRAY<STRING> COMMENT '物品类别',
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

INSERT INTO tmp_kgs_life_user_words
SELECT 
t1.mobile_no,
t1.label,
t1.tag_psb,
t1.token_t,
t1.subroots,
t2.gender,
t2.occupation,
t2.level_edu
FROM tmp_kgs_life_user_words1 t1
LEFT JOIN tmp_kgs_life_user_words2 t2
ON t1.mobile_no=t2.mobile_no
AND t1.label=t2.label;