# 學習心得
本周 pandas 課程，了解到潘大師的強大之處，傳統程式語言(java,c#) 需要花費不少代碼的功能，利用潘大師只需要幾行即可解決。
後續會再觀看其他參考資料來好好把pandas 學好。



# 本周作業
作业背景：在数据处理的步骤中，可以使用 SQL 语句或者 pandas 加 Python 库、函数等方式进行数据的清洗和处理工作。
因此需要你能够掌握基本的 SQL 语句和 pandas 等价的语句，利用 Python 的函数高效地做聚合等操作。
作业要求：请将以下的 SQL 语句翻译成 pandas 语句：

```SQL
1. SELECT * FROM data;
 
2. SELECT * FROM data LIMIT 10;
 
3. SELECT id FROM data;  //id 是 data 表的特定一列
 
4. SELECT COUNT(id) FROM data;
 
5. SELECT * FROM data WHERE id<1000 AND age>30;
 
6. SELECT id,COUNT(DISTINCT order_id) FROM table1 GROUP BY id;
 
7. SELECT * FROM table1 t1 INNER JOIN table2 t2 ON t1.id = t2.id;
 
8. SELECT * FROM table1 UNION SELECT * FROM table2;
 
9. DELETE FROM table1 WHERE id=10;
 
10. ALTER TABLE table1 DROP COLUMN column_name;
```