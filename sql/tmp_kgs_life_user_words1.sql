DROP table tmp_kgs_life_user_words1;

CREATE TABLE if not exists tmp_kgs_life_user_words1
(
mobile_no          STRING COMMENT '手机号',
label              STRING COMMENT '标记',
tag_psb            MAP<STRING,STRING> COMMENT '用户画像标签',
token_t            MAP<STRING,STRING> COMMENT '物品描述',
subroots           ARRAY<STRING> COMMENT '物品类别'
) 
comment "签名发送短信统计表"
-- PARTITIONED BY (ds STRING) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
COLLECTION ITEMS TERMINATED BY '\073'
MAP KEYS TERMINATED BY '\072'
STORED AS TEXTFILE;

INSERT INTO tmp_kgs_life_user_words1
SELECT 
t1.mobile_no,
t1.label,
t2.tag_psb,
t3.token_t,
t4.subroots
FROM tmp_kgs_life_mobile_160000 t1
LEFT JOIN 
    (SELECT
    mobile_no,
    tag_psb
    FROM adl_person_tag_agg
    WHERE ds="2017-06-26"
    ) t2
ON t1.mobile_no=t2.mobile_no
LEFT JOIN
    (SELECT
    mobile_no,
    token_t
    FROM adl_limao_commodity_token_agg
    WHERE ds="2017-06-26"
    ) t3
ON t1.mobile_no=t3.mobile_no
LEFT JOIN
    (SELECT 
    mobile_no,
    collect_set(subroot_name) subroots
    FROM idl_limao_user_cidset_agg
    WHERE ds="2017-06-26"
    GROUP BY mobile_no
    ) t4
ON t1.mobile_no=t4.mobile_no;


