DROP table tmp_kgs_life_mobile_60000;

CREATE TABLE if not exists tmp_kgs_life_mobile_60000
(
mobile_no   STRING COMMENT '手机号',
label       STRING COMMENT '标记'
) 
comment "签名发送短信统计表"
-- PARTITIONED BY (ds STRING) 
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE;

INSERT INTO tmp_kgs_life_mobile_60000
SELECT
t.mobile_no,
t.label
FROM
    (SELECT
    t1.mobile_no,
    "60000" AS label,
    row_number()over(ORDER BY rand_k DESC) AS ranks
    FROM 
        (SELECT
        DISTINCT mobile_no AS mobile_no,
        rand() rand_k
        FROM idl_msg_received_join_log
        WHERE msg_type="消息通知"
        AND msg_industry="生活服务"
        ) t1
    LEFT JOIN
        (SELECT
        mobile_no
        FROM adl_person_tag_agg
        WHERE ds="2017-06-26"
        ) t2
    ON t1.mobile_no=t2.mobile_no
    WHERE t2.mobile_no IS NOT NULL
    ) t
WHERE ranks<=60000;
