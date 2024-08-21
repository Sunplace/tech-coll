# Elasticsearch

## Catalog
1. Elastisearch是什么
    1. 定义（Elasticsearch是什么，Lucene是什么）
    2. 功能、优势、特性
        1. 全文搜索
        2. 结构化搜索
        3. 聚合分析
        4. 接近实时的搜索
        5. 高性能，集群，负载均衡
        6. 分布式，高可用性，水平扩展性
        7. Restful API，JSON-based document，多种编程语言接入
        8. 开源软件，活跃的社区，丰富的生态
    3. 使用场景
        1. 存储、搜索、分析日志、指标、安全事件等数据。（ELK）
        2. 网站搜索，垂直搜索，代码搜索。（The nytimes，Github，stack overflow）
        3. 商业数据分析，Business Intelligence and Analytics。（Walmart，Netflix）
        4. 商品搜索。（Ebay）
        5. 企业级搜索引擎。（Pfizer） 
2. Elasticsearch是如何工作的
    1. ES vs MySql
    2. 文档与字段
    3. 索引与映射
    4. 索引的CRUD
    5. 文档的CRUD
    6. 倒排索引
    7. 文本与分词
    8. 接近实时的搜索
    9. 搜索
        1. 全文搜索
        2. 关键字搜索
        3. 组合搜索
    10. 聚合
        1. 指标聚合
        2. 桶聚合
    11. 分片与副本
    12. 节点与集群
3. Elasticsearch的应用
    1. 日志收集、存储、搜索、分析。（ELK）
    2. 垂直搜索。（药品信息搜索）
    3. 数据分析。
    4. 全文搜索。（ELK日志搜索，Google搜索）
    5. 全文搜索，企业搜索。（Github docs，Github Code）
4. Elasticsearch所针对的数据
    1. 最好是那种不需要更新的数据。
    2. 最好是那种不需要删除的数据。
    3. 最好是那种只需要频繁写入新数据。
    4. 主要是为了查询、搜索、分析。
    5. 比如日志数据，销售数据，某种记录数据，带时间戳那种。

## Special thanks
引用了很多文档，感谢文档作者的辛苦付出。

特别的感谢这篇文章的作者，[thanks](https://www.cnblogs.com/buchizicai/p/17093719.html)。