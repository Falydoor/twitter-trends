-- Create table
CREATE EXTERNAL TABLE
IF NOT EXISTS twitter.trend
(
  `name` string,
  `url` string,
  `promoted_content` string,
  `query` string,
  `tweet_volume` bigint
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = '1'
) LOCATION 's3://twitter-trends-tlebrunplaygrounde8fe0c54-1v2x25damodlr/'
TBLPROPERTIES
('has_encrypted_data'='false');

-- Select latest trends
SELECT
    date_parse(substr("$path", 61), '%Y-%m-%d %H:%i:%s') as date,
    tweet_volume as volume,
    name,
    url,
    query,
    promoted_content as promoted
FROM twitter.trend
WHERE tweet_volume > 0
ORDER BY date DESC;

-- Select trends with highest volume
SELECT
    name,
    MAX(tweet_volume)
FROM twitter.trend
GROUP BY name
ORDER BY MAX(tweet_volume) DESC;

-- Select trends with highest occurrence
SELECT *
FROM (SELECT name, COUNT(name) as count
    FROM twitter.trend
    GROUP BY name)
ORDER BY count desc;